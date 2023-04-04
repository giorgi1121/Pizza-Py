#import modules
from tabulate import tabulate
import csv
import sys

#main function checks if file exists and calls grid function with argument of file name
def main():
    check_command_lines()

    try:
        arg = sys.argv[1]

        print(grid(arg))

    except FileNotFoundError:
        sys.exit("File does not exist")


#grid function returns file in table format
def grid(arg):
    menu = []
    with open(arg) as file:
        reader = csv.reader(file)
        for row in reader:
            menu.append(row)
        return tabulate(menu, headers= "firstrow", tablefmt= "grid")

#check_command_lines function checks errors
def check_command_lines():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith("csv"):
        sys.exit("Not a CSV format")

main()
