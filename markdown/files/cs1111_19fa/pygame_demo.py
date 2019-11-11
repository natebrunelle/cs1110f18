import pygame
import gamebox

camera = gamebox.Camera(800,600)

time = 0

def tick(keys):
    global time

    camera.clear("blue")

    time += 1
    frac = str(int((time%ticks_per_second)/ticks_per_second*10))
    seconds = str(int((time/ticks_per_second)%60)).zfill(2)
    minutes = str(int((time/ticks_per_second)/60))

    timer = gamebox.from_text(50,100,minutes+":"+seconds+"."+frac,24,"red")
    camera.draw(timer)

    camera.display()

ticks_per_second = 10

gamebox.timer_loop(ticks_per_second, tick)