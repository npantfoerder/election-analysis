# The data we need to retrieve:
# 1) The total number of votes cast
# 2) A complete list of candidates who recieved votes
# 3) The percentage of voes each candidate won
# 4) The total number of votes each candidate won
# 5) The winner of the election based on popular vote

import csv
import os

# Assign a variable for the file to laod and the path
file_to_load = 'Resources/election_results.csv'
#file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file
with open(file_to_load, 'r') as election_data:
    # To do: perform analytics
    print(election_data)

# Create a filename variable to a direct path to the file 
file_to_save = 'analysis/election_analysis.txt'

# Write data to the file
with open(file_to_save, 'w') as out_file:
    # Write data to the file
    out_file.write("Hello World")
    