from time import sleep
import pygame
pygame.init()
import pifacedigitalio as p

p.init()
p.digital_write(0,1)

song = pygame.mixer.Sound('/home/pi/Downloads/Halleluhja.wav')
clock = pygame.time.Clock()
song.play()
#(ha1)
sleep(0.5)
p.digital_write(1,1)
p.digital_write(2,1)
p.digital_write(3,1)
p.digital_write(4,1)
p.digital_write(5,1)
p.digital_write(6,1)
p.digital_write(7,1)
sleep(0.8)
#(le1)
p.digital_write(1,0)
p.digital_write(2,0)
p.digital_write(3,0)
p.digital_write(4,0)
p.digital_write(5,0)
p.digital_write(6,0)
p.digital_write(7,0)
sleep(0.4)
#(lu1)
p.digital_write(1,1)
p.digital_write(2,1)
p.digital_write(3,1)
p.digital_write(4,1)
p.digital_write(5,1)
p.digital_write(6,1)
p.digital_write(7,1)
sleep(0.3)
#(hja1)
p.digital_write(1,0)
p.digital_write(2,0)
p.digital_write(3,0)
p.digital_write(4,0)
p.digital_write(5,0)
p.digital_write(6,0)
p.digital_write(7,0)
sleep(1.1)

#(ha2)
p.digital_write(1,0)
p.digital_write(2,0)
p.digital_write(3,0)
p.digital_write(4,1)
p.digital_write(5,1)
p.digital_write(6,1)
p.digital_write(7,1)
sleep(0.7)
#(le2)
p.digital_write(1,1)
p.digital_write(2,1)
p.digital_write(3,1)
p.digital_write(4,0)
p.digital_write(5,0)
p.digital_write(6,0)
p.digital_write(7,0)
sleep(0.3)
#(lu2)
p.digital_write(1,0)
p.digital_write(2,0)
p.digital_write(3,0)
p.digital_write(4,1)
p.digital_write(5,1)
p.digital_write(6,1)
p.digital_write(7,1)
sleep(0.3)
#(hja2)
p.digital_write(1,0)
p.digital_write(2,0)
p.digital_write(3,0)
p.digital_write(4,0)
p.digital_write(5,0)
p.digital_write(6,0)
p.digital_write(7,0)
sleep(0.7)

#(ha3)
p.digital_write(1,1)
p.digital_write(2,1)
p.digital_write(3,1)
p.digital_write(4,0)
p.digital_write(5,0)
p.digital_write(6,0)
p.digital_write(7,0)
sleep(0.2)
#(le3)
p.digital_write(1,0)
p.digital_write(2,0)
p.digital_write(3,0)
p.digital_write(4,1)
p.digital_write(5,1)
p.digital_write(6,1)
p.digital_write(7,1)
sleep(0.2)
#(lu3)
p.digital_write(1,1)
p.digital_write(2,1)
p.digital_write(3,1)
p.digital_write(4,0)
p.digital_write(5,0)
p.digital_write(6,0)
p.digital_write(7,0)
sleep(0.2)
#(hja3)
p.digital_write(1,0)
p.digital_write(2,0)
p.digital_write(3,0)
p.digital_write(4,0)
p.digital_write(5,0)
p.digital_write(6,0)
p.digital_write(7,0)
sleep(0.5)

#(ha4)
p.digital_write(1,0)
p.digital_write(2,0)
p.digital_write(3,0)
p.digital_write(4,1)
p.digital_write(5,1)
p.digital_write(6,1)
p.digital_write(7,1)
sleep(0.2)
#(le4)
p.digital_write(1,1)
p.digital_write(2,1)
p.digital_write(3,1)
p.digital_write(4,0)
p.digital_write(5,0)
p.digital_write(6,0)
p.digital_write(7,0)
sleep(0.2)
#(lu4)
p.digital_write(1,0)
p.digital_write(2,0)
p.digital_write(3,0)
p.digital_write(4,1)
p.digital_write(5,1)
p.digital_write(6,1)
p.digital_write(7,1)
sleep(0.2)
#(hja4)
p.digital_write(1,0)
p.digital_write(2,0)
p.digital_write(3,0)
p.digital_write(4,0)
p.digital_write(5,0)
p.digital_write(6,0)
p.digital_write(7,0)
sleep(0.5)

#(ha5)
p.digital_write(1,1)
p.digital_write(2,1)
p.digital_write(3,0)
p.digital_write(4,0)
p.digital_write(5,0)
p.digital_write(6,0)
p.digital_write(7,0)
sleep(0.4)
#(le5)
p.digital_write(1,0)
p.digital_write(2,0)
p.digital_write(3,1)
p.digital_write(4,0)
p.digital_write(5,0)
p.digital_write(6,0)
p.digital_write(7,0)
sleep(0.3)
#(ee)
p.digital_write(1,1)
p.digital_write(2,1)
p.digital_write(3,0)
p.digital_write(4,0)
p.digital_write(5,0)
p.digital_write(6,0)
p.digital_write(7,0)
sleep(0.6)
#(luuu5)
p.digital_write(1,1)
p.digital_write(2,1)
p.digital_write(3,1)
p.digital_write(4,0)
p.digital_write(5,0)
p.digital_write(6,0)
p.digital_write(7,0)
sleep(0.4)
#(hja5)
p.digital_write(1,0)
p.digital_write(2,1)
p.digital_write(3,1)
p.digital_write(4,0)
p.digital_write(5,0)
p.digital_write(6,0)
p.digital_write(7,0)
sleep(0.3)


sleep(10)

p.digital_write(1,0)
p.digital_write(2,0)
p.digital_write(3,0)
p.digital_write(4,0)
p.digital_write(5,0)
p.digital_write(6,0)
p.digital_write(7,0)
p.digital_write(0,0)

exit()