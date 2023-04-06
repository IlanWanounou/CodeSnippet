import keyboard
import json
import time
from plyer import notification

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
        notification.notify(
            title = "Code correct",
            message = "Code correct",
            timeout = 5
        )
    else:
        if(len(code) > 4):
            notification.notify(
                title = "Code incorrect",
                message = "Code incorrect",
                timeout = 5
        )

def on_key_press(key):
    global str
    str += key.name
    checkCode(str)

str = ""
keyboard.on_press(on_key_press)
data = loadData()

while True:
    time.sleep(1)
