# Completed gamebox program - this is a program that was mostly created
#   during the 9AM section of CS1110 on 11/13/19.
#
# A rough outline of the order in which this program was made:
#
# create make_walker function for making person
# add player, the list to store the multiple walkers (1 for each image)
# create a stage_counter variable, add 1 each time tick() is called
#	to use for animating the person
# in the tick function, draw player1[stage_counter % len(player1)]
#   so there is always a valid image (stage_counter will get big)
# person should be walking now
# stage_counter can be decreased to a smaller value (i.e. 0.5) to make
#   the animation cycle slower
# we don't want to use the 6th image while walking, so don't cycle
#   that one in
# create move_walker function to handle movement each loop
# move_walker should have access to key presses
# move_walker parameters are keys and walker
# remember that walker is a list of gameboxes
# for frame in walker, change frame.x += 5
# from the tick function, call move_walker()
# the make_walker() function should be called outside of tick
# the walking animation should happen only when moving
# in move_walker, when we move, add to stage_counter
# don't always change stage_counter if we aren't moving
# stage_counter will need to be cast to an int when used as an index
# side scrolling - move the camera so that walker is always centered,
#   the camera's x coordinate can be set to the walker's x coordinate
# in move_walker, change x of camera to x of walker[0]
# create a couple obstacles, from color, and put them in a list
# in tick(), for each obstacle, draw it
# think of creating one big scene for the whole game first that is
#   bigger than the camera/window, then move the camera around as needed
# add multiplayer, by using different keys for each player
# make platforms - 2 from_color gameboxes
# in tick, draw platforms
# move platform, create function move_platform
# use keys to move platform up, down, left, right (can use a,d,w,s)
# walker shouldn't be able to walk through other things,
#   use move_to_stop_overlapping
# put walker on top of platform1 to start
# make gravity, initial value is 1
#   for frame in walker, speedy += gravity, frame.move_speed
# add lives - keep track of when the walker leaves the screen
# def is_walker_off_screen(walker)
# compare top of walker and bottom of screen
# in tick, if player1 off, for frame in walker,
#   frame.bottom = platform1.top,  player1.x = platform1.x
# initialize lives 3
# in if player off, subtract 1 from lives
# make a gamebox for lives, from_circle
# draw that gamebox if alive
# if lives, draw lives gamebox
# extra life can be a collectable
# if player.touches(extra_life), increase lives
#


import pygame
import gamebox

camera = gamebox.Camera(800, 600)

# background

# background = gamebox.from_image(400, 300, 'globe.jpg')
# background.scale_by(0.7)

obstacles = [gamebox.from_color(1000, 400, 'darkgreen', 30, 30),
			 gamebox.from_color(2000, 400, 'darkgreen', 30, 700)
			 ]

# person
stepcount = 0
frames = 0
frame = 0


def make_walker(x, y):
	global frames
	images = gamebox.load_sprite_sheet("walk_stand.png", 1, 6)
	frames = len(images)
	walker = [] # walker is a list of gameboxes
	for image in images:
		walker.append(gamebox.from_image(x, y, image))
	return walker


walking_speed = 5


def move_walker(walker, keys):
	global stepcount
	global frame
	if pygame.K_RIGHT in keys:
		for frame in walker:
			frame.x += walking_speed
		stepcount += 0.5
		frame = int(stepcount) % (frames - 1)
	elif pygame.K_LEFT in keys:
		for frame in walker:
			frame.x -= walking_speed
		stepcount -= 0.5
		frame = int(stepcount) % (frames - 1)
	else:
		frame = frames - 1
	camera.x = walker[0].x
	walker_fall(walker)
	for obstacle in obstacles:
		for the_frame in walker:
			the_frame.move_to_stop_overlapping(obstacle)
	return


is_falling = False


def walker_fall(walker):
	global is_falling
	for frame in walker:
		frame.speedy += gravity
		frame.move_speed()
	is_falling = True
	for platform in platforms:
		for frame in walker:
			frame.move_to_stop_overlapping(platform)
		if walker[0].bottom_touches(platform):
			is_falling = False
	return


def draw_walker(walker):
	camera.draw(walker[frame])


player = make_walker(400, 300)


def walker_offscreen(walker):
	return walker[0].top > camera.bottom


def replace_walker(walker):
	for frame in walker:
		frame.x = platforms[active_index].x
		frame.bottom = platforms[active_index].y
		camera.x = frame.x


# Platforms:

platform_width = 200

platform1 = gamebox.from_color(0, 0, 'orangered', platform_width, 10)
platform1.top = player[0].bottom
platform1.x = player[0].x

platform2 = gamebox.from_color(0, 0, 'purple', platform_width, 10)
platform2.top = player[0].bottom
platform2.left = platform1.right

platforms = [platform1, platform2]

active_index = 0


def move_platform(platform, keys):
	if pygame.K_d in keys:
		platform.x += 20
	if pygame.K_a in keys:
		platform.x -= 20
	if pygame.K_w in keys:
		platform.y -= 20
	if pygame.K_s in keys:
		platform.y += 20


def switch_platform():
	global active_index
	active_index = (active_index + 1) % len(platforms)


# physics

gravity = 1

switch_time = 0

# lives

lives = 3

life_boxes = [gamebox.from_circle(camera.right - 20, camera.top + 20, 'red', 15),
			  gamebox.from_circle(camera.right - 60, camera.top + 20, 'red', 15),
			  gamebox.from_circle(camera.right - 100, camera.top + 20, 'red', 15),
			  gamebox.from_circle(camera.right - 140, camera.top + 20, 'red', 15)
			  ]

extra_life = gamebox.from_circle(2500, 300, 'red', 15)
extra_life_collected = False


def draw_lives(num_lives):
	first_x = camera.right - 20
	y = camera.top + 20
	for i in range(num_lives):
		life = gamebox.from_circle(first_x - i * 40, y, 'red', 15)
		# life = life_boxes[i]
		# life.x = first_x - i*40
		camera.draw(life)


def tick(keys):
	global switch_time, lives, extra_life_collected

	camera.clear('lightblue')

	if switch_time >= 15:
		if pygame.K_SPACE in keys:
			switch_platform()
			switch_time = 0
	else:
		switch_time += 1
	if walker_offscreen(player):
		replace_walker(player)
		lives -= 1
	move_platform(platforms[active_index], keys)
	move_walker(player, keys)
	draw_walker(player)
	for platform in platforms:
		camera.draw(platform)
	for obstacle in obstacles:
		camera.draw(obstacle)

	if player[0].touches(extra_life) and not extra_life_collected:
		lives += 1
		extra_life_collected = True
	draw_lives(lives)
	if not extra_life_collected:
		camera.draw(extra_life)
	camera.display()


gamebox.timer_loop(30, tick)
