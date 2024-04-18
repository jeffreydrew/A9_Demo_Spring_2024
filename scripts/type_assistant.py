#!/usr/bin/python3

from pynput.keyboard import Controller
import time
import sys

#string_arg = sys.argv[1]

def type_string(s):
    keyboard = Controller()

    # Add a small delay to ensure the active window is ready to receive input
    time.sleep(0.1)

    for char in s:
        keyboard.type(char)

if __name__ == "__main__":
    type_string('string_arg')
