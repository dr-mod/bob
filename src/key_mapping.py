from adafruit_hid.keycode import Keycode as kc
from adafruit_hid.consumer_control_code import ConsumerControlCode as cc


STRING = 1
KEY = 2
CONTROL_CODE = 3

keys = [
    (KEY, [kc.ENTER]),
    # (STRING, "Button 1"),
    # (KEY, [kc.SPACE]),
    # (KEY, [kc.CONTROL, kc.R]),
    # (KEY, [kc.GUI, kc.V]),
    # (CONTROL_CODE, cc.VOLUME_INCREMENT),
]