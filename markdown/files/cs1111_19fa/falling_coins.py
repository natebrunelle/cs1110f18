import pygame
import gamebox
import random

camera=gamebox.Camera(800,600)

score = 0
time = 1800       # 1 minute -> (1sec=30 per sec) * 60sec = 1800
#time = 9000      # 5 minutes -> (1sec=30 per sec) * 60sec * 5min = 9000

box_lower = gamebox.from_color(100,590,"white",50,20)
box_lower.speedx = 10

my_text_box = gamebox.from_text(50,100,"Hooray",30,"red")

box_upper = gamebox.from_color(100,400,"white",50,20)
box_upper.speedx = 10

coins = [
    gamebox.from_color(random.randint(10,750), -10, "yellow", 12, 12),
    gamebox.from_color(random.randint(10,750), -10, "yellow", 12, 12),
    gamebox.from_color(random.randint(10, 750), -10, "blue", 12, 12)

]

def tick(keys):
    global time, score, minutes

    camera.clear("black")

    time -= 1

    # calculate minutes, seconds, and fractions of seconds
    frac = str(int((time % ticks_per_second) / ticks_per_second * 10))
    seconds = str(int((time / ticks_per_second) % 60)).zfill(2)
    minutes = str(int((time / ticks_per_second) / 60))

    # write timer to screen
    timer = gamebox.from_text(650, 50, "Timer: " + minutes + ":" + seconds + "." + frac, 24, "red")
    camera.draw(timer)

    # Check if box_lower goes out of boundaries
    if box_lower.speedx > 0 and box_lower.x > 800:
        box_lower.speedx = -10     # acceleration on horizontal direction
    if box_lower.speedx < 0 and box_lower.x < 0:
        box_lower.speedx = 10
    box_lower.move_speed()

    if pygame.K_RIGHT in keys:
        box_upper.x += 5
    if pygame.K_LEFT in keys:
        box_upper.x -= 5
    if pygame.K_UP in keys:
        box_upper.y -= 5
    if pygame.K_DOWN in keys:
        box_upper.y += 5

    # reset to make sure box_upper is inside the window
    if box_upper.x <= 0:
        box_upper.x = 0
    elif box_upper.x >= 800:
        box_upper.x = 800

    for coin in coins:
        coin.speedy += 0.03    # acceleration on horizontal direction

        # if a box touches a coin, increase score and remove a coin from a list
        if box_upper.touches(coin):
            score += 1
            coins.remove(coin)
        elif box_lower.touches(coin):
            score += 10
            coins.remove(coin)
        elif coin.y >= 610:
            coins.remove(coin)
            score -= 1
        else:
            coin.move_speed()
        camera.draw(coin)

    if len(coins) < 2:
        new_coin = gamebox.from_color(random.randint(10,750), -10, "yellow", 12, 12)
        coins.append(new_coin)

    # write timer to screen
    scr = gamebox.from_text(100, 50, "Score: " + str(score), 24, "red")
    camera.draw(scr)

    camera.draw(box_upper)
    # typically here you update the position of the characters
    # then you call camera.draw(box) for each GameBox you made
    camera.draw(box_lower)

    if score < 0:
        camera.draw(gamebox.from_text(300, 300, "DEAD", 70, "red"))
        # this line will end the game
        gamebox.pause()

    if time <= 0:
        camera.draw(gamebox.from_text(300, 300, "GAME OVER", 70, "red"))
        # this line will end the game
        gamebox.pause()

    # usually camera.display() should be the last line of the tick method
    camera.display()

ticks_per_second = 30
gamebox.timer_loop(ticks_per_second,tick)