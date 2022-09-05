#This program computes the area of a triangle, rectangle, and circle


import math


def areaTriangle(base, height):
    area = 1/2 * base * height
    return area

def areaRectangle(width, height):
    area= width * height
    return area

def areaCircle(radius):
    area= math.pi * radius**2
    return area

def main():
    print("This program computes the area of a triangle, rectangle, and circle.")
    print("")

    print("Triangle")
    base = float(input("Enter base:"))
    theight = float(input("Enter height:"))
    print("The area is=", "{:.2f}".format(areaTriangle(base, theight)))
    print("")

    print("Rectangle")
    width = float(input("Enter width:"))
    rheight = float(input("Enter height:"))
    print("The area is=", "{:.2f}".format(areaRectangle(width, rheight)))
    print("")

    print("Circle")
    radius = float(input("Enter radius:"))
    print("the area is=","{:.2f}".format(areaCircle(radius)))
    

main()
