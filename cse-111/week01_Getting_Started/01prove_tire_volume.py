#From: https://byui-cse.github.io/cse111-course/lesson01/prove.html
#By: Felipe dos Santos Belisário

"""
Assignment
Write a Python program named tire_volume.py that reads from the keyboard the three numbers for a tire and computes and outputs the volume of space inside that tire.

"""
import math 
#function
def volume(width, aspect_ratio, diameter):
    pi = math.pi
    w = width
    a = aspect_ratio
    d = diameter
    space_volume = (pi * (w ** 2) * a (w * a + 2540 * d))/10000000000
    return space_volume






user_width = float(input('Enter the width of the tire in mm (ex 205): '))
user_aspect_ratio = float(input('Enter the aspect ratio of the tire (ex 60): '))
user_diameter = float(input('Enter the diameter of the wheel in inches (ex 15): '))

print(f'The approximate volume is {volume(user_width, user_aspect_ratio, user_diameter)} liters')