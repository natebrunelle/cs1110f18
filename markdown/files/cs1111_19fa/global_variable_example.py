import random

# 4 players
# each player rolls a dice (dice face is the returning value from get_random_number())
# use global variable to keep track of each player's accumulate score

# declare some global variables
score1 = 0
score2, score3 = 0, 0  # declare multiple variables in one line
score4 = 0


def roll_dice(player):
    global score1, score2, score3, score4  # tell python you want to use the global versions
                                           # of these variables
    if (player == 1):
        score1 += random.randint(1, 6)
    if (player == 2):
        score2 += random.randint(1, 6)
    if (player == 3):
        score3 += random.randint(1, 6)
    if (player == 4):
        score4 += random.randint(1, 6)

roll_dice(1)      # player1
roll_dice(2)      # player2
roll_dice(3)      # player3
roll_dice(4)      # player4

print("first round", score1, ":", score2, ":", score3, ":", score4)

roll_dice(1)      # player1
roll_dice(2)      # player2
roll_dice(3)      # player3
roll_dice(4)      # player4

print("second round " + str(score1) + " : " + str(score2) + " : " + str(score3) + " : " + str(score4))

roll_dice(1)      # player1
roll_dice(2)      # player2
roll_dice(3)      # player3
roll_dice(4)      # player4

print("finals scores " + str(score1) + " : " + str(score2) + " : " + str(score3) + " : " + str(score4))
