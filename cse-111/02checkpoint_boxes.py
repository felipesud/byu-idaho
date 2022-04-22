#From: https://byui-cse.github.io/cse111-course/lesson02/check.html
#By: Felipe dos Santos Belisário

"""
Assignment
A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping. Write a Python program named boxes.py that asks the user for two integers:

1- the number of manufactured items
2- the number of items that the user will pack per box

Your program must compute and print the number of boxes necessary to hold the items. This must be a whole number. Note that the last box may be packed with fewer items than the other boxes.

"""
import math
#Function
def boxes_total(items, items_per_box):
    boxes = items / items_per_box
    return math.ceil(boxes)






number_items = int(input('Enter the number of items: '))
items_per_box = int(input('Enter the number of items per box: '))

print(f'\nFor {number_items} items, packing {items_per_box} items in each box, you will need {boxes_total(number_items, items_per_box)} boxes.')
