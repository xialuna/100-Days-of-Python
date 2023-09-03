#documentation: https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen 
timmy = Turtle()
timmy.shape("turtle")
timmy.color("DeepPink");
timmy.forward(100);
#Screen - window in which turtle will show up
my_screen = Screen()
#canvheight = attribute in the Screen() 
print (my_screen.canvheight) #will output the height of the canvas fo the screen we created
my_screen.exitonclick() #allows program to continue running until we click








