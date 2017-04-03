#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter
import ttk
from Tkinter import *
from ttk import *
import Database.Db as DB
from Database.Entity import *

class Controller():
    @staticmethod
    def add(entities_names):
        frame = Frame()
        window = Tkinter.Toplevel(frame)
        window.geometry("600x300")
        name = Label(window, text="Name")
        details = Label(window, text="Details")
        name_content = Text(window, height=1, width=30)
        details_content = Text(window, height=10, width=30)

        # entity = Entity(name_content.get(0.0, END), details_content.get(0.0, END))

        confirm_cancel_frame = Frame(window)
        confirm = Button(confirm_cancel_frame, text="Confirm", command= lambda : add_entity_and_close_window(name_content.get(1.0, END), details_content.get(1.0, END)))
        cancel = Button(confirm_cancel_frame, text="Cancel", command=frame.destroy)
        confirm.grid(row=0, column=0)
        cancel.grid(row=0, column=1)

        name.grid(row=0, column=0, padx=25, pady=25, sticky=N)
        name_content.grid(row=0, column=1, padx=(0, 25), sticky=W+E)
        details.grid(row=1, column=0, sticky=N)
        details_content.grid(row=1, column=1, padx=(0, 25), pady=(0, 25), sticky=N+S+E+W)
        confirm_cancel_frame.grid(row=2, column=1)

        window.columnconfigure(1, weight=1)
        window.rowconfigure(1, weight=1)
        window.transient(frame)
        window.grab_set()
        # frame.grid()
        def add_entity_and_close_window(name_content, details_content):
            frame.destroy()
            if DB.Database.add_entity(name_content, details_content) == True:
                entities_names.insert(entities_names.size(), name_content)
            else:
                print "FAILURE!"
