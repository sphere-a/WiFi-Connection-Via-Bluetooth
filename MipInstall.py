import network
import time

WLAN = network.WLAN(network.STA_IF)
WLAN.active(True)
WLAN.connect(input('Network: '), input('Password: '))
while not WLAN.isconnected():
	print("Waiting for connection...")
	time.sleep(1)
print("Connected!")

import mip
mip.install(input('Package: '))

