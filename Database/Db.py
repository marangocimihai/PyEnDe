import sqlite3
import Entity
import os
import Aes.Anonymize as Aes
import Constants.Constants as Constants

class Database:
    @staticmethod
    def create_database_file():
        current_directory = os.getcwd()
        path = current_directory + Constants.DATABASE_FILE_NAME
        print "Path: " + path
        if not os.path.exists(path):
            open(path, "w+")

    @staticmethod
    def create_database_tables():
        conn = sqlite3.connect('C:\Users\marangocimihai\PycharmProjects\PyEnDe\View\passwords.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS ENTITY(ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, NAME TEXT NOT NULL UNIQUE, CONTENT TEXT NOT NULL, ENCRYPTED INTEGER NOT NULL);''')
        conn.commit()
        return

    @staticmethod
    def connect_to_database():
        conn = sqlite3.connect('C:\Users\marangocimihai\Desktop\db.db')
        return conn

    @staticmethod
    def get_entity_ID(name):
        name = "".join(str(x) for x in name)
        # print "Type in Db: " + str(type(name))
        # print "Name in Db: " + str(name)
        conn = Database.connect_to_database()
        c = conn.cursor()
        # print name
        c.execute("SELECT ID FROM ENTITY WHERE NAME LIKE ?", (name,)) # Aici e ceva eroare cu binding care survine doar cand adaugi o noua entitate si selectezi o alta, etc. ... vezi tu maine
        conn.commit()
        return c.fetchone()[0]

    @staticmethod
    def get_entities():
        conn = Database.connect_to_database()
        c = conn.cursor()
        c.execute('SELECT NAME FROM ENTITY')
        return c.fetchall()

    @staticmethod
    def get_entity_content(name):
        # print "Name in getdetails: " + str(name)
        # print "Name type in getdetails: " + str(type(name))
        ID = Database.get_entity_ID(name)
        # print "Dupa ce am apelat luarea ID-ului din get_entity_details"
        # print "Inainte: " + str(ID)
        # ID = "".join(str(x) for x in ID)
        # print "Dupa : " + str(ID)
        conn = Database.connect_to_database()
        c = conn.cursor()
        c.execute("SELECT CONTENT FROM ENTITY WHERE ID = ?", (ID,))
        conn.commit()
        # print c.fetchone()
        return c.fetchone()[0]

    @staticmethod
    def add_entity(entity):
        entity.name = entity.name[:-1]
        entity.content = entity.content[:-1]
        # print entity.name + " ************************ "
        # print entity.content + " ************************ "
        conn = Database.connect_to_database()
        c = conn.cursor()
        c.execute("INSERT INTO ENTITY(NAME, CONTENT, ENCRYPTED) VALUES(?, ?, ?)", (entity.name, entity.content, entity.is_encrypted))
        conn.commit()
        return True if c.rowcount > 0 else False
        # frame.destroy()

    @staticmethod
    def remove_entity(name):
        ID = Database.get_entity_ID(name)
        conn = Database.connect_to_database()
        c = conn.cursor()
        c.execute("DELETE FROM ENTITY WHERE ID = ?", (ID,))
        conn.commit()
        return True if c.rowcount > 0 else False

    @staticmethod
    def set_new_content(entity):
        # entity.name = entity.name[:-1]
        # entity.content = entity.content[:-1]
        ID = Database.get_entity_ID(entity.name)
        # print type((ID))
        print entity.content
        conn = Database.connect_to_database()
        c = conn.cursor()
        # int_id = int(ID)
        c.execute("UPDATE ENTITY SET CONTENT = ? WHERE ID = ?", (entity.content, ID))
        conn.commit()
        return True if c.rowcount > 0 else False

    @staticmethod
    def encrypt_content(entity):
        entity.is_encrypted = Constants.ENCRYPTED_CONTENT
        ID = Database.get_entity_ID(entity.name)
        conn = Database.connect_to_database()
        c = conn.cursor()
        print "Content din Db: " + entity.content
        entity.content = Aes.Anonymize.encrypt(entity.content)
        c.execute("UPDATE ENTITY SET CONTENT = ? WHERE ID = ?", (entity.content, ID))
        # c.execute("UPDATE ENTITY SET ENCRYPTED = 1 WHERE ID = ?", (ID[0]))
        conn.commit()
        return True if c.rowcount > 0 else False

    @staticmethod
    def decrypt_content(entity):
        entity.is_encrypted = Constants.DECRYPTED_CONTENT
        ID = Database.get_entity_ID(entity.name)
        conn = Database.connect_to_database()
        c = conn.cursor()
        entity.content = Aes.Anonymize.decrypt(entity.content)
        # entity.content = entity.content[:-1]
        c.execute("UPDATE ENTITY SET CONTENT = ? WHERE ID = ?", (entity.content, ID))
        # Database.is_encrypted(Constants.DECRYPTED_CONTENT)
        # c.execute("UPDATE ENTITY SET ENCRYPTED = 0 WHERE ID = ?", ID[0])
        conn.commit()
        return True if c.rowcount > 0 else False

    @staticmethod
    def is_encrypted(entity, option):
        ID = Database.get_entity_ID(entity.name)
        conn = Database.connect_to_database()
        c = conn.cursor()
        c.execute("UPDATE ENTITY SET ENCRYPTED = ? WHERE ID = ?", (option, ID))
        conn.commit()

    @staticmethod
    def get_is_encrypted(name):
        ID = Database.get_entity_ID(name)
        # print "ID din getul ala: " + str(ID)
        conn = Database.connect_to_database()
        c = conn.cursor()
        c.execute("SELECT ENCRYPTED FROM ENTITY WHERE ID = ?", (ID,))
        conn.commit()
        return c.fetchone()

    @staticmethod
    def get_non_encrypted_entities():
        # ID = Database.get_entity_ID(name)
        # print "ID din getul ala: " + str(ID)
        conn = Database.connect_to_database()
        c = conn.cursor()
        c.execute("SELECT * FROM ENTITY WHERE ENCRYPTED = 0")
        conn.commit()
        # print "from withing db : " + str(c.fetchall())
        return c.fetchall()