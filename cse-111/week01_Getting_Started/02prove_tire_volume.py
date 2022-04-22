#From: https://byui-cse.github.io/cse111-course/lesson02/prove.html
#By: Felipe dos Santos Belisário

"""
The previous lesson's prove milestone required you to write a program named tire_volume.py that computes the approximate volume of air inside a tire. Add code near the end of that program that does the following:

1- Gets the current date from the computer's operating system.
2- Opens a text file named volumes.txt for appending.
3- Appends to the end of the volumes.txt file one line of text that contains the following five values:
    a. current date
    b. width of the tire
    c. aspect ratio of the tire
    d. diameter of the wheel
    e. volume of the tire 

"""
import math 
#function
def volume(width, aspect_ratio, diameter):
    pi = math.pi
    w = width
    a = aspect_ratio
    d = diameter
    space_volume = (pi * (w * w) * a * (w * a + 2540 * d))/10000000000
    return space_volume






user_width = float(input('Enter the width of the tire in mm (ex 205): '))
user_aspect_ratio = float(input('Enter the aspect ratio of the tire (ex 60): '))
user_diameter = float(input('Enter the diameter of the wheel in inches (ex 15): '))

print(f'\nThe approximate volume is {volume(user_width, user_aspect_ratio, user_diameter):.2f} liters')