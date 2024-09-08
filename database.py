# library needed for database
import sqlite3

# creates a connection to the database
def create_database():
    conn = None
    try:
        conn = sqlite3.connect("farmsave.db")
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

# sets up and creates the tables for the database if they have not yet been created
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
            
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

# creates 3 empty saves slots
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

# prints out the contents of the table for developing reasons
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

# creates a new save by inserting the values inputted into the table
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

# checks against the database to see if there is an existing save with the username, returning a boolean value
def checkUsername(name):
    sql = """ SELECT USERNAME
                FROM save
                WHERE SAVE_ID = ? """
    valid = True

    try:
        with sqlite3.connect('farmsave.db') as conn:
            cur = conn.cursor()

            # repeats 3 times for each save
            for x in range(1,4):
                cur.execute(sql, (x,))
                username = cur.fetchone()
                conn.commit()

                # checks to see if the username selected is the same as the one passed in the argument
                if username[0] == name:
                    valid = False

    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    
    return valid

# checks to see if the password inputted by the user matches up with the password stored in the database in the save
def checkPassword(choice, passwordHash):
    sql = """ SELECT PASSWORD_HASH
                FROM save
                WHERE SAVE_ID = ? """
    match = False

    try:
        with sqlite3.connect('farmsave.db') as conn:
            cur = conn.cursor()
            cur.execute(sql, (choice,))
            passHash = cur.fetchone()
            conn.commit()
            if passHash[0] == passwordHash:
                match = True
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

    return match

# gets all the usernames stored in the 3 saves and returns it in a form of a list
def getUsernames():
    sql = """ SELECT USERNAME
                FROM save
                WHERE SAVE_ID = ? """
    names = []

    try:
        with sqlite3.connect('farmsave.db') as conn:
            cur = conn.cursor()

            # repeats 3 times for each save
            for x in range(1,4):
                cur.execute(sql, (x,))

                # gets each name
                username = cur.fetchone()

                # adds the username to a list call names
                names.append(username)
                conn.commit()
                
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    
    return names

# this is called at the start of program which calls all the relavent functions that starts up the database
def startupDatabase():
    create_database()
    create_tables()
    initialise_empty_saves()
    