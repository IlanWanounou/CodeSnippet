from tkinter import *
import json
from tkinter import messagebox
from src import utils

def createWindow():
    root = Tk()
    root.geometry("500x500")
    # Création de la PanedWindow
    pw = PanedWindow(root, orient=HORIZONTAL)
    pw.pack(fill=BOTH, expand=1)

    create_list_box(pw, root)

    # Création d'une Listbox pour afficher les éléments de la liste
    root.iconbitmap("icon.ico")
    root.mainloop()

def on_select(event):
    # On récupère l'index de l'élément sélectionné
    index = event.widget.curselection()[0]
    # On récupère l'élément sélectionné
    key = event.widget.get(index)

    # On récupère la frame de droite
    frame = event.widget.master.master.master.children["!panedwindow"].children["!frame2"]

    # On supprime le contenu de la frame de droite
    for widget in frame.winfo_children():
        widget.destroy()
    

    # On ajoute le contenu de l'élément sélectionné

    inputText = StringVar()
    inputText.set(data[key])
    input = Entry(frame, textvariable=inputText, width=50)
    input.pack()


    Button(frame, text="Valider l'edition").pack()

def on_update(inputText, key):
    # On met à jour la valeur de l'élément sélectionné
    data[key] = inputText
    # On sauvegarde la nouvelle valeur dans le fichier
    with open("data.json", "w") as json_file:
        json.dump(data, json_file)

def on_add(event):
    # On récupère la frame de droite
    frame = event.widget.master.master.children["!panedwindow"].children["!frame2"]

    # On supprime le contenu de la frame de droite
    for widget in frame.winfo_children():
        widget.destroy()
    
    # On ajoute le contenu de l'élément sélectionné
    Label(frame, text="snippet").pack()
    snippet = StringVar()
    input = Entry(frame, textvariable=snippet, width=50)
    input.pack()
    
    Label(frame, text="valeur").pack()
    value = StringVar()
    input = Entry(frame, textvariable=value, width=50)
    input.pack()

    Button(frame, text="Valider l'ajout", command= lambda:on_add_validate(snippet.get(), value.get())).pack()

def on_add_validate(snippet, value):
    try:
        if(snippet == value):
            messagebox.showerror("Erreur", "Le snippet et la valeur ne peuvent pas être identiques")
        else:
            # On met à jour la valeur de l'élément sélectionné
            data[snippet] = value
            # On sauvegarde la nouvelle valeur dans le fichier
            with open("data.json", "w") as json_file:
                json.dump(data, json_file)
                json_file.close()
            
            data=utils.load_data()
                
    except:
        messagebox.showerror("Erreur", "Une erreur est survenue")

def create_list_box(pw, root):
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
    
    # Création d'une frame pour le bouton
    button_frame = Frame(root)
    button_frame.pack(side=BOTTOM, pady=10)
    
    # Création du bouton
    button = Button(button_frame, text="Ajouter")
    button.pack()
    button.bind("<Button-1>", on_add)
    
data=utils.load_data()

