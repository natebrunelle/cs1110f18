def travel_time(distance, speed):
    if (distance < 0):
        raise ValueError("travel_time distance cannot be negative")
    if (speed < 0):
        raise ValueError("travel_time speed cannot be negative")
    return distance / speed

finished = False;
while(not finished):
    distance = 0;
    while distance == 0:
        try:
            distance = float(input("Enter a distance to travel in miles:"))
        except ValueError:
            print("You didn't enter a number. Please try again!")

    speed = 0;
    while speed == 0:
            try:
                speed = float(input("Enter a speed in miles per hour:"))
            except ValueError:
                print("You didn't enter a number. Please try again!")

    try:
        print("Your journey will take ", travel_time(distance,speed), " hours")
        finished = True
    except ValueError:
        print("Uh oh, looks like you entered a negative number. Try again!")