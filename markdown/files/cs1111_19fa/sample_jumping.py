import pygame
import gamebox
camera = gamebox.Camera(400, 400)

character = gamebox.from_color(200, 200, 'blue', 15, 15)

blocks = [
    gamebox.from_color(180, 300, 'brown', 320, 20),
    gamebox.from_color(200, 180, 'darkgreen', 20, 140),
    gamebox.from_color(80, 260, 'black', 20, 80),
    gamebox.from_color(280, 290, 'black', 20, 80)
]
moving = [
    gamebox.from_color(230, 240, 'yellow', 20, 20),
    gamebox.from_color(260, 200, 'white', 20, 20)
]

def tick(keys):
    camera.clear('darkgray')

    if pygame.K_LEFT in keys:
        character.x -= 5       # move left
    if pygame.K_RIGHT in keys:
        character.x += 5       # move right

    #set gravity
    character.speedy += 1
    character.move_speed()



    #draw blocks
    for block in blocks:
        camera.draw(block)
        character.move_to_stop_overlapping(block)
        if character.bottom_touches(block) and pygame.K_UP in keys:
            character.speedy = -15




    camera.draw(character)

    camera.display()


gamebox.timer_loop(30, tick)