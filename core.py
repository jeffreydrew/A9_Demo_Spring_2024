#!/usr/bin/python3

from eden import EdenAPI
from speech_in import SpeechIn
from speech_out import SpeechOut
import os, sys
import json
import asyncio

script_dir = os.path.dirname(os.path.abspath(__file__))
commands_path = os.path.join(script_dir, "commands.json")
scripts_path = os.path.join(script_dir, "scripts")
audio_path = os.path.join(script_dir, "audio_cache")


def check_input(eden, speech_out, input):
    os.system(f"mpg321 {audio_path}/off.mp3")

    input = input.lower()
    print(input)
    # if input in first item of command.keys
    if "play" in input:
        #parse the input to everything after play
        parsed_input = input.split("play ")[1]
        parsed_input = f"\"{parsed_input}\""
        #call scripts/play_music.py with parsed_input as argument
        os.system(f"{scripts_path}/play_music.py {parsed_input}")
    elif "google" in input:
        #parse the input to everything after google
        parsed_input = input.split("google ")[1]
        parsed_input = f"\"{parsed_input}\""
        #call scripts/google_search.py with parsed_input as argument
        os.system(f"{scripts_path}/google_search.py {parsed_input}")
    elif "type" in input:
        #parse 
        parsed_input = input.split("type ")[1]
        os.system(f"{scripts_path}/type_assistant.py {parsed_input}")
    elif input in commands.keys():
        os.system(commands[input][0])

    else:
        out = asyncio.run(eden.ask(input))
        speech_out.write(out)
    sys.exit()


if __name__ == "__main__":
    eden = EdenAPI()
    speech_in = SpeechIn()
    speech_out = SpeechOut()

    # load commands from json file
    with open(commands_path, "r") as f:
        commands = json.load(f)

    while True:
        os.system(f"mpg321 {audio_path}/on.mp3")
        #for windows
        #os.system(f"start wmplayer {audio_path}/on.mp3")
        #os.system(f"start vlc {audio_path}/on.mp3")

        input = speech_in.listen()
        check_input(eden, speech_out, input)
