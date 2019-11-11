import pygame
import gamebox
camera = gamebox.Camera(800,600)

logo = gamebox.from_image(-100, -100, "https://www.python.org/static/img/python-logo.png")

score = 0

def tick(keys):
    if pygame.K_UP in keys:
        print(" the up key is currently being pressed")
    if camera.mouseclick:
        logo.center = camera.mouse
    camera.draw(logo)
    camera.display()

gamebox.timer_loop(30, tick)