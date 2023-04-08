import keyboard
import json
import time
from plyer import notification
from tkinter import *


def loadData():
    try:
        with open("data.json") as json_file:
            data = json.load(json_file)
            return data
    except:
        return {}


def checkCode(code):
    global str
    if code in data.values():
        str = ""
        notification.notify(title="Code correct", message="Code correct", timeout=5)
    else:
        if len(code) > 4:
            notification.notify(
                title="Code incorrect", message="Code incorrect", timeout=5
            )


def on_key_press(key):
    global str
    str += key.name
    checkCode(str)


def createWindow():
    global root
    root.geometry("500x500")
    # Création de la PanedWindow
    pw = PanedWindow(root, orient=HORIZONTAL)
    pw.pack(fill=BOTH, expand=1)

    # Création de deux frames
    list_frame = Frame(pw, width=100, height=200, background="white")
    pw.add(list_frame)
    pw.add(Label(pw, text="", background="white"))

    # Création d'une Listbox pour afficher les éléments de la liste
    listbox = Listbox(list_frame)
    listbox.pack(side=LEFT, fill=BOTH, expand=1)

    # Ajout des éléments à la liste
    for code in data.keys():
        listbox.insert(END, code)


    #root.protocol("WM_DELETE_WINDOW", on_close)
    root.iconbitmap("icon.ico")
    root.mainloop()

root = Tk()
data = loadData()
str = ""
keyboard.on_press(on_key_press)
createWindow()


""" while True:
    time.sleep(1) """


""" data = codeSpinner()

def seralizeData(data):
    json_object = json.dumps(data, indent = 4)
    with open("data.json", "w") as outfile:
        outfile.write(json_object) """
