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
        # print name
        c.execute("SELECT ID FROM ENTITY WHERE NAME LIKE (?)", (name)) # Aici e ceva eroare cu binding care survine doar cand adaugi o noua entitate si selectezi o alta, etc. ... vezi tu maine
        conn.commit()
        return c.fetchone()

    @staticmethod
    def get_entities():
        conn = Database.connect_to_database()
        c = conn.cursor()
        c.execute('SELECT NAME FROM ENTITY')
        return c.fetchall()

    @staticmethod
    def get_entity_details(name):
        ID = Database.get_entity_ID(name)
        conn = Database.connect_to_database()
        c = conn.cursor()
        c.execute("SELECT CONTENT FROM ENTITY WHERE ID = ?", (ID))
        conn.commit()
        # print c.fetchone()
        return c.fetchone()

    @staticmethod
    def add_entity(name, content):
        name = name[:-1]
        content = content[:-1]
        # print title + " aici "
        # print content + " aici "
        conn = Database.connect_to_database()
        c = conn.cursor()
        c.execute("INSERT INTO ENTITY(NAME, CONTENT) VALUES(?, ?)", (name, content))
        conn.commit()
        return True if c.rowcount > 0 else False
        # frame.destroy()

    @staticmethod
    def remove_entity(name):
        ID = Database.get_entity_ID(name)
        conn = Database.connect_to_database()
        c = conn.cursor()
        c.execute("DELETE FROM ENTITY WHERE ID = ?", (ID))
        conn.commit()
        return True if c.rowcount > 0 else False

    @staticmethod
    def set_new_content(entity):
        ID = Database.get_entity_ID(entity.name)
        print type((ID))
        print entity.content
        conn = Database.connect_to_database()
        c = conn.cursor()
        # int_id = int(ID)
        c.execute("UPDATE ENTITY SET CONTENT = ? WHERE ID = ?", (entity.content, ID[0])) # some error in here as well
        conn.commit()
        return True if c.rowcount > 0 else False