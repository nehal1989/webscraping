import sqlite3

def initialiase_database(database_name='sysk'):
    db = sqlite3.connect(f'/Users/Nehal/Programming/python_projects/webscraping/{database_name}.db')

    cursor = db.cursor()

    try:
        cursor.execute("""CREATE TABLE podcastInfo (
                        id INTEGER PRIMARY KEY,
                        title text,
                        date text
        )""")
    except sqlite3.OperationalError:
        print(f'Looks like the table already exist, no worries, carrying on')

    db.commit()  # comitting changes to the DB
    db.close()

def add_data(podcast_data):
    db = sqlite3.connect(f'/Users/Nehal/Programming/python_projects/webscraping/sysk.db')
    cursor = db.cursor()

    try:
        cursor.executemany(''' INSERT INTO podcastInfo(title, date) VALUES(?,?)''', podcast_data)

    except sqlite3.OperationalError:
        print(f'Looks like the table already exist, no worries, carrying on')

    db.commit()  # comitting changes to the DB
    db.close()




initialiase_database()