"""Module that manages the main application window"""
import json
from tkinter import (
    Scrollbar,
    Tk,
    messagebox,
    StringVar,
    Entry,
    Button,
    Label,
    PanedWindow,
    HORIZONTAL,
    BOTH,
    BOTTOM,
    Frame,
    LEFT,
    RIGHT,
    Y,
    VERTICAL,
    END,
    Listbox,
)
from src import listener


from src import utils

data = utils.load_data()


def create_window():
    """Create the main window"""
    root = Tk()
    # on supprime la fenêtre précédente si elle n'est pas la fenêtre de lancement
    if is_window_open(root):
        root.destroy()

    root.geometry("500x500")
    # Création de la PanedWindow
    paned_window = PanedWindow(root, orient=HORIZONTAL)
    paned_window.pack(fill=BOTH, expand=1)

    create_list_box(paned_window, root)

    # root.protocol("WM_DELETE_WINDOW", lambda: on_close(root))
    root.iconbitmap("icon.ico")
    root.mainloop()


def on_select(event):
    """Function called when an element is selected in the listbox"""
    # On récupère l'index de l'élément sélectionné
    index = event.widget.curselection()[0]
    # On récupère l'élément sélectionné
    key = event.widget.get(index)

    # On récupère la frame de droite
    frame = event.widget.master.master.master.children["!panedwindow"].children[
        "!frame2"
    ]

    # On supprime le contenu de la frame de droite
    for widget in frame.winfo_children():
        widget.destroy()

    # On ajoute le contenu de l'élément sélectionné

    value = StringVar()
    value.set(data[key])
    input_value = Entry(frame, textvariable=value, width=50)
    input_value.pack()

    Button(
        frame,
        text="Valider l'edition",
        command=lambda: on_update(input_value.get(), key),
    ).pack()


def on_update(value, key):
    """Update the value of the selected element"""
    # On met à jour la valeur de l'élément sélectionné
    data[key] = value
    # On sauvegarde la nouvelle valeur dans le fichier
    with open("data.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file)


def on_add(event):
    """Function called when the add button is clicked"""
    # On récupère la frame de droite
    frame = event.widget.master.master.children["!panedwindow"].children["!frame2"]

    # On supprime le contenu de la frame de droite
    for widget in frame.winfo_children():
        widget.destroy()

    # On ajoute le contenu de l'élément sélectionné
    Label(frame, text="snippet").pack()
    snippet = StringVar()
    snippet_input = Entry(frame, textvariable=snippet, width=50)
    snippet_input.pack()
    Label(frame, text="valeur").pack()
    value = StringVar()
    value_input = Entry(frame, textvariable=value, width=50)
    value_input.pack()

    Button(
        frame,
        text="Valider l'ajout",
        command=lambda: on_add_validate(snippet.get(), value.get()),
    ).pack()


def on_add_validate(snippet, value):
    """Add a snippet and its value to the data.json file"""
    try:
        if snippet == value:
            messagebox.showerror(
                "Erreur", "Le snippet et la valeur ne peuvent pas être identiques"
            )
        else:
            # On met à jour la valeur de l'élément sélectionné
            data[snippet] = value
            # On sauvegarde la nouvelle valeur dans le fichier
            with open("data.json", "w", encoding="utf-8") as json_file:
                json.dump(data, json_file)
            # On crée une nouvelle fenêtre pour mettre à jour la liste et on supprime l'ancienne
            # create_window()
            listener.data = utils.update_data()

    except (ValueError, TypeError):
        messagebox.showerror("Erreur", "Une erreur de type est survenue")


def create_list_box(paned_window, root):
    """Create the list box"""
    # Création de deux frames
    list_frame = Frame(paned_window, width=100, height=200, background="white")
    paned_window.add(list_frame)
    paned_window.add(Frame(paned_window, width=400, height=200, background="white"))

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
    listbox.bind("<<ListboxSelect>>", on_select)

    # Création d'une frame pour le bouton
    button_frame = Frame(root)
    button_frame.pack(side=BOTTOM, pady=10)

    # Création du bouton
    button = Button(button_frame, text="Ajouter")
    button.pack()
    button.bind("<Button-1>", on_add)


def is_window_open(root):
    """Check if the window is already open"""
    return len(root.children) > 0
