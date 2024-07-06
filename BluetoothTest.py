import bluetooth
import WiFi

import sys

# ruff: noqa: E402
sys.path.append("")

from micropython import const

import asyncio
import aioble
import bluetooth

import random
import struct

# WiFi Setup UUID
WIFI_SETUP_UUID = bluetooth.UUID("6e400001-b5a1-f393-e0a9-e50e24dcca9e")
# SSID Characteristic
WIFI_UUID = bluetooth.UUID("6e400002-b5a1-f393-e0a9-e50e24dcca9e")
# Password Characteristic
PASSWORD_UUID = bluetooth.UUID("6e400003-b5a1-f393-e0a9-e50e24dcca9e")
# Networks Characteristic
NETWORKS_UUID = bluetooth.UUID("6e400004-b5a1-f393-e0a9-e50e24dcca9e")
# User ID Characteristic
UID_UUID = bluetooth.UUID("6e400005-b5a1-f393-e0a9-e50e24dcca9e")
# Connection Status Characteristic
CONN_STAT_UUID = bluetooth.UUID("6e400006-b5a1-f393-e0a9-e50e24dcca9e")

# org.bluetooth.characteristic.gap.appearance.xml
ADV_APPEARANCE_GENERIC_HID = const(960)

# How frequently to send advertising beacons.
ADV_INTERVAL_MS = 250_000


# Register GATT server.
Service = aioble.Service(WIFI_SETUP_UUID)
WiFiSSID = aioble.Characteristic(Service, WIFI_UUID, read=True, notify=True)
WiFiPassword = aioble.Characteristic(Service, PASSWORD_UUID, read=True, notify=True)
WiFiNetworks = aioble.Characteristic(Service, NETWORKS_UUID, write=True, notify=True)
UserID = aioble.Characteristic(Service, UID_UUID, read=True, notify=True)
ConnectionStatus = aioble.Characteristic(Service, CONN_STAT_UUID, write=True, notify=True)
aioble.register_services(Service)

WiFi.Init()

async def DeviceTask():
    while True:
        Networks : str = ""
        for i in WiFi.Scan(): Networks += i + ' '
        WiFiNetworks.write(Networks)
        await asyncio.sleep_ms(1000)


# Serially wait for connections. Don't advertise while a central is connected.
async def PeripheralTask():
    while True:
        async with await aioble.advertise(
            ADV_INTERVAL_MS,
            name="LeakGuard - Communications",
            services=[WIFI_SETUP_UUID],
            appearance=ADV_APPEARANCE_GENERIC_HID,
        ) as connection:
            print("Connection from", connection.device)
            await connection.disconnected(timeout_ms=None)


# Run both tasks.
async def main(): await asyncio.gather(asyncio.create_task(DeviceTask()), asyncio.create_task(PeripheralTask()))


asyncio.run(main())