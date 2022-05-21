# 09 Prove Milestone: Text Files
# From: https://byui-cse.github.io/cse111-course/lesson09/prove.html
# By: Felipe dos Santos Belisário  - https://fsbelisario.com.br/

"""
Assignment
During this milestone, you will write half of a Python program named receipt.py that prints to the terminal window a receipt for a customer's grocery order. Specifically, by the end of this milestone, your program must contain at least these two functions:

1. main
2. read_dict
and must read and process these two CSV files:

-> The products.csv file is a catalog of all the products that the grocery store sells.
-> The request.csv file contains the items ordered by a customer.

"""
from calendar import WEDNESDAY
import csv
from datetime import datetime
from re import sub
KEY_COLUMN_INDEX = 0
NAME_INDEX = 1
PRICE_INDEX = 2
QUANTITY_INDEX = 1

# Get the current date and time from your computer's operating system and print the current date and time.
current_date_and_time = datetime.now(tz=None)
weekday = current_date_and_time.weekday()

def main():
    # Print the store name at the top of the receipt.
    print_elements('header')
    # Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError.
    try: 
        # Calls the read_dict function and stores the compound dictionary in a variable named products_dict.
        products_dict = read_dict("products.csv", KEY_COLUMN_INDEX)
        # print('All Products')
        # # Prints the products_dict.
        # print(products_dict)
    except FileNotFoundError as not_found_err:
        print('Error: missing file')
        print(not_found_err)
    except PermissionError as perm_err:
        print(perm_err)

    compound_list = []
    total_items = []
    every_prices = []
    subtotal = 0
    try:
        # print('\n Requested Items')
        # Opens the request.csv file for reading.
        # Contains a loop that reads and processes each row from the request.csv file. Within the body of the loop, your program must do the following for each row:
        # Use the requested product number to find the corresponding item in the products_dict.
        # Print the product name, requested quantity, and product price.
        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)
            for row_list in reader:
                if len(row_list) != 0:
                    compound_list.append(row_list) 
    except FileNotFoundError as not_found_err:
        print('Error: missing file')
        print(not_found_err)
    except PermissionError as perm_err:
        print(perm_err)
    try: 
        
        for codes in compound_list:
            code = codes[KEY_COLUMN_INDEX]
            quantity = int(codes[QUANTITY_INDEX])
         
            element_name = products_dict[code]
            name = element_name[NAME_INDEX]
            price = float(element_name[PRICE_INDEX])
            key = element_name[KEY_COLUMN_INDEX]
            
            total_items.append(quantity)
            every_prices.append(price)
        
            if code in key:
                print(f'{name}: {quantity} @ {price}')
    except FileNotFoundError as not_found_err:
        print('Error: missing file')
        print(not_found_err)
    except PermissionError as perm_err:
        print(perm_err)
#     Sum and print the number of ordered items.
# Sum and print the subtotal due.
# Compute and print the sales tax amount. Use 6% as the sales tax rate.
# Compute and print the total amount due.
    subtotal = [x*y for x,y in zip(total_items, every_prices)]
    sum_subtotal = sum(subtotal)
    total_to_pay = ((sum_subtotal * 0.06) + sum_subtotal)
    

    print(f'\nNumber of Items: {sum(total_items)}')
    print(f'Subtotal: {sum_subtotal:.02f}')
    print(f'Sales Tax: {(sum_subtotal * 0.06):.02f}')
   
    
    
    if weekday == 1 or weekday == 2:
        total = (total_to_pay * 0.01) + total_to_pay
        print(f'Total with 10% discount: {total:.02f}')
    else:
        print(f'Total: {total_to_pay:.02f}')
    #  Print a thank you message.   
    print_elements('footer')
        


           


        


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        next(reader)
        try:
            for row_list in reader:
                if len(row_list) != 0:
                    key = row_list[key_column_index]
                    dictionary[key] = row_list
        except KeyError as key_err:
            print(type(key_err).__name__, key_err)
    return dictionary


# Function to print some decorative elements
def print_elements(option): 
    break_line = "\n***********************************************\n"
    section_line = "***********************************************"
    header       = "*                AMAZING STORE                *"
    footer       = "*  Thank you for shopping at the Amazing Store!  *"

    if option == "header":
        print(f"{break_line}{header}{break_line}")
    elif option == "footer":
        print(f"{break_line}{footer}{break_line}")
        print(f"{current_date_and_time:%A %I:%M %p}")
    elif option == "break_line":
        print(f"{break_line}")
    elif option == "section_line":
        print(f"{section_line}")





if __name__ == "__main__":
    main()