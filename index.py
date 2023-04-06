import keyboard
import json
def loadData():
    try:
        with open("data.json") as json_file:
            data = json.load(json_file)
            return data
    except:
        return {}

def on_key_press(key):
    print(f"Touche pressée : {key.name}")

keyboard.on_press(on_key_press)
data = loadData()