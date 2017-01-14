edu_web_scraper

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
* [License](#license)

## <a name="database"></a>Database

The database consists of one table at this time. Once I gain a better understanding
of this project it can be redone and migrated. As it stand, the one table has six columns:
last_name, middle_name, first_name, gender, degree_earned, university_attended. 

In the future, data can be broken out into three tables: name and email, gender, degree_earned and
university_attended.

All data - the name and email info fed from the csv file and the discovered
gender and educational data - is encrypted using postgres pgcrypto extension and blowfish algorithm.

Reason for this choice is that it is sensitive data for blind auditions, and pgcrypto
is highly reliable scalable solution alreday build into postgres.


## <a name="scraping"></a>Scraping



## <a name="license"></a>License

The MIT License (MIT)
Copyright (c) 2016 Anka Kondraska 

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.