"""Listen for key presses and replace them with the corresponding value"""
import threading
import re
from pynput import keyboard
from src import utils

def check_code():
    """Check if the key sequence is in the data dictionary and return the corresponding value"""
    key_match = next((key for key in data.keys() if re.search(key, on_press.key_sequence)), None)
    if key_match:
        return True, key_match
    return False, None

def clear():
    """Clear the key sequence"""
    on_press.key_sequence = ""

def on_press(key):
    """
    Check if the key sequence is in the data dictionary and replace it with the corresponding value
    """
    try:
        if key == keyboard.Key.backspace:
            on_press.key_sequence = on_press.key_sequence[:-1]
        else:
            on_press.key_sequence += key.char
        if check_code()[0]:
            key = check_code()[1]
            for _ in range(len(key)):
                keyboard.Controller().press(keyboard.Key.backspace)
                keyboard.Controller().release(keyboard.Key.backspace)
            on_press.key_sequence = ""
            keyboard.Controller().type(data[key])
            threading.Timer(0.1, clear).start()
    except AttributeError:
        pass
on_press.key_sequence = ""
data = utils.load_data()

def start_listener():
    """Start the listener"""
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
