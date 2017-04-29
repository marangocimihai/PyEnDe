#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkMessageBox
import tkSimpleDialog
from Tkinter import *

import GUI
from Driver import Constants as Constants


def password():
    temp_window = Tk()
    temp_window.withdraw()
    center(temp_window)
    temp_window.update()
    input_password = tkSimpleDialog.askstring('Password',
                                              'Type password: ',
                                               parent=temp_window, show='*')
    if input_password == Constants.PASSWORD:
        temp_window.destroy()
        return Constants.CORRECT_PASSWORD
    elif input_password != None and input_password != Constants.PASSWORD:
        return Constants.INCORRECT_PASSWORD
    elif input_password == None:
        return Constants.NONE_PASSWORD

def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

def main():
    root = Tk()
    # root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(1, weight=0)
    root.geometry("700x400")
    root.protocol("WM_DELETE_WINDOW", lambda:GUI.UI.on_closing(root))
    app = GUI.UI(root)
    # app.grid(sticky=N+S+E+W)
    # app.grid_columnconfigure(5, weight=10)
    # app.grid_rowconfigure(5, weight=10)
    center(root)
    root.mainloop()

if __name__ == '__main__':
    while True:
        input_password = password()
        if input_password == Constants.CORRECT_PASSWORD:
            main()
            break
        elif input_password == Constants.INCORRECT_PASSWORD:
            tkMessageBox.showerror("Invalid password", "The typed password does not match.")
        elif input_password == Constants.NONE_PASSWORD:
            break