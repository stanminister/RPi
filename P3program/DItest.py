from time import sleep
import pygame
pygame.init()
import pifacedigitalio as p

p.init()
p.digital_write(0,1)

start = 1
while start == 1:
    DI4 = p.digital_read(4)
    p.digital_write(1,DI4)
    DI5 = p.digital_read(5)
    p.digital_write(2,DI5)
    DI6 = p.digital_read(6)
    p.digital_write(3,DI6)


