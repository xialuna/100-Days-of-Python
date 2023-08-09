#Instructions:
# 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
import math

def paint_calc(height,width,cover):
    result = math.ceil((height * width)/cover)
    return result

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

print("You'll need %d cans of paint" %paint_calc(test_h, test_w, coverage))