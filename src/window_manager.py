from tkinter import *
import json

def load_data():
    try:
        with open("data.json") as json_file:
            data = json.load(json_file)
            return data
    except:
        return {}

def createWindow():
    root = Tk()
    root.geometry("500x500")
    # Création de la PanedWindow
    pw = PanedWindow(root, orient=HORIZONTAL)
    pw.pack(fill=BOTH, expand=1)

    # Création de deux frames
    list_frame = Frame(pw, width=100, height=200, background="white")
    pw.add(list_frame)
    pw.add(Frame(pw, width=400, height=200, background="white"))

    # Création d'une Listbox pour afficher les éléments de la liste
    listbox = Listbox(list_frame)
    listbox.pack(side=LEFT, fill=BOTH, expand=1)

    # Ajout des éléments à la liste
    for code in data.keys():
        listbox.insert(END, code)

    # Création d'une Scrollbar pour la Listbox
    scrollbar = Scrollbar(list_frame, orient=VERTICAL, command=listbox.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox.config(yscrollcommand=scrollbar.set)
    
    # On lie l'événement à la Listbox
    listbox.bind('<<ListboxSelect>>', on_select)

    #root.protocol("WM_DELETE_WINDOW", on_close)
    root.iconbitmap("icon.ico")
    root.mainloop()
    
    #root.update()   

data=load_data()

