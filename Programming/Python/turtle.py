from math import*
from turtle import*

print(pow(10,2))
print(sqrt(100))

def koordinatenkreuz():
    for i in range(4):
        setheading(i*90)
        forward(100)
        home()

koordinatenkreuz()
for i in range(-10,11,2):
    y = pow(i,2)
    goto(10*i,y)