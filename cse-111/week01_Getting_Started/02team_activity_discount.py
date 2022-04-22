#From: https://byui-cse.github.io/cse111-course/lesson02/teach.html
#By: Felipe dos Santos Belisário

"""
Assignment
Write a Python program named discount.py that gets a customer's subtotal as input and gets the current day of the week from your computer's operating system. Your program must not ask the user to enter the day of the week. Instead, it must get the day of the week from your computer's operating system.

If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10% from the subtotal. Your program must then compute the total amount due by adding sales tax of 6% to the subtotal. Your program must print the discount amount if applicable, the sales tax amount, and the total amount due.


"""
#Find the day of the week
#Module function
from datetime import datetime

current_date_and_time = datetime.now()

day_of_week = current_date_and_time.weekday()
# print(day_of_week)
user_subtotal = 0

#function to calculate the discount
def get_discount(day, subtotal):
    if subtotal >= 50 and (day == 1 or day == 2):
        new_subtotal = subtotal - (subtotal * 0.10)
    else:
        new_subtotal = subtotal
    return new_subtotal

#function to calculate sales tax amount
def get_sales_tax():
    subtotal = get_discount(day_of_week, user_subtotal)
    tax_amount = subtotal * 0.06
    return tax_amount 

#function to calculate the new subtotal with taxes
def new_subtotal_taxed():
    discounted = get_discount(day_of_week, user_subtotal)
    taxes = get_sales_tax()
    taxed_subtotal = discounted + taxes
    return taxed_subtotal


price = 1
#Built-in functions
while price != 0:
    price = float(input('Please, enter the price: '))
    if price != 0:
        quantity = float(input('Please enter the quantity: '))
        user_subtotal += price * quantity


if user_subtotal < 50 and (day_of_week == 1 or day_of_week == 2): 
    needed = 50 - user_subtotal
    print(f'To receive the discount, add {needed:.2f} to your order')

print(f'Sales tax amount: {get_sales_tax():.2f} ')
print(f'Total: {new_subtotal_taxed():.2f}')
