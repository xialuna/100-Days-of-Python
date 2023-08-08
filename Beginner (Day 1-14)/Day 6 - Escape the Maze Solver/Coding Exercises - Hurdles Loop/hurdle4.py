#HURDLE FOUR: The height & number of hurdles and goal position changes each time this world is reloaded.
def turn_right():
    for i in range(3):
        turn_left()
        
def jump():
    while wall_on_right():
        move()   
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
  
while not at_goal():
    if wall_in_front():
        turn_left()
        jump()
        turn_left()
    else:
        move()