import sqlite3
import os

DATABASE = os.path.join(os.getenv('HOME'), '.tasks.db')

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def query_db(query, args=(), one=False):
    db = sqlite3.connect(DATABASE)
    db.row_factory = make_dicts
    cur = db.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    db.close()
    return (rv[0] if rv else None) if one else rv

def modify_db(query, args=(), one=False):
    db = sqlite3.connect(DATABASE)
    db.row_factory = make_dicts
    cur = db.execute(query, args)
    db.commit()
    rv = cur.fetchall()
    cur.close()
    db.close()
    return (rv[0] if rv else None) if one else rv

def create_database_if_not_present():
    if False == os.path.exists(DATABASE):
        db = sqlite3.connect(DATABASE)
        # all times are in minutes
        columns = "id integer primary key autoincrement, description text, " \
            + "ci_level real, range_min integer, range_max integer, " \
            + "started timestring, ended timestring"
        cur = db.execute("CREATE TABLE tasks (%s)" % columns)
        db.commit()
        cur.close()
        db.close()
