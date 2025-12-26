import machine
import time

led = machine.Pin(4 , machine.pin.OUT)

while True:
  led.value(1)
  time.sleep(1)
  led.value(0)
  time.sleep(1)