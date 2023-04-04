import keyboard

def on_key_press(key):
    print(f"Touche pressée : {key.name}")

keyboard.on_press(on_key_press)