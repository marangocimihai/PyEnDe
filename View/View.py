#!/usr/bin/python
# -*- coding: utf-8 -*-
import Tkinter
import ttk
from Tkinter import *
from ttk import *
import Database.Db as DB
import Controller.Controller as C

# Ai putea incerca sa faci toate functiile ca fiind functii imbricate constructorului, si sa incerci sa accesezi astfel unii membri.
# Cam toate widgeturile ar trebui declarate in constructor, si dupa prelucrate in functiile imbricate aferente, pentru a reusi. :)

class UI(Frame):
    # frame = Tkinter.Tk()
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        # self.grid_columnconfigure(0, weight=10)
        # self.grid_rowconfigure(0, weight=10)
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1)
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)
        # self.entities_list_content = Listbox()
        entities_names_frame = Frame()
        entities_names = Listbox(entities_names_frame)
        self.grid()

        def init_UI(self):
              # self.parent.title("Buttons")
    #        self.style = Style()
    #        self.style.theme_use("default")
    #        self.frame.grid()
            self.parent.title("PyEnDe")
            entities_list()
            # self.separator()
            # UI.add(self)
            add_and_remove()
            # UI.encrypt_button(self)
            # UI.decrypt_button(self)
            encrypt_and_decrypt()
            details()
            save_button()
            # self.grid()
            # for x in range(10):
            #     Grid.columnconfigure(self, x, weight=1)
            # for y in range(5):
            #     Grid.rowconfigure(self, y, weight=1)

        def entities_list():
            # entities_names_frame = Frame()
            # entities_names = Listbox(entities_names_frame)
            entities_names.pack(side=LEFT, fill=Y, expand=True)
            # entities_names.config(highlightbackground="blue")
            scrollbar = Tkinter.Scrollbar(entities_names_frame, orient="vertical")
            scrollbar.pack(side=LEFT, fill=Y)
            entities = DB.Database.retrieve_database_entities()
            for item in entities:
                print item
                entities_names.insert(END, item)
            entities_names.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=entities_names.yview)
            entities_names_frame.grid(row=0, column=0, padx=25, pady=25, sticky=N+S)
            # entities_names_frame.columnconfigure(0, weight=1)
            # entities_names.pack()
            # UI.entities_content = entities_names

        def add(frame):
            # add_frame = Frame()
            add_button = Button(frame, text="Add", command=lambda:C.Controller.add(entities_names))
            add_button.grid(row=0, column=0)
            # add_frame.grid(row=1, column=0)
            return add_button

        def remove(frame):
            def remove_entity():
                if DB.Database.remove_entity(entities_names.get(ACTIVE)) == True:
                    entities_names.delete(entities_names.curselection())
                else:
                    print "FAILURE!"
            remove_button = Button(frame, text="Remove", command=remove_entity)
            remove_button.grid(row=0, column=1)
            # UI.entities_content.get
            return remove_button

        def add_and_remove():
            add_and_remove_frame = Frame()
            add(add_and_remove_frame)
            remove(add_and_remove_frame)
            add_and_remove_frame.grid(row=1, column=0, ipady=10)

        def encrypt_button(frame):
            # encrypt_frame = Frame()
            encrypt_button = Button(frame, text="Encrypt")
            encrypt_button.grid(row=0, column=0)
            # encrypt_frame.grid(row=1, column=1)
            return encrypt_button

        def decrypt_button(frame):
            # decrypt_frame = Frame()
            decrypt_button = Button(frame, text="Decrypt")
            decrypt_button.grid(row=0, column=1)
            # decrypt_frame.grid(row=1, column=2)
            return decrypt_button

        def encrypt_and_decrypt():
            encrypt_and_decrypt_frame = Frame()
            encrypt_button(encrypt_and_decrypt_frame)
            decrypt_button(encrypt_and_decrypt_frame)
            encrypt_and_decrypt_frame.grid(row=1, column=1, ipady=10)

        def save_button():
            save_frame = Frame()
            save_button = Button(save_frame, text="Save")
            save_button.grid(row=0, column=1)
            # decrypt_frame.grid(row=1, column=2)
            save_frame.grid(row=0, column=3, ipadx=10, pady= 25, sticky=N)

        def details():
            details_frame = Frame()
            entity_info = Text(details_frame, height=10, width=50)
            # entity_info.bind("<Key>", self.update_size)
            entity_info.columnconfigure(0, weight=1)
            entity_info.rowconfigure(0, weight=1)
            entity_info.pack(fill='both', expand=True)
            details_frame.grid(row=0, column=1, sticky=N+S+E+W, padx=25, pady=25)

            # details_frame.update()
            # entity_info.config(width=details_frame.winfo_width(), height=details_frame.winfo_height())

        def separator(self):
            ttk.Separator(self).grid(column=5)

        init_UI(self)

def main():
    root = Tk()
    # root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(1, weight=0)
    root.geometry("700x400")
    app = UI(root)
    # app.grid(sticky=N+S+E+W)
    # app.grid_columnconfigure(5, weight=10)
    # app.grid_rowconfigure(5, weight=10)
    root.mainloop()

if __name__ == '__main__':
    main()