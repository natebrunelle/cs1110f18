# Modified from example by Prof. Tychonievich

import pygame
import gamebox
camera = gamebox.Camera(300, 300)

character = gamebox.from_color(150, 150, 'brown', 10, 10)
things = [
    gamebox.from_color(150, 250, 'green', 200, 50),
    gamebox.from_color(220, 200, 'white', 20, 100),
    gamebox.from_color(80, 100, 'black', 80, 20),
]
moving = [
    gamebox.from_color(120, 150, 'red', 20, 20),
]
for thing in moving:
    thing.being_carried = False


def tick(keys):
    camera.clear('lightblue')

    if pygame.K_LEFT in keys:
        character.x -= 5
    if pygame.K_RIGHT in keys:
        character.x += 5

    if pygame.K_UP in keys:
        for thing in things + moving:
            if character.bottom_touches(thing):
                character.speedy = -15


    character.speedy += 1
    # character.y += character.speedy
    character.move_speed()

    for thing in things:
        character.move_to_stop_overlapping(thing)
    for thing in moving:
        if character.touches(thing):
            thing.being_carried = True

    for thing in moving:
        if thing.being_carried:
            thing.left = character.right
            thing.y = character.y

    for thing in things + moving:
        camera.draw(thing)
    camera.draw(character)
    # ground.move_to_stop_overlapping(character)

    camera.display()


gamebox.timer_loop(30, tick)