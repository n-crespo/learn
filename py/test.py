from pynput import keyboard
import time

def on_press(key):
    if key == keyboard.Key.space:
        return False  # Stop listener

def wait_for_space(timeout):
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    start_time = time.time()
    while (time.time() - start_time) < timeout:
        if not listener.running:
            return True
        time.sleep(0.1)  # Sleep a bit to avoid busy waiting

    listener.stop()
    return False

def message(prompt, options):
    print(prompt)
    for option in options:
        print(option)

    if wait_for_space(4):
        print("Space bar pressed! Continuing...")
    else:
        print("Timeout: You did not press the space bar within 4 seconds.")

message("Please select 1 or 2", ["1", "2"])

