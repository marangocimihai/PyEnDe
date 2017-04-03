import sqlite3
import Entity

class Database:
    @staticmethod
    def connect_to_database():
        conn = sqlite3.connect('C:\Users\marangocimihai\Desktop\db.db')
        return conn

    @staticmethod
    def get_entity_ID(name):
        conn = Database.connect_to_database()
        c = conn.cursor()
        print name
        c.execute("SELECT ID FROM ENTITY WHERE NAME LIKE (?)", (name)) # Aici e ceva eroare cu binding, etc. ... vezi tu maine
        conn.commit()
        return c.fetchone()

    @staticmethod
    def retrieve_database_entities():
        conn = Database.connect_to_database()
        c = conn.cursor()
        c.execute('SELECT NAME FROM ENTITY')
        return c.fetchall()

    @staticmethod
    def add_entity(title, content):
        title = title[:-1]
        content = content[:-1]
        print title + " aici "
        print content + " aici "
        conn = Database.connect_to_database()
        c = conn.cursor()
        c.execute("INSERT INTO ENTITY(NAME, CONTENT) VALUES(?, ?)", (title, content))
        conn.commit()
        return True if c.rowcount > 0 else False
        # frame.destroy()

    @staticmethod
    def get_details():
        conn = Database.connect_to_database()
        c = conn.cursor()
        c.execute("SELECT * FROM ENTITY")
        conn.commit()

    @staticmethod
    def remove_entity(name):
        ID = Database.get_entity_ID(name)
        conn = Database.connect_to_database()
        c = conn.cursor()
        c.execute("DELETE FROM ENTITY WHERE ID = ?", (ID))
        conn.commit()
        return True if c.rowcount > 0 else False