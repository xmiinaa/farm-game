import sqlite3

def create_database():
    """ create a database connection to an SQLite database """
    conn = None
    try:
        conn = sqlite3.connect("farmsave.db")
        print(conn)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

import sqlite3

def create_tables():
    sql_statements = [ 
        """CREATE TABLE IF NOT EXISTS save (
                SAVE_ID INTEGER PRIMARY KEY, 
                USERNAME TEXT, 
                PASSWORD_HASH TEXT
        );"""]

    # create a database connection
    try:
        with sqlite3.connect('farmsave.db') as conn:
            cursor = conn.cursor()
            for statement in sql_statements:
                cursor.execute(statement)
            
            conn.commit()
            print("save table made")
            
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def initialise_empty_saves():
    sql = """ INSERT INTO save (USERNAME, PASSWORD_HASH)
                VALUES (?, ?) """
    emptySave = ("NULL", "NULL")
    try:
        with sqlite3.connect('farmsave.db') as conn:
            for x in range(3):
                cur = conn.cursor()
                cur.execute(sql, emptySave)
                conn.commit()
                SAVE_ID =  cur.lastrowid
                print(f"created a project with the id {SAVE_ID}")
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def view_table():
    sql = """ SELECT * FROM save"""
    try:
        with sqlite3.connect('farmsave.db') as conn:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def create_newsave(username, passwordHash, saveChoice):
    sql = """ UPDATE save
                SET USERNAME = ?, PASSWORD_HASH = ?
                WHERE id = ? """
    data = (username, passwordHash, saveChoice)

    try:
        with sqlite3.connect('farmsave.db') as conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    create_database()
    create_tables()
    initialise_empty_saves()
    view_table()