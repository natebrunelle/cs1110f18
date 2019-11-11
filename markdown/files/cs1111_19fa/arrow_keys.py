import pygame
import gamebox
camera = gamebox.Camera(200, 200)

ship = gamebox.from_image(100, 100, "http://www.cs.virginia.edu/~up3f/cs1111/images/spaceship.jpg")
# try different x,y coordinate  (notice the screen size (200, 200) above)

def tick(keys):
    camera.clear('black')

    if pygame.K_LEFT in keys:
        ship.x -= 5
    if pygame.K_RIGHT in keys:
        ship.x += 5
    if pygame.K_UP in keys:
        ship.y -= 5
    if pygame.K_DOWN in keys:
        ship.y += 5

    camera.draw(ship)
    camera.display()

gamebox.timer_loop(30, tick)