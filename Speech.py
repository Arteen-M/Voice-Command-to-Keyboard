import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)
transcript = ["", ""]
to_script = 0

try:
    file = open("Commands.txt", "r")
    file.close()
except FileNotFoundError:
    file = open("Commands.txt", "w")
    file.close()

print("Listening")

while True:
    to_script = ""
    file = open("Commands.txt", "w")
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            to_script = r.recognize_google(audio)
            print("Recognized:", to_script)
        except sr.UnknownValueError:
            print("Unrecognized Audio")

    if "up" in to_script.lower() or "down" in to_script.lower() or "left" in to_script.lower() or "right" in to_script.lower() or "stop" in to_script.lower():
        transcript[0] = to_script

    if "alpha" in to_script.lower() or "bravo" in to_script.lower() or "x-ray" in to_script.lower() or "canuck" in to_script.lower():
        transcript[1] = to_script
    else:
        transcript[1] = ""

    file.writelines(transcript[0] + '\n')
    file.writelines(transcript[1])



