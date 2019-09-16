##################################################
## {This program computes the following info on a dataset:
## The total number of months included in the dataset
## The net total amount of "Profit/Losses" over the entire period
## The average of the changes in "Profit/Losses" over the entire period
## The greatest increase in profits (date and amount) over the entire period
## The greatest decrease in losses (date and amount) over the entire period}
##################################################
## {License_info} N/A
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
## Input File(s): 
##      ../Resources/budget_data.csv
##################################################
## Output File(s): 
##       main_output.txt
##################################################
## imports
import os
import csv
import sys
##################################################
## Variables
row_count = 0
column_count = 0
diff_count = 0
avg_change = 0
average_change = 0
top_row = 0
bottom_row_minus_top = 0
saved_difference = 0
profit_losses = 0
my_dict = {}
############################

##############################
## Main Program begins here ##
##############################

# Specify the file to read from
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Get total months with sum function
with open(csvpath, 'r') as file_handler:
    row_count = sum(1 for row in file_handler)

# Get total count of column Profit - Losses 
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Add up all Profit - Losses
    for row in csvreader:
        if column_count == 0: # first time in the loop
            profit_losses = int(row[1])
        else:
            profit_losses = int(profit_losses) + int(row[1])
        column_count += 1 # next row to be added
        
# Get total count of average change
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Compute avg_change
    for row in csvreader:

        if diff_count == 0:
            top_row = int(row[1])
        else:
            bottom_row_minus_top = (int(row[1])) - top_row
            top_row = int(row[1])
            saved_difference = saved_difference + bottom_row_minus_top
            my_dict[bottom_row_minus_top] = (row[0])
            avg_change = (saved_difference / (row_count - 2))
        diff_count += 1

# round to 2 decimal points       
average_change = round(avg_change, 2)    
    
# Print to Screen
print(" ")
print("Financial Analysis")
print("---------------------------")
print("Total Months: " + str(row_count - 1)) 
print("Total: $" + str(profit_losses))
print("Average  Change: $" + str(average_change)) 
maximum = max(my_dict)
print("Greatest Increase in Profits: ", my_dict[maximum], maximum)
minimum = min(my_dict)
print("Greatest Decrease in Profits: ", my_dict[minimum], minimum)
print(" ")

# Print to Text file
orig_stdout = sys.stdout
f = open('main_output.txt', 'w')
sys.stdout = f

print(" ")
print("Financial Analysis")
print("---------------------------")
print("Total Months: " + str(row_count - 1)) 
print("Total: $" + str(profit_losses))
print("Average  Change: $" + str(average_change)) 
maximum = max(my_dict)
print("Greatest Increase in Profits: ", my_dict[maximum], maximum)
minimum = min(my_dict)
print("Greatest Decrease in Profits: ", my_dict[minimum], minimum)
print(" ")

sys.stdout = orig_stdout
f.close()