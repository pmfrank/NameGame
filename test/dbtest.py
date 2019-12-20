# dict_factory function found at: https://stackoverflow.com/questions/3300464/how-can-i-get-dict-from-sqlite-query
# Originally posted by Alex Martelli on Stack Overflow
# Function is used to covert sqlite3 queary results into a list of dictionaries

import sqlite3
from speech import speak
from random import randrange

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

with sqlite3.connect('family.db') as conn:
    c = conn.cursor()

    c.execute(''' SELECT count(name) FROM sqlite_master where type='table' and name='family_info' ''')

    if c.fetchone()[0] != 1:
        print('Table not found')

        # Create table
        c.execute(''' CREATE TABLE family_info
                        (name TEXT NOT NULL,
                        gender TEXT NOT NULL,
                        relation TEXT NOT NULL,
                        image TEXT NOT NULL) ''')

 #with sqlite3.connect('family.db') as conn:
 #     c = conn.cursor()
 #     c.execute(''' INSERT INTO family_info VALUES('Amanda','girl','mom','image.jpg') ''')
picked = list()

for x in range(0, 16):
    with sqlite3.connect('family.db') as conn:
        conn.row_factory = dict_factory
        c = conn.cursor()
        rowid = randrange(16)+1
        while rowid in picked:
            rowid = randrange(16) + 1
        picked.append(rowid)
        print(rowid)
        c.execute(f'SELECT * FROM family_info WHERE rowid = {rowid}')
        fam_mem = c.fetchall()[0]

    if fam_mem["gender"] == 'girl':
        pronoun = 'she'
    else:
        pronoun = 'he'

    text = f'I met your {fam_mem["relation"]}, {pronoun} is a {fam_mem["gender"]} named {fam_mem["name"]}.'

    print(text)
    # speak(f'Loop {x}')
    speak(text)