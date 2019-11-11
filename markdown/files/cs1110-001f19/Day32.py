#### this file contains 3 different programs: 
# - a starting point
# - code created during our class
# - code created during the 9AM class


# # Example of a good starting outline for a gamebox game program
# import pygame
# import gamebox
#
# # every game needs a camera
# # set the initial screen/window size with a width and height
# camera = gamebox.Camera(800, 600)
#
# ##############################  SCENERY  ##############################
#
# # create boxes for background objects
# #
# box1 = gamebox.from_color(400, 300, 'blue', 100, 50)
# #box2 = gamebox.from_text(400, 300, 'Hello World', 20, 'red')
# #box3 = gamebox.from_image(400, 300, 'my_image.jpg')
#
#
# # create a function for drawing the scenery
# #
# def draw_scenery():
# 	# draw each scenery box
# 	camera.draw(box1)
#
#
# ######################## INTERACTIVE COMPONENTS ########################
#
# # create boxes that will be active
# #
# inter_box1 = gamebox.from_color(100, 300, 'green', 75, 75)
#
#
# #
# # create a function for drawing the interactives
# #
# def draw_interactives(keys):
#
# 	# respond to keys
# 	handle_keys(keys)
#
# 	# move an interactive according to its speed
# 	inter_box1.move_speed()
#
# 	# don't let some things overlap
# 	inter_box1.move_to_stop_overlapping(box1)
#
# 	# draw each interactive box
# 	camera.draw(inter_box1)
#
#
# # handle keys used
# def handle_keys(keys):
# 	if pygame.K_RIGHT in keys:
# 		inter_box1.speedx += 1
#
#
# ################################ STATS ################################
#
# # initialize stat variables
# #
# # create any stat boxes needed
# #
# # draw the stat boxes
# #
# # update the stat boxes each loop
#
#
# ############################### PHYSICS ###############################
#
# # initialize physics variables
# #
# # update physics each loop
#
# ############################## MAIN LOOP ##############################
#
# def tick(keys):
# 	# clear camera
# 	camera.clear('black')
#
# 	# update the physics
#
# 	# draw the scenery
# 	draw_scenery()
#
# 	# draw the interactive components
# 	draw_interactives(keys)
#
# 	# update the stats
#
# 	# show the updated scene
# 	camera.display()
#
#
# # Start the main game loop
# # redraw the scene 30 times per second, call the tick function
# gamebox.timer_loop(30, tick)







# # Code created during our class
# 
# import pygame
# import gamebox
# 
# # every game needs a camera
# # set the initial screen/window size with a width and height
# width = 800
# height = 600
# camera = gamebox.Camera(width, height)
# 
# # initialize stat variables
# score = 0
# 
# ##############################  SCENERY  ##############################
# 
# # create boxes for background objects
# #
# 
# #box1 = gamebox.from_color(400, 300, 'blue', 100, 50)
# #box2 = gamebox.from_text(400, 300, 'Hello World', 20, 'red')
# #box3 = gamebox.from_image(400, 300, 'my_image.jpg')
# hwy = gamebox.from_image(width // 2, height // 2, 'hwy.png')
# hwy.scale_by(3)
# hwy.rotate(90)
# 
# # create a function for drawing the scenery
# #
# def draw_scenery():
#  # draw each scenery box
#  camera.draw(hwy)
# 
# 
# ######################## INTERACTIVE COMPONENTS ########################
# 
# # create boxes that will be active
# #
# frog = gamebox.from_color(100, 300, 'green', 60, 60)
# car1 = gamebox.from_color(300, height - 20, 'blue', 40, 100)
# car2 = gamebox.from_color(200, height - 20, 'purple', 40, 100)
# car3 = gamebox.from_color(400, height - 20, 'pink', 40, 100)
# interactives = [car1, car2, car3, frog]
# cars = [car1, car2, car3]
# 
# car1.speedy = -2
# car2.speedy = -3
# car3.speedy = -1
# 
# 
# #
# # create a function for drawing the interactives
# #
# def draw_interactives(keys):
# 
#  # respond to keys
#  handle_keys(keys)
# 
#  # move an interactive according to its speed
#  for each in cars:
#    each.move_speed()
#    frog.move_to_stop_overlapping(each)
# 
#  # don't let some things overlap
# 
# 
#  # draw each interactive box
#  for each in interactives:
#      camera.draw(each)
# 
# 
# # handle keys used
# def handle_keys(keys):
#  if pygame.K_RIGHT in keys:
#     frog.x += 5
#  if pygame.K_LEFT in keys:
#     frog.x -= 5
#  if pygame.K_UP in keys:
#     frog.y -= 5
#  if pygame.K_DOWN in keys:
#     frog.y += 5
# 
# 
# ################################ STATS ################################
# 
# 
# # create any stat boxes needed
# stat_box = gamebox.from_text(50, 50, 'Score: ' + str(score), 40, 'red')
# 
# # draw the stat boxes
# def draw_stats():
#    global score
#    score+=1
#    camera.draw(stat_box)
# 
# # update the stat boxes each loop - call from tick function
# 
# 
# ############################### PHYSICS ###############################
# 
# # initialize physics variables
# #
# # update physics each loop
# 
# ############################## MAIN LOOP ##############################
# 
# def tick(keys):
#  # clear camera
#  camera.clear('black')
# 
#  # update the physics
# 
#  # draw the scenery
#  draw_scenery()
# 
#  # draw the interactive components
#  draw_interactives(keys)
# 
#  # update the stats
#  draw_stats()
# 
#  # show the updated scene
#  camera.display()
# 
# 
# # Start the main game loop
# # redraw the scene 30 times per second, call the tick function
# gamebox.timer_loop(30, tick)
# 























