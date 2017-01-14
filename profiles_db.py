import psycopg2

# access db
con = psycopg2.connect(dbname='vagrant')
# specify db encoding
con.set_client_encoding('UTF-8') 
cur = con.cursor()
# create pgcrypto extension - just once when accessing db the first time
# cur.execute("CREATE EXTENSION pgcrypto")
cur.execute("DROP TABLE IF EXISTS profiles")
cur.execute("CREATE TABLE profiles(Id Serial PRIMARY KEY, f_name VARCHAR(300),\
             m_name VARCHAR(300), l_name VARCHAR(300),gender VARCHAR(300),\
             degree_earned VARCHAR(300),university_attended VARCHAR(300)) ")
con.commit()


def add_to_db(first_name, last_name, degree, university):
    """Add encrypted data to db"""

    cur.execute("INSERT INTO profiles (f_name, l_name, degree_earned," +
                "university_attended) VALUES (crypt(%s, gen_salt('bf',8)),\
                crypt(%s, gen_salt('bf',8)),crypt(%s, gen_salt('bf',8)),\
                crypt(%s, gen_salt('bf',8)))",
                (first_name, last_name, degree, university))
    con.commit()
