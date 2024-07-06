# Bluetooth Test

For setting up WiFi connection for a Raspberry PI Pico via Bluetooth.

## Installation

Install adafruit-ampy via [pip](https://pip.pypa.io/en/stable/):

```bash
pip install adafruit-ampy
```

Upload the files to the PI Pico:

```bash
ampy --port com3 upload . # The port might be different on you PC
```

Install libraries on your PI Pico:
In a REPL which you can open via a serial monitor connected to your PI type:

```Python
import MipInstall
# Enter your WiFi credentials
# In package type: "aioble"
```

Restart your PI.

## Usage

To start the Bluetooth device,
open a REPL via a serial monitor connected to your PI and type:

```Python
import BluetoothTest
```