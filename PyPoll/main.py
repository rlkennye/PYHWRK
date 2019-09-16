##################################################
## {This program computes the following info on a dataset:
##	The total number of votes cast
##	A complete list of candidates who received votes
##	The percentage of votes each candidate won
##	The total number of votes each candidate won
##	The winner of the election based on popular vote.
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
##      ../Resources/election_data.csv
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
C_Khan = 0
C_Correy = 0
C_Li = 0
C_OTooley = 0
my_dict = {}
##################################################
# Define function 
def perc_count(C_Name, C_Votes, Total_Votes):
    perc = float(C_Votes / (Total_Votes)) * 100
    new_perc = round(perc, 3)
    print(C_Name + str(new_perc) + "%" + "  " +"(" + str(C_Votes) + ")")

##############################
## Main Program begins here ##
##############################

# Specify the file to read from
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# Get total votes cast with sum function
with open(csvpath, 'r') as file_handler:
    row_count = sum(1 for row in file_handler)

# Get total votes for each Candidate 
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Add up all Profit - Losses
    for row in csvreader:
        if (row[2]) == "Khan":
            C_Khan += 1
        elif (row[2]) == "Correy":
            C_Correy += 1
        elif (row[2]) == "Li":
            C_Li += 1
        else:
            C_OTooley += 1
my_dict = {C_Khan:'Khan',C_Correy:'Correy',C_Li:'Li',C_OTooley:'O\'Tooley'}

# Print to Screen
print(" ")
print("Election Results")
print("---------------------------")
print("Total Votes: " + str(row_count - 1)) 
print("---------------------------")
perc_count("Khan: ",C_Khan,row_count)
perc_count("Correy: ",C_Correy,row_count)
perc_count("Li: ",C_Li,row_count)
perc_count("O\'Tooley: ",C_OTooley,row_count)
print("---------------------------")
maximum = max(my_dict)
print("Winner: ", my_dict[maximum] )
print("---------------------------")
print(" ")

# Print to Text file
orig_stdout = sys.stdout
f = open('main_output.txt', 'w')
sys.stdout = f

print(" ")
print("Election Results")
print("---------------------------")
print("Total Votes: " + str(row_count - 1)) 
print("---------------------------")
perc_count("Khan: ",C_Khan,row_count)
perc_count("Correy: ",C_Correy,row_count)
perc_count("Li: ",C_Li,row_count)
perc_count("O\'Tooley: ",C_OTooley,row_count)
print("---------------------------")
maximum = max(my_dict)
print("Winner: ", my_dict[maximum] )
print("---------------------------")
print(" ")


sys.stdout = orig_stdout
f.close()