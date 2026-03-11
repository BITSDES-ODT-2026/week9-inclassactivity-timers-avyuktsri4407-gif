from machine import Pin
import time

pb1 = Pin(18,Pin.IN,Pin.PULL_UP)
pb2 = Pin(19,Pin.IN,Pin.PULL_UP)
count = 0
start = 0

while True:
    pb1_val = pb1.value()
    pb2_val = pb2.value()
    
    if pb1_val == 0 and count == 0:
        start = time.ticks_ms()
        count = 1
        print("Timer Started")
        time.sleep(0.2) 
        
    elif pb1_val == 0 and count > 0:
        current = time.ticks_ms()
        dif = time.ticks_diff(current, start)/1000
        print("Elapsed:", dif, "s")
        time.sleep(0.2)
        
    if pb2_val == 0:
        if count > 0:
            end = time.ticks_ms()
            dif2 = time.ticks_diff(end, start)/1000
            print("Final Time:", dif2, "s")
            count = 0
            time.sleep(0.2) 
        else:
            print("Timer not Started")
            time.sleep(0.2)

#Code for Advanced StopWatch
