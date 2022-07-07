import time
import board
import digitalio
import usb_hid
import key_mapping as km
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl


def send_keys(button_number):
    try:
        key = km.keys[button_number]
        state = buttons[button_i]
        if state:
            if key[0] == km.STRING:
                keyboard_layout.write(key[1])
            elif key[0] == km.KEY:
                keyboard.press(*key[1])
            elif key[0] == km.CONTROL_CODE:
                cc.press(key[1])
        else:
            if key[0] == km.KEY:
                keyboard.release(*key[1])
            elif key[0] == km.CONTROL_CODE:
                cc.release()
    except ValueError:
        pass


receiver_pins = [board.GP7]

receivers = []
for pin in receiver_pins:
    receiver = digitalio.DigitalInOut(pin)
    receiver.switch_to_input(pull=digitalio.Pull.UP)
    receivers.append(receiver)

buttons_count = len(receivers)
buttons = [False] * buttons_count
history = [False] * buttons_count

time.sleep(1)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
cc = ConsumerControl(usb_hid.devices)

receivers_count = len(receivers)

while True:
    for receiver_i in range(receivers_count):
        buttons[receiver_i] = not receivers[receiver_i].value
    for button_i in range(buttons_count):
        if buttons[button_i] != history[button_i]:
            send_keys(button_i)
            history[button_i] = buttons[button_i]
    time.sleep(0.01)
