import tinytuya
import time

device = tinytuya.BulbDevice(
    dev_id="eb3256ed7aa143bf7e0lxx",   # Device ID
    address="192.168.0.92",           # IP del dispositivo
    local_key="*}S:D86M0J7|tGgC",    # Local Key
    version=3.4
)
device.set_socketPersistent(True) 
print(device.status())       # Ver estado actual

while True:
    device.turn_on()
    time.sleep(2)
    device.turn_off()
    time.sleep(2)
    device.turn_on()