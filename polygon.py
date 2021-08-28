import math
import turtle

print ("Hello, this is an application that does some functions related to regular Polygons.")

print ("Choose from these options:")
print ("[1] Calculate the area of a regular polygon")
print ("[2] Calculate the perimeter of a regular polygon")
print ("[3] Calculate the measurement of this polygon's single angle")
print ("[4] Draw a regular polygon")
Choice = int(input("Choose number of program to execute: "))

Sides_Number = int(input("Input number of sides: "))
Side_Length = float(input("Input the lenght of the side: "))

Polygon_Perimeter = Sides_Number * Side_Length
Polygon_Apothem = Side_Length / (2 * math.tan(math.pi / Sides_Number))
Polygon_Area = Polygon_Perimeter * Polygon_Apothem / 2
Angle_Measure = 2 * 180 / Sides_Number

def Area_Func():
    print("Polygon Area = " + str(round(Polygon_Area, 3)))

def Perimeter_Func():
    print("Polygon perimeter = " + str(round(Polygon_Perimeter, 3)))

def Angle_Func():
    print("The measurement of every single angle = " + str(round(Angle_Measure, 3)))

def Draw_Func():
    for _ in range(Sides_Number):
        turtle.forward(90)
        turtle.right(360 / Sides_Number)
    turtle.done()


if Choice == 1:
    Area_Func()
    
elif Choice == 2:
    Perimeter_Func()

elif Choice == 3:
    Angle_Func()

elif Choice == 4:
    Draw_Func()

else: print ("Wrong choice...")
