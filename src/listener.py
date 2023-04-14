import json
import threading
import re
from pynput import keyboard

def load_data():
    try:
        with open("data.json") as json_file:
            data = json.load(json_file)
            return data
    except:
        return {}

def check_code():
    if next((key for key in data.keys() if re.search(key, on_press.key_sequence)), None):
        return True, next((key for key in data.keys() if re.search(key, on_press.key_sequence)), None)
    else:
        return False, None

def clear():
    on_press.key_sequence = ""
    return

def on_press(key):
    global data
    try:
        on_press.key_sequence += str(key.char)
        if check_code()[0]:
            key = check_code()[1]
            for i in range(len(key)):
                keyboard.Controller().press(keyboard.Key.backspace)
                keyboard.Controller().release(keyboard.Key.backspace)
            on_press.key_sequence = ""
            keyboard.Controller().type(data[key])
            threading.Timer(0.1, clear).start()
            
    except AttributeError:
        pass
on_press.key_sequence = ""
data = load_data()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
