##################################################
## {This program computes the following info on a dataset:
## The total number of months included in the dataset
## The net total amount of "Profit/Losses" over the entire period
## The average of the changes in "Profit/Losses" over the entire period
## The greatest increase in profits (date and amount) over the entire period
## The greatest decrease in losses (date and amount) over the entire period}
##################################################
## {License_info}
##################################################
## Author: Ricardo L Kenny
## Copyright: Copyright {2019}, {main.py}
## Credits: BootCampSpot Team
## License: N/A
## Version: Python 3.7.3
## Mmaintainer: {maintainer}
## Email: RicardoLKenny@gmail.com
## Status: production version
##################################################

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# My Functions
# def 

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
with open(csvpath, 'r') as file_handler:
    lines = file_handler.read()
    print(lines)

# Begin
print("Financial Analysis")
print("---------------------------")
print("Total Months: ")
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
