# HURDLE TWO: The goal position changes each time this world is reloaded.
def turn_right():
    for i in range(3):
        turn_left()
    
def jump():
    for i in range(2):
        move()
        turn_right()
    move()
    turn_left()
    
#VERSION 1:
while at_goal() == False:
    move()
    turn_left()
    jump()

#VERSION 2:
while not at_goal():
    move()
    turn_left()
    jump()
