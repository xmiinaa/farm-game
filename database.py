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
    sql = """ INSERT OR REPLACE INTO save (SAVE_ID, USERNAME, PASSWORD_HASH)
                VALUES (?, ?, ?) """

    try:
        with sqlite3.connect('farmsave.db') as conn:
            cur = conn.cursor()
            cur.execute('SELECT COUNT(*) FROM save')
            count = cur.fetchone()[0]
            if count == 0:
                for x in range(1,4):
                    cur.execute(sql, (x, "NULL", "NULL"))
                    conn.commit()
                    SAVE_ID =  cur.lastrowid
                    print(f"created a project with the id {SAVE_ID}")
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def view_table():
    try:
        with sqlite3.connect('farmsave.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM save;")
            print(cur.fetchall())
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def create_newsave(username, passwordHash, saveChoice):
    sql = """ UPDATE save
                SET USERNAME = ?, PASSWORD_HASH = ?
                WHERE SAVE_ID = ? """
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

def checkUsername(name):
    sql = """ SELECT USERNAME
                FROM save
                WHERE SAVE_ID = ? """
    Found = False

    try:
        with sqlite3.connect('farmsave.db') as conn:
            cur = conn.cursor()
            for x in range(1,4):
                username = cur.execute(sql, (x))
                if str(username) == name:
                    Found = True
                conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    
    return Found

if __name__ == "__main__":
    create_database()
    create_tables()
    initialise_empty_saves()
    view_table()
    print(checkUsername("Amina"))
    #create_newsave("Amina", "7833dc6e82e9378117bcb03128ac8fdd95d9073161ebc963783b3010dd847ff3", 1)
    #create_newsave("Kalam", "8d71292c2d52e804d6e43412655bf3ec8020354446913b30e0813baaf675651e", 2)
    #view_table()