edu_web_scraper

Overview:<br/>
edu_web_scraper scrapes the web, specifically google search results for gender and educational information
based on full name and email address.

It takes a csv file as input with full name and email address columns. It runs google search on each name
and/or email address and scrapes the educational degree and educational institution associated with each name
and/or email adddress. It also scrapes gednerize.io and behindthename.com for gender information
based on first name.

At this point it is a script file. There is no UI to speak of. To run it in your terminal specify 
the script file and test names/emails csv file to be discovered:<br/>
python gapjump.py test_profiles.csv

## Table of Contents📖

* [Tech Stack](#tech-stack)
* [Database](#database)
* [Setup/Installation](#installation)
* [To-Do](#future)
* [License](#license)

## <a name="tech-stack"></a>Tech Stack

__Backend:__ Python, Matplotlib, Mechanize, BeautifulSoup <br/>
__Database:__ Postgres<br/>

## <a name="database"></a>Database

Homepage D3 network graph with user nodes and skill edges

![SwiftSwap Homepage](assets/ss2.png)

Pagerank of the most popular users and Chart.js doughnut visualization

![SwiftSwap Homepage](assets/ss3.png)

User profile page with current and predicted skills

![SwiftSwap Homepage](assets/ss4.png)

User closed path⭕ D3 graph and first degree connections D3 graph

![SwiftSwap Homepage](assets/ss5.png)

User closed path⭕ connections links and user location map

![SwiftSwap Homepage](assets/ss6.png)

## <a name="installation"></a>Setup/Installation

####Requirements:

- PostgreSQL
- Python 2.7
- Google Maps API keys

To have this app running on your local computer, please follow the below steps:

Clone repository:
```
$ git clone https://github.com/skakanka/swiftswap.git
```
Create a virtual environment:
```
$ virtualenv env
```
Activate the virtual environment:
```
$ source env/bin/activate
```
Install dependencies:
```
$ pip install -r requirements.txt
```
Get your own Google Maps API key and save it to a file `secrets.py`.

Create database 'barternet'.
```
$ createdb -E UTF8 -T template0 --locale=en_US.utf8 barternet
```
Create your database tables and seed example data.
```
$ python barter_network/seed.py
```
Run the app from the command line.
```
$ python runserver.py
```
If you want to use SQLAlchemy to query the database, run in interactive mode
```
$ python -i model.py
```

## <a name="future"></a>TODO
* Map users within the shortest distance of each other in the closed path⭕
* User reviews, verification and photos
* Add ability for users to communicate
* Develop system for valuing skills


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