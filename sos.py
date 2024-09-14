import machine
import time

LED_RED = 0
Blink_200 = 27
led = machine.Pin(LED_RED,machine.Pin.OUT)
Button0 = machine.Pin(Blink_200,machine.Pin.IN, machine.Pin.PULL_DOWN)


def blinked_led(times, duration):
    for i in range(times):
        led.on()
        time.sleep(duration)
        led.off()
        time.sleep(duration)
        
def send_sos(num_of_sos):
    for _ in range(num_of_sos):
        blinked_led(3, 0.2)
        blinked_led(3, 0.8)
        blinked_led(3, 0.2)
        
while True:
    if Button0.value() ==1:
        send_sos(1)
        time.sleep(0.1)