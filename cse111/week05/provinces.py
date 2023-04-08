# 09 Checkpoint: Text Files
# From: https://byui-cse.github.io/cse111-course/lesson09/check.html
# By: Felipe dos Santos Belisário

"""
Assignment
You must do the following to setup VS Code so that your program can read from a text file:

1. Download the provinces.txt file and save it in the same folder where you will save your Python program.
2. Using VS Code, open the folder where you saved the provinces.txt file by doing the following:
    *On a computer running the Mac OSX operating system:
        a. Click the "File" menu, then "Open..."
        b. Find and select the folder where you saved the provinces.txt file.
        c. Click the "Open" button.
    *On a computer running the Windows operating system:
        a. Click the "File" menu, then "Open Folder..."
        b. Find and select the folder where you saved the provinces.txt file.
        c. Click the "Select Folder" button.

Now that you have correctly setup VS Code so that your program can read the provinces.txt file, open that file in VS Code and examine it. 
Notice that the file contains a list of names of Canadian Provinces. 
Notice also that the file contains "AB" several times which is an abbreviation for Alberta.

Write a Python program named provinces.py that reads the contents of provinces.txt into a list and then modifies the list. 
Your program must do the following:

1. Open the provinces.txt file for reading.
2. Read the contents of the file into a list where each line of text in the file is stored in a separate element in the list.
3. Print the entire list.
4. Remove the first element from the list.
5. Remove the last element from the list.
6. Replace all occurrences of "AB" in the list with "Alberta".
7. Count the number of elements that are "Alberta" and print that number.


"""
def main():
    # Read the contents of a text file named
    # provinces.txt into a list named provinces_list.
    provinces_list = read_list("provinces.txt")

    # As a debugging aid, print the entire list.
    print(provinces_list)

    # Remove the first element from the list.
    provinces_list.pop(0)
    #print(provinces_list)

    # Remove the last element from the list.
    provinces_list.pop()
    #print(provinces_list)

    # Replace all occurrrences of "AB" with "Alberta".
    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"
    #print(provinces_list)

    # Call the list.count method which will count the
    # number of times that Alberta appears in the list.
    count = provinces_list.count("Alberta")

    print()
    print(f"Alberta occurs {count} times in the modified list.")


def read_list(filename):
    """Read the contents of a text file into a list
    and return the list that contains the lines of text.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list that will store
    # the lines of text from the text file.
    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)

    # Return the list that contains the lines of text.
    return text_list


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()