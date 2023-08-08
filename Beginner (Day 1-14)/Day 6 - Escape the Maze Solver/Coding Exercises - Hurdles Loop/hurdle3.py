# HURDLE THREE: The number of hurdles and goal position changes each time this world is reloaded.
def turn_right():
    for i in range(3):
        turn_left()
    
def jump():
    turn_left()
    for i in range(2):
        move()
        turn_right()
    move()
    turn_left()
    
while not at_goal():
    if front_is_clear(): 
        move()
    else:
        jump()