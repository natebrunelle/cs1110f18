#
# import pygame
# import gamebox
#
# camera = gamebox.Camera(800,600)
#
# # prep work: make the boxes and variables to be used later
#
# guido = gamebox.from_image(300, 200
# 	, "https://www.python.org/static/img/python-logo.png")
#
# ground = gamebox.from_color(300, 500, 'brown', 400, 10)
#
# # Every PyGame program should end with an event loop. There are a lot
# # of pieces to making these work, so gamebox adds a simpler version:
#
# # make a method that will be called every frame.
# # Must have parameter "keys"
# def tick(keys):
#     camera.clear('blue')
#
#     if pygame.K_UP in keys:
#         guido.y -= 5
#
#     #    print(" the up arrow key is currently being pressed")
#     if camera.mouseclick:  #true if some mouse button is being pressed
#         guido.center = camera.mouse # the current mouse position
#
#     guido.move_to_stop_overlapping(ground)
#     # ground.move_to_stop_overlapping(guido)
#
#     camera.draw(guido)
#     camera.draw(ground)
#     camera.display() # you almost always want to end this method
#                      # with this line
#
# # tell gamebox to call the tick method 30 times per second
# gamebox.timer_loop(30, tick)
# # this line of code will not be reached until after the window is closed
#





# import pygame
# import gamebox
# import random
# 
# width = 800
# height = 600
# camera = gamebox.Camera(width, height)
# 
# 
# # prep work: make the boxes and variables to be used later
# 
# guido = gamebox.from_image(300, 50
# 	, "https://www.python.org/static/img/python-logo.png")
# 
# ground = gamebox.from_color(width//2, height-10, 'brown', width, 10)
# 
# guido.speedy = 0
# 
# gravity = False
# gravity_accel = 1
# gravity_dir = 1
# gravity_strength = 0.1
# # Every PyGame program should end with an event loop. There are a lot
# # of pieces to making these work, so gamebox adds a simpler version:
# 
# # make a method that will be called every frame.
# # Must have parameter "keys"
# def tick(keys):
#     camera.clear('black')
#     global gravity,gravity_accel,gravity_dir,gravity_strength
#     #logo.x += random.randrange(-20, 20)
#     #logo.y += random.randrange(-20, 20)
# 
#     if len(keys) > 0:
#         if pygame.K_UP in keys:
#             guido.y -= 5
#         if pygame.K_DOWN in keys:
#             guido.y += 5
#         if pygame.K_LEFT in keys:
#             guido.x -= 5
#         if pygame.K_RIGHT in keys:
#             guido.x += 5
#         if pygame.K_g in keys:
#             print('gravity on')
#             guido.speedy = 1
#             gravity_accel = 1 + gravity_strength
#             gravity_dir = 1
#             gravity = True
#         if pygame.K_f in keys:
#             print('gravity off')
#             guido.speedy = 0
#             gravity_accel = 1
#             gravity_dir = 1
#             gravity = False
#         if pygame.K_h in keys:
#             gravity_strength *= 1.1
#             print('gravity_strength:', str(gravity_strength))
#         if pygame.K_j in keys:
#             gravity_strength *= 0.9
#             print('gravity_strength:', str(gravity_strength))
# 
#     if gravity:
#         if guido.speedy < 0.1:
#             gravity_accel = 1 + gravity_strength
#             gravity_dir = 1
#             guido.speedy = 1
#             gravity = True
#         else:
#             guido.speedy *= gravity_accel
#             guido.y += guido.speedy * gravity_dir
# 
# 
#     #if pygame.K_UP in keys: # you can check which keys are being pressed
#     #    print(" the up arrow key is currently being pressed")
#     if camera.mouseclick:  #true if some mouse button is being pressed
#         guido.center = camera.mouse # the current mouse position
# 
#     if guido.bottom >= ground.top:
#         guido.bottom = ground.top
#         #guido.speedy *= -1
#         gravity_accel = 1 - gravity_strength
#         gravity_dir = -1
# 
#     #print('guido.speedy,gravity,gravity_dir,gravity_accel')
#     #print(guido.speedy,gravity,gravity_dir,gravity_accel)
# 
#     guido.move_to_stop_overlapping(ground)
#     #ground.move_to_stop_overlapping(guido)
# 
#     camera.draw(guido)
#     camera.draw(ground)
#     camera.display() # you almost always want to end this method
#                      # with this line
# 
# # tell gamebox to call the tick method 30 times per second
# gamebox.timer_loop(30, tick)
# # this line of code will not be reached until after the window is closed


