from time import sleep
import pygame
pygame.init()
import pifacedigitalio as p

p.init()

start = True

Stopper = 0
Stop = False

while start:
    DI4 = p.digital_read(4)
    DI5 = p.digital_read(5)
    DI6 = p.digital_read(6)
    Stopper = 0

    while DI4 and not DI6:
        Stopper = 0
        
        p.digital_write(0,1)
        p.digital_write(1,0)
        p.digital_write(2,0)
        p.digital_write(3,0)
        p.digital_write(4,0)
        p.digital_write(5,0)
        p.digital_write(6,0)
        p.digital_write(7,0)
        
        sleep(0.75)
        p.digital_write(4,1)
        sleep(0.75)

        DI4 = p.digital_read(4)
        DI6 = p.digital_read(6)

    if DI5:
        Stopper = 0
        
        sleep(0.2)
        p.digital_write(0,1)
        p.digital_write(1,1)
        p.digital_write(2,0)
        p.digital_write(3,1)
        p.digital_write(4,0)
        p.digital_write(5,0)
        p.digital_write(6,0)
        p.digital_write(7,0)
        sleep(3.0)
        while DI5 and not DI6:
            p.digital_write(1,0)
            sleep(0.5)
            p.digital_write(2,1)
            DI5 = p.digital_read(5)
            DI6 = p.digital_read(6)
        
    while not DI4 and not DI5 and not Stop:
        Stopper = Stopper + 1
        sleep(1.0)

        DI4 = p.digital_read(4)
        DI5 = p.digital_read(5)

        if Stopper >= 2:
            Stop = True
        
    if Stop:
        sleep(0.2)
        p.digital_write(0,0)
        p.digital_write(1,0)
        p.digital_write(2,0)
        p.digital_write(3,0)
        p.digital_write(4,0)
        p.digital_write(5,0)
        p.digital_write(6,0)
        p.digital_write(7,0)
        Stopper = 0
        Stop = False

    if DI6:
        p.digital_write(0,0)
        p.digital_write(1,0)
        p.digital_write(2,0)
        p.digital_write(3,0)
        p.digital_write(4,0)
        p.digital_write(5,0)
        p.digital_write(6,0)
        p.digital_write(7,0)
        start = 0
        
