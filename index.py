import json
import threading
import sys
if sys.version_info[0] == 3:
   from tkinter import *
else:
    from Tkinter import *
try:
    from pynput import keyboard
except ImportError as e:
    print("Error: {}".format(e))
    
# workflow
import os
os.environ['DISPLAY'] = ':0'


def loadData():
    try:
        with open("data.json") as json_file:
            data = json.load(json_file)
            return data
    except:
        return {}

def checkCode():
    return on_press.key_sequence in data.keys()

def clear():
    on_press.key_sequence = ""
    return

def on_press(key):
    try:
        on_press.key_sequence += key.char
        if  checkCode():
            for i in range(len(on_press.key_sequence)):
                keyboard.Controller().press(keyboard.Key.backspace)
                keyboard.Controller().release(keyboard.Key.backspace)
            keyboard.Controller().type(data[on_press.key_sequence])
            threading.Timer(0.1, clear).start()
            
    except AttributeError:
        pass

def createWindow():
    global root
    global data
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
    #root.iconbitmap("icon.ico")
    root.title("Code Manager")
    root.mainloop()
    
    #root.update()


root = Tk()
data = loadData()

# Initialiser la séquence de touches stockée en mémoire
#on_press.key_sequence = ""


#t1 = threading.Thread(target=createWindow)
#t2 = threading.Thread(target=keyboard.Listener(on_press=on_press).start)
createWindow()
#t1.start()
#t2.start()
#root.mainloop()