# # Example gamebox program developed during 9:00 section
# import pygame
# import gamebox
#
# camera = gamebox.Camera(800, 600)
#
# # scenery
# background = gamebox.from_image(400, 300, 'uva_court.jpg')
# background.scale_by(0.8)
# court = gamebox.from_color(400, 500, 'blue', 300, 50)
# backboard = gamebox.from_color(475, 400, 'white', 30, 150)
# hoop = gamebox.from_image(445, 350, 'hoop.png')
# hoop.scale_by(0.1)
# scenery = [background, court, backboard, hoop]  # Things that are stationary
# obstacles = [court, backboard]  # things that are "solid"
#
# # interactive
# ball = gamebox.from_circle(300, 465, 'orangered', 10)
#
# # stats
# score = 0
# lives = 3
#
# # physics
# gravity = 0.75
# jump_speed = 20
#
# # other
# scored_since_landed = False
#
#
# def draw_scenery():
#    """Draw all the stationary items"""
#    for item in scenery:
#        camera.draw(item)
#
#
# def draw_stats():
#    """draws the gameplay information (lives, score)"""
#    scorebox = gamebox.from_text(75, 25, "score: " + str(score), 36, 'red')
#    camera.draw(scorebox)
#    for i in range(lives):
#        heart = gamebox.from_image(775, 25, 'heart.png')
#        heart.x -= 50 * i
#        heart.scale_by(0.5)
#        camera.draw(heart)
#
#
# def move_ball(keys):
#    """Determines where the ball should be by checking for user input and obstacles"""
#    global scored_since_landed
#    if pygame.K_RIGHT in keys:
#        ball.speedx += 1
#    if pygame.K_LEFT in keys:
#        ball.speedx -= 1
#    for obstacle in obstacles:
#        if ball.bottom_touches(obstacle):
#            scored_since_landed = False
#            if pygame.K_UP in keys:
#                ball.speedy = -jump_speed
#    ball.speedy += gravity
#    ball.move_speed()
#    for obstacle in obstacles:
#        ball.move_to_stop_overlapping(obstacle)
#
#
# def points_scored():
#    """Checks if the user scored a basket this tick"""
#    global scored_since_landed
#    if ball.touches(hoop) and not scored_since_landed and ball.speedy > 0:
#        scored_since_landed = True
#        return 2
#    return 0
#
#
# def out_of_bounds():
#    """checks if the ball is out of bounds"""
#    return ball.y > 600 or (ball.touches(hoop) and ball.speedy < 0)
#
#
# def reset_ball():
#    """replace the ball when it's out of bounds"""
#    ball.x = 400
#    ball.y = 300
#    ball.speedx = 0
#    ball.speedy = 0
#
#
# def game_over():
#    """checks if there is a game over, draws things based on that"""
#    if lives == 0:
#        camera.draw(gamebox.from_text(400, 300, 'You Lose', 42, 'white', True))
#        camera.display()
#        return True
#    return False
#
#
# def tick(keys):
#    global score, lives
#    camera.clear('black')
#    if game_over():
#        return
#    draw_scenery()
#    draw_stats()
#    move_ball(keys)
#    score += points_scored()
#    if out_of_bounds():
#        lives -= 1
#        reset_ball()
#    camera.draw(ball)
#    camera.display()
#
#
# gamebox.timer_loop(30, tick)
#
