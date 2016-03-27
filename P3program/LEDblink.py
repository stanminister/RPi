from time import sleep
import pifacedigitalio as p
p.init()
p.digital_write(0,1)
sleep(0.5)
p.digital_write(0,0)
sleep(0.5)
p.digital_write(0,1)
sleep(0.5)
p.digital_write(0,0)
sleep(0.025)
p.digital_write(1,1)
n1 = 4
sum1 = 0
counter1 = 1
n2 = 8
sum2 = 0
counter2 = 1
n3 = 32
sum3 = 0
counter3 = 1
n4 = 128
sum4 = 0
counter4 = 1
while counter1 <= n1:
    p.digital_write(3,0)
    p.digital_write(2,1)
    sleep(0.5)
    p.digital_write(2,0)
    p.digital_write(3,1)
    sleep(0.5)
    sum1 = sum1 + counter1
    counter1 += 1

while counter2 <= n2:
    p.digital_write(3,0)
    p.digital_write(2,1)
    sleep(0.25)
    p.digital_write(2,0)
    p.digital_write(3,1)
    sleep(0.25)
    sum2 = sum2 + counter2
    counter2 += 1

while counter3 <= n3:
    p.digital_write(3,0)
    p.digital_write(2,1)
    sleep(0.05)
    p.digital_write(2,0)
    p.digital_write(3,1)
    sleep(0.05)
    sum3 = sum3 + counter3
    counter3 += 1

while counter4 <= n4:
    p.digital_write(3,0)
    p.digital_write(2,1)
    sleep(0.02)
    p.digital_write(2,0)
    p.digital_write(3,1)
    sleep(0.02)
    sum4 = sum4 + counter4
    counter4 += 1

p.digital_write(3,0)
p.digital_write(1,0)
sleep(1)
exit()
