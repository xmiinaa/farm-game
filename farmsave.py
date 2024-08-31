import pygame, sqlite3

def create_database(filename):
    """ create a database connection to an SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(filename)
        print(sqlite3.sqlite_version)
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
                USERNAME TEXT NOT NULL, 
                PASSWORD_HASH TEXT NOT NULL, 
                NPC_REL INTEGER
                PLAYER_ID INTEGER
                PET_OWNED_ID INTEGER
                ANIMAL_OWNED_ID INTEGER
                WEATHER_ID INTEGER
                TILE_ID INTEGER
                INVENTORY_ID INTEGER
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

def new_save(conn, save):
    sql = """ INSERT INTO save (USERNAME, PASSWORD_HASH)
                VALUES (?, ?) """
    cur = conn.cursor()
    cur.execute(sql, save)
    conn.commit()
    return cur.lastrowid

def main():
    try:
        with sqlite3.connect('farmsave.db') as conn:
            save = ("Amina", "Password1")
            SAVE_ID = new_save(conn, save)
            print(f"created a project with the id {SAVE_ID}")
    except sqlite3.Error as e:
        print(e)

if __name__ == "__main__":
    create_database("farmsave.db")
    create_tables()
    main()