import json
import threading
from pynput import keyboard

def load_data():
    try:
        with open("data.json") as json_file:
            data = json.load(json_file)
            return data
    except:
        return {}
    
def check_code():
    return on_press.key_sequence in data.keys()

def clear():
    on_press.key_sequence = ""
    return

def on_press(key):
    try:
        on_press.key_sequence += key.char
        if  check_code():
            for i in range(len(on_press.key_sequence)):
                keyboard.Controller().press(keyboard.Key.backspace)
                keyboard.Controller().release(keyboard.Key.backspace)
            keyboard.Controller().type(data[on_press.key_sequence])
            threading.Timer(0.1, clear).start()
            
    except AttributeError:
        pass

data = load_data()
on_press.key_sequence = ""

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
