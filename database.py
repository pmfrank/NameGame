# dict_factory function found at: https://stackoverflow.com/questions/3300464/how-can-i-get-dict-from-sqlite-query
# Originally posted by Alex Martelli on Stack Overflow
# Function is used to covert sqlite3 queary results into a list of dictionaries

import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_database(db, table):

    with sqlite3.connect(db) as conn:
        conn.row_factory = dict_factory
        c = conn.cursor()
        c.execute(f'SELECT rowid, name, gender, relation, image FROM {table}')
        return c.fetchall()