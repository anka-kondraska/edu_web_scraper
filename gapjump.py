import urllib2
from bs4 import BeautifulSoup
import csv
import re
import json
import mechanize
import sys
import profiles_db
import degree_pie_chart

# when running this python script, specify second argument as the csv data file
# e.g. python gapjump.py test_profiles.csv
csv_file = sys.argv[1]
# count degrees for pie chart
count_degrees = []

def find_gender(first_name):
    """Find gender based on first name scraping behindthename.com
       and genderize.io"""
    behindthename1 = "https://api.genderize.io/?name="
    page1 = urllib2.urlopen(behindthename1+first_name)
    soup1 = BeautifulSoup(page1, 'html.parser')
    gender=json.loads(str(soup1))
    behindthename2 = "http://www.behindthename.com/name/"
    page2 = urllib2.urlopen(behindthename2+first_name)
    soup2 = BeautifulSoup(page2, 'html.parser')
    # scraping genderize.io
    if gender["gender"] == "female":
        return "F"
    elif gender["gender"] == "male":
        return "M"
    else:
        # if not found, scraping behindthename.com
        name_f = soup2.find(class_="fem")
        name_m = soup2.find(class_="masc")
        error = soup2.find('p', attrs={'class' : 'error'})
        if error:
            return "Unknown"
        elif name_f and name_m:
            return "F/M"
        elif name_f:
            return "F"
        else:
            return "M"


with open(csv_file) as csvfile1:
    reader = csv.DictReader(csvfile1)
    for row in reader:
        first_name = row['Full Name'].split(' ')[0]
        if "(" in first_name:
            first_name = re.search(r'\((.*?)\)',first_name).group(1)

        middle_name = row['Full Name'].split(' ')[1:-1]
        if middle_name:
            middle_name = row['Full Name'].split(' ')[1:-1][0]
        else:
            middle_name = ''
        last_name = row['Full Name'].split(' ')[-1]
        email = row['Email']
    
        

        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.set_handle_equiv(False)
        br.addheaders = [('User-agent', 'Chrome/55.0.2883.95')] 
        br.open('http://www.google.com/')   

        # do the query
        br.select_form(name='f') 
        if email.endswith(".edu"):
            print email
            br.form['q'] = email # query
        else:
            br.form['q'] = first_name+' '+last_name # query

        data = br.submit()
        soup = BeautifulSoup(data.read(), 'html.parser', from_encoding='utf-8')
        #each search result description
        # desc = soup.findAll('span', attrs={'class': 'st'})
        #linkedin headlines
        # desc2 = soup.findAll('div', attrs={'class': 'f', 'class' : 'slp'})
        # for de in desc2:
        #     print de
        #     print



        #DEGREE

        degree = None
        doc =[ "PhD","Assistant Professor"]
        bs = ["B.A.","BA","B.S.","BS","Student","Undergraduate"]
        ms = ["M.S.","Graduate Student", "MS", "Adjunct Instructor","Associate Instructor"]
        mba = ["MBA", "M.B.A"]
        try:
            #linkedin headline if any
            desc2 = soup.find('div', attrs={'class': 'f', 'class' : 'slp'}).get_text()
            # print desc2
            if any(d in desc2 for d in doc):
                degree = "PhD"
            elif any(a in desc2 for a in mba):
                degree = "MBA"
            elif any(m in desc2 for m in ms):
                degree = "MS/MA"
            elif any(b in desc2 for b in bs):
                degree = "BA/BS"
            else:
                degree = "None"
        except AttributeError:
        # all search descriptions 
            desc = soup.findAll('span', attrs={'class': 'st'})
            for des in desc:
                des = des.get_text()
                # print des
                if any(d in des for d in doc):
                    degree = "PhD"
                    break
                elif any(a in des for a in mba):
                    degree = "MBA"
                    break
                elif any(m in des for m in ms):
                    degree = "MS/MA"
                    break
                elif any(b in des for b in bs):
                    degree = "BA/BS"
                    break
                else:
                    degree="None"
        #UNIVERSITY
        pattern = "([A-Z][^\s,.]+[.]?\s[(]?)*(College|University|Institute|Law School|School of|Academy)[^,\d]*(?=,|\d)"
        university = None
        try:
            #linkedin headline if any
            desc2 = soup.find('div', attrs={'class': 'f', 'class' : 'slp'}).get_text()
            match = re.search(pattern, desc2, flags=re.MULTILINE)
           
            if match:
                university = match.group()
                print university

            
        except AttributeError:
        # all search descriptions 
            desc = soup.findAll('span', attrs={'class': 'st'})
            for des in desc:
                des = des.get_text()
                # print des
                match = re.search(pattern, des, flags=re.MULTILINE)
                
                if match:
                    university = match.group()
                    print university
                    break
        count_degrees.append(degree)
        # gender = find_gender(first_name)     
        print first_name, degree, university

        # Add to database
        profiles_db.add_to_db(first_name, last_name, degree, university)
            
# close the csv file
csvfile1.close()
# generate pie chart upon completion
degree_pie_chart.create_pie_chart(count_degrees)






