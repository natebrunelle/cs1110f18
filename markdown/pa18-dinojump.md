---
title: "PA 18: dinojump.py"
...

# Task

In a file named `dinojump.py`, implement a simplified version the Google Chrome "there's no internet "dinosaur jumping game using pygame. If you are using Google Chrome, you can play it by typing chrome://dino/ into the browser's address bar, and then pressing the space bar on that page. If you are not using Google Chrome, you can play it [here](https://chromedino.com) instead.

Your game needs all of the following components of the original game:

- **A "dinosaur" character** (it may be just a rectangle) that stays stationary (in the x dimension) on the screen, but jumps when the player presses the space bar. Jumping should be implemented so that:
    - The dinosaur falls with gravity (it accelerates downward rather than falling at a constant speed).
    - Jumping gives the dinosaur sudden upward speed.
    - The dinosaur cannot jump while already in the air.
- **"Cactuses"** of a variety of sizes that are randomly spaced, and that cause the game to end if the dinosaur touches them (they may be just rectangles). Be sure that:
    - It must be possible for the dinosaur to jump over every cactus.
    - There are sometimes multiple cactuses on the screen at the same time.
- **A score** that increases as the game progresses.
- Pressing the space bar after a game over **restarts** the game.

Your game must also have at least one of the following additional components present in the original game:

- **A textured ground and background elements (like the clouds) that scroll**:
    - The ground should match the scroll speed of the cacti.
    - The background should scoll at a slower speed than the cacti.
    - The objects in the background must be randomly spaced in both the x dimension and the y dimension.

- **Game sprites**: 
    - Make your dinosaur look like a dinosaur and your cactuses look like cactuses. 
    - The dinosaur must have a running animation.

- **Airborn obstacles (like the pterodactyls) and ducking**: 
    - In addition to the cactuses, add in airborn enemies that also cause a game over when touched. 
    - They must be placed at random heights so that somtimes the dinosaur can get past them by jumping over them, somtimes it can get past by ducking under, and somtimes by simply running upright underneath. 
    - Ducking should make the dinosaur shorter, and is achieved by pressing the down arrow. 
    - The dinosaur should not get shorter while in the air.
    - It is ok if your pterodactyls are rectangles

- **Acceleration and night time**: 
    - Make the game more challenging by making the game accelerate as the score increases 
    - Make the game occasionally switch between day time and night time (happens after a score of 750 in the original game).


We won't be able to perform automated testing for this submission (we'll have course staff run it to grade it), but you should be able to tell if it is working on your own by playing the game you've created.

In implementing the game, avoid over-running the computer's resources.
In particular

-   Don't draw() a gamebox for a cactus (or pterodactyl or background image if you chose those optional features) until it is almost on the screen
-   Remove (or re-use) cactuses (or pterdactyls or background images) that go off the screen behind the player

Typically this means having some logic like this in your tick function:

````
if the left-most cactus is off the left side of the screen,
    move it to some random distance past the right side of the screen
````

That way you can have a small fixed number of cactus objects in Python
look like an endless stream of cactuses when playing the game


# Troubleshooting

The infinite scrolling example games might be a good starting point.

You don't need to implement anything beyond our required components and your selection of additional components, though you may implement multiple additional components (or extra features not mentioned in this document) as long as it's identifiable as the dinosaur game.

Many questions of the form "how do I do *X*" are answered in [The GameBox Docs](gamebox-summary.html)


Use gamebox, in a way similar to our examples from lecture and lab.
