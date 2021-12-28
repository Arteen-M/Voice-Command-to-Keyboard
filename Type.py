from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
current_key = [None, None]

try:
    file = open("Commands.txt", "r")
    file.close()
except FileNotFoundError:
    file = open("Commands.txt", "w")
    file.close()

file = open("Commands.txt", "r")


while True:

    transcript = []

    file.close()
    file = open("Commands.txt", "r")

    for x in range(1, 3):
        transcript += file.readlines(x)
    for x in range(2 - len(transcript)):
        transcript.append("")
    print(transcript)

    if "up" in transcript[0]:
        print("Moving Up")
        current_key[1] = current_key[0]
        current_key[0] = Key.up
    elif "down" in transcript[0]:
        print("Moving Down")
        current_key[1] = current_key[0]
        current_key[0] = Key.down
    elif "left" in transcript[0]:
        print("Moving Left")
        current_key[1] = current_key[0]
        current_key[0] = Key.left
    elif "right" in transcript[0]:
        print("Moving Right")
        current_key[1] = current_key[0]
        current_key[0] = Key.right
    elif "stop" in transcript[0]:
        if current_key[0] is not None and current_key[1] is not None:
            keyboard.release(current_key[0])
            keyboard.release(current_key[1])
        current_key = [None, None]

    if "alpha" in transcript[1].lower():
        print("A Button")
        keyboard.press(Key.space)
    elif "bravo" in transcript[1].lower():
        print("B Button")
        keyboard.press(Key.tab)
    elif "x-ray" in transcript[1].lower():
        print("X Button")
        keyboard.press(Key.insert)
    elif "canuck" in transcript[1].lower():
        print("Y Button")
        keyboard.press(Key.backspace)

    if current_key[0] is not None:
        keyboard.press(current_key[0])
    if current_key[1] is not None and current_key[0] != current_key[1]:
        keyboard.release(current_key[1])
        current_key[1] = None

    time.sleep(0.2)

    keyboard.release(Key.space)
    keyboard.release(Key.tab)
    keyboard.release(Key.insert)
    keyboard.release(Key.backspace)
