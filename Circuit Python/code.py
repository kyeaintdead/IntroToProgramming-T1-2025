from adafruit_circuitplayground import cp
import time

def wrong():
    cp.pixels.fill((255, 0, 0))
    cp.start_tone(500)
    time.sleep(0.5)
    cp.stop_tone()
    cp.pixels.fill((0, 0, 0))
    time.sleep(0.2)
    return




def get_press():
    while True:
        if cp.button_a and cp.button_b:
            while cp.button_a or cp.button_b:
                pass
            return "AB"
        if cp.button_a:
            while cp.button_a:
                pass
            return "A"
        if cp.button_b:
            while cp.button_b:
                pass
            return "B"

def step_A():
    if get_press() != "A":
        wrong()
        return False
    return True

def step_B():
    if get_press() != "B":
        wrong()
        return False
    return True

def step_AB():
    if get_press() != "A+B":
        success()
        return False
    return True

def success():
    cp.pixels.fill((0, 255, 0))
    cp.start_tone(800)
    time.sleep(0.5)
    cp.stop_tone()
    cp.pixels.fill((0, 0, 0))
    time.sleep(0.3)

while True:
    if not step_A(): continue
    if not step_A(): continue
    if not step_B(): continue
    if not step_A(): continue
    if not step_B(): continue
    if not step_B(): continue
    if not step_B(): continue
    if not step_A(): continue
    if not step_A(): continue
    if not step_AB(): continue
    success()

