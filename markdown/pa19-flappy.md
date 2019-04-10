---
title: "PA 19: flappybird.py"
...

# Task

In a file named `flappybird.py`, implement a [FlappyBird](https://flappybird.me/)-like game using pygame.

<!--
- Gravity causes continual downward acceleration, not downward speed or downward teleportation
    - i.e., the longer we go without pressing flap, the faster the bird is moving downward each frame
- A flap should be
    - accomplished by a single key press or mouse click
    - result in a sudden increase in upward velocity
    - not allow holding down the key or mouse to rocket upward
        - either require distinct clicks/presses for each flap
        - or have a held button/key only flap periodically
- The screen should scroll sideways at a steady pace, with the bird not moving horizontally relative to the screen
- The pillars should be
    - paired, with one coming from the top and another from the bottom at each point
    - with randomly-positioned openings, infinitely (not repeating or ending)
    - spaced so that winning is possible, but not necessarily easy
- Touching a pillar or the edge of the screen should end the game
- Score is a function of how long you survive, how many pillars you pass, or the equivalent
    - Score must be shown on-screen at the end of the game
    - Score may be shown continually or not, at your preference
- The window should be no more than 800×600 pixels, in order to fit on all TA's screens
-->

In particular,

-   There should be one kind if user input, a vertical flap action triggered by either a mouse click or the space bar (your choice) 
    - a flap is a burst of upward speed
    - rocketing up as long as you hold the key/button is not flapping
    - teleporting higher on the screen without passing through intermediate locations is not flapping
-   There should be momentum and gravity (acceleration, not constant-speed motion)
-   There should be scrolling obstacles (pillars) with openings at random heights
    - these should be matched top and bottom, like the original game
    - every opening should be on screen and large enough to fly through
    - no matter how long the user lasts, there should always be more pillars to pass through
-   Touching a pillar or exiting the screen should end the game
-   Score should be based on how long the player lasts before the game ends
-   When the game ends, the score should be displayed visually in the game screen
    - displaying it continually is OK, as long as it still shows up in the end
-   The window should be no more than 800×600 pixels, in order to fit on TA's screens

We won't be able to perform automated testing for this submission (we'll have course staff run it to grade it), but you should be able to tell if it is working on your own by playing the game you've created.

In implementing the game, avoid over-running the computer's resources.
In particular

-   Don't draw() a gamebox for a pilar until it is almost on the screen
-   Remove (or re-use) pilars that go off the screen behind the player

Typically this means having some logic like this in your tick function:

````
if the left-most pillar is off the left side of the screen,
    move it to some distance past the right side of the screen
    re-randomize its opening's vertical location
````

That way you can have a small fixed number of pillar objects in Python
look like an endless stream of pillars when playing the game


# Troubleshooting

The infinite scrolling example games (all sections had one) might be a good starting point.

You don't need to implement anything we don't ask for (e.g., animation, images, background images, etc), though you may as long as you still implement what we do ask for.

Many questions of the form "how do I do *X*" are answered in [The GameBox Docs](gamebox-summary.html)

If you do a web search for "Python flappybird" you'll find a lot of code that will get 0 points if submitted.
Use gamebox, in a way similar to our examples from lecture and lab.
