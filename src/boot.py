import usb_cdc
import storage
import board, digitalio


usb_cdc.enable(console=False, data=False)
button = digitalio.DigitalInOut(board.GP7)
button.pull = digitalio.Pull.UP
if button.value:
   storage.disable_usb_drive()

