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
                PASSWORD_HASH TEXT, 
                NPC_REL INTEGER,
                PLAYER_ID INTEGER,
                PET_OWNED_ID INTEGER,
                ANIMAL_OWNED_ID INTEGER,
                WEATHER_ID INTEGER,
                TILE_ID INTEGER,
                INVENTORY_ID INTEGER
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

def initialise_empty_saves():
    sql = """ INSERT INTO save (USERNAME, PASSWORD_HASH)
                VALUES (?, ?) """
    try:
        with sqlite3.connect('farmsave.db') as conn:
            for x in range(3):
                cur = conn.cursor()
                cur.execute(sql, "NULL, NULL")
                conn.commit()
                SAVE_ID =  cur.lastrowid
                print(f"created a project with the id {SAVE_ID}")
    except sqlite3.Error as e:
            print(e)



def main():
    try:
        with sqlite3.connect('farmsave.db') as conn:
            save = ("Amina", "Password1")
            SAVE_ID = initialise_empty_saves(conn, save)
            print(f"created a project with the id {SAVE_ID}")
    except sqlite3.Error as e:
        print(e)

if __name__ == "__main__":
    create_database()
    create_tables()
    initialise_empty_saves()