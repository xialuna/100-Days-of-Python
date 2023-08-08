# Robot is randomly positioned inside the maze and can't see the walls, create a program that can help it escape
# Solved: World 1 to 3
def turn_right():
    for i in range(3):
        turn_left()
        
while not at_goal():
    if wall_in_front() and wall_on_right():
        turn_left()
    elif wall_in_front():
        turn_right()
    else:
        move()