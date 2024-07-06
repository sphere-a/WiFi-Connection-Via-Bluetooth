import network
import time

WLAN : network.WLAN = network.WLAN(network.STA_IF)

def Init() -> None:
	global WLAN
	WLAN.active(True)

def Connect(SSID : str, Password : str, Time : float = 10) -> bool:
	global WLAN
	INTERVAL : float = 0.1
	WLAN.connect(SSID, Password)

	Count : int = 0
	while not WLAN.isconnected():
		time.sleep(INTERVAL)
		Count += 1
		if Count * INTERVAL >= Time:
			return False
	
	return WLAN.status() == network.STAT_GOT_IP

def Scan():
	global WLAN
	return [x[0].decode() for x in WLAN.scan()]

