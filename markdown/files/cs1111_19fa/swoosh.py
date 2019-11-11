import pygame
import gamebox

camera = gamebox.Camera(800, 600)

# scenery
background = gamebox.from_image(400, 300, 'uva_court.jpg')
background.scale_by(0.8)
court = gamebox.from_color(400, 500, 'blue', 300, 50)
backboard = gamebox.from_color(475, 400, 'white', 30, 150)
hoop = gamebox.from_image(445, 350, 'hoop.png')
hoop.scale_by(0.1)
scenery = [background, court, backboard, hoop]  # Things that are stationary
obstacles = [court, backboard]  # things that are "solid"

# interactive
ball = gamebox.from_circle(300, 465, 'orangered', 10)

# stats
score = 0
lives = 3

# physics
gravity = 0.75
jump_speed = 20

# other
scored_since_landed = False


def draw_scenery():
    """Draw all the stationary items"""
    for item in scenery:
        camera.draw(item)


def draw_stats():
    """draws the gameplay information (lives, score)"""
    scorebox = gamebox.from_text(75, 25, "score: " + str(score), 36, 'red')
    camera.draw(scorebox)
    for i in range(lives):
        heart = gamebox.from_image(775, 25, 'heart.png')
        heart.x -= 50 * i
        heart.scale_by(0.5)
        camera.draw(heart)


def move_ball(keys):
    """Determines where the ball should be by checking for user input and obstacles"""
    global scored_since_landed
    if pygame.K_RIGHT in keys:
        ball.speedx += 1
    if pygame.K_LEFT in keys:
        ball.speedx -= 1
    for obstacle in obstacles:
        if ball.bottom_touches(obstacle):
            scored_since_landed = False
            if pygame.K_UP in keys:
                ball.speedy = -jump_speed
    ball.speedy += gravity
    ball.move_speed()
    for obstacle in obstacles:
        ball.move_to_stop_overlapping(obstacle)


def points_scored():
    """Checks if the user scored a basket this tick"""
    global scored_since_landed
    if ball.touches(hoop) and not scored_since_landed and ball.speedy > 0:
        scored_since_landed = True
        return 2
    return 0


def out_of_bounds():
    """checks if the ball is out of bounds"""
    return ball.y > 600 or (ball.touches(hoop) and ball.speedy < 0)


def reset_ball():
    """replace the ball when it's out of bounds"""
    ball.x = 400
    ball.y = 300
    ball.speedx = 0
    ball.speedy = 0


def game_over():
    """checks if there is a game over, draws things based on that"""
    if lives == 0:
        camera.draw(gamebox.from_text(400, 300, 'You Lose', 42, 'white', True))
        camera.display()
        return True
    return False


def tick(keys):
    global score, lives
    camera.clear('black')
    if game_over():
        return
    draw_scenery()
    draw_stats()
    move_ball(keys)
    score += points_scored()
    if out_of_bounds():
        lives -= 1
        reset_ball()
    camera.draw(ball)
    camera.display()


gamebox.timer_loop(30, tick)
