#From: https://byui-cse.github.io/cse111-course/lesson01/check.html
#By: Felipe dos Santos Belisário

# Assignment
# Write a Python program named heart_rate.py that asks for a person's age and computes and outputs the slowest and fastest rates necessary to strengthen his heart. To start your program, copy and paste the following code into your program and use it as an outline as you write code. Note that in a Python program, a triple quoted string at the top of the file acts as a comment for the entire program.


"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

#Functions
def heart_rate(age):
    heart  = 220 - age
    return heart

def slowest():
    slowest_rate = (heart_rate()) * 0,65
    return slowest_rate

def fastest():
    fastest_rate = (heart_rate()) * 0,85
    return fastest_rate

user_age = int(input('Please enter your age: '))
heart_rate(user_age)
user_slowest = slowest()
user_fastest = fastest()
print(f'When you exercise to strengthen your heart, you should keep your heart rate between {user_slowest} and {user_fastest} beats per minute.')