Software Design Document - SDD for edu_web_scraper

Overview:<br/>
edu_web_scraper scrapes the web, specifically google search results for gender and educational information
based on full name and email address.

It takes a csv file as input with full name and email address columns. It runs google search on each name
and/or email address and scrapes the educational degree and educational institution associated with each name
and/or email adddress. It also scrapes genderize.io and behindthename.com for gender information
based on first name.

At this point it is a Python script. There is no UI to speak of. To run it in your terminal specify 
the script file and test names/emails csv file to be discovered:<br/>

python gapjump.py test_profiles.csv

Upon completion pie chart is saved to your local directory/machine with the degree breakdown
among the individuals listed in the csv file.

## Table of Contents📖

* [Database](#database)
* [Scraping](#scraping)
* [Pie Chart](#pie chart)
* [Requirements](#requirements)

## <a name="scraping"></a>Scraping

I am using google search results to scrape the educational data.

I first attempted to find the technologies that would make scraping this type of data
easier and more accurate i.e. LinkedIn and Rapportive. LinkedIn does not allow
it's pages to be scraped. And their API was revised to not include people search.
Your application can request access to custom API endpoints but that would require
getiing in touch personally and going through vetting process. Not something I could do on a 
3 day coding challenge. Rapportive used to have an API, from what I have read, but no longer does.
Too much potential for abuse.

I resorted to google search result scraping paying special attention to
LinkedIn headlines which appear in a seperate div in google search results, then going through
the search results descriptions for any traces of educational data for a given name
search result.

This does not produce the most accurate results. Understanding more about the needs
of this project I would want to fine tune the scraping results. Perhaps grabbing all
educational data which comes up in a single google search for that person's name and then email address, and analyzing it, and arriving at most frequently mentioned university or degree for that name. That would yield more accurate results. At the same time, sometimes, it is hard to know
whether you have the correct person.

I would also try using selenium to possibly scrape LinkedIn's site results, as it seems
some people have been successful. This woudl require more research as I am not certain
if thats against LinkedIn's terms of use.

The goal in further pursuing it would be to arrive at better results: either fine tiuning or finding other ways of scraping. So far reasearch on other scraping methods of this particular data
has proved limiting.

## <a name="database"></a>Database

The database consists of one table at this time. Once I gain a better understanding
of this project it can be redone and migrated. As it stand, the one table has six columns:
last_name, middle_name, first_name, gender, degree_earned, university_attended. 

In the future, data can be broken out into three tables: name and email, gender, degree_earned and
university_attended.

All data - the name and email info fed from the csv file and the discovered
gender and educational data - is encrypted using postgres pgcrypto extension and salted with blowfish algorithm.

Reason for this choice is that it is sensitive data for blind auditions, and pgcrypto
is highly reliable scalable solution alreday build into postgres.

## <a name="pie chart"></a>Pie Chart


## <a name="requirements"></a>Requirements

