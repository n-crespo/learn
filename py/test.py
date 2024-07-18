from pynput import keyboard
import threading
import time

space_pressed = False


def on_press(key):
    global space_pressed
    if key == keyboard.Key.space:
        space_pressed = True
        return False  # Stop listener


def wait_for_space(timeout):
    global space_pressed
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    start_time = time.time()
    while not space_pressed and (time.time() - start_time) < timeout:
        time.sleep(0.1)  # Sleep a bit to avoid busy waiting

    listener.stop()
    return space_pressed


def message(prompt, options):
    print(prompt)
    for option in options:
        print(option)

    if wait_for_space(4):
        print("Space bar pressed! Continuing...")
    else:
        print("Timeout: You did not press the space bar within 4 seconds.")


message("Please select 1 or 2", ["1", "2"])
