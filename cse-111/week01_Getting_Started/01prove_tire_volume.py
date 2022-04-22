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
    space_volume = (pi * (w * w) * a * (w * a + 2540 * d))/10000000000
    return space_volume






text_width = input('Enter the width of the tire in mm (ex 205): ')
text_aspect_ratio = input('Enter the aspect ratio of the tire (ex 60): ')
text_diameter = input('Enter the diameter of the wheel in inches (ex 15): ')
user_width = float(text_width)
user_aspect_ratio = float(text_aspect_ratio)
user_diameter = float(text_diameter)
user_volume = volume(user_width, user_aspect_ratio, user_diameter)
print(f'The approximate volume is {user_volume} liters')