from ppadb.client import Client
from PIL import Image
import numpy as np

"""
Download adb server from https://developer.android.com/studio/releases/platform-tools
Make sure to on developer mode in android device using:
    settings -> about phone -> software information -> build version (tap 7 times)
    
Go back to settings, developer mode should be there. Please turn it on. 

Ensure that phone is connected to computer via USB
cd to adb.exe and run `advb devices -l` to check if device is properly connected

Run the following for the client
    pip install pure-python-adb
"""

adb = Client(host="127.0.0.1", port=5037)
devices = adb.devices()
device = devices[0]
print(device.get_serial_no())

# in this example (swipe) X1=100, Y1=500, X2=100, Y2=1450, Duration = 100ms
# device.shell('input swipe 500 500 600 600 100')

# in this example (tap) X1=100, Y1=400
#device.shell('input tap 100 400')

# Here is a screenshot example
byte_image = device.screencap() # screen capture

with open('screen.png', 'wb') as f:
    f.write(byte_image)
    
image_file = Image.open('screen.png')
image_arr = np.array(image_file,dtype=np.uint8)
print(image_arr)
