# note: This is done with Reeborg's World
# HURDLE ONE: program knows how long the race is
def turn_right():
    for i in range(3):
        turn_left()
    
def jump():
    for i in range(2):
        move()
        turn_right()
    move()
    turn_left()

for i in range(6):       
    move()
    turn_left()
    jump()



