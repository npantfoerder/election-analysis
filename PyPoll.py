# The data we need to retrieve:
# 1) The total number of votes cast
# 2) A complete list of candidates who recieved votes
# 3) The percentage of voes each candidate won
# 4) The total number of votes each candidate won
# 5) The winner of the election based on popular vote

# Import dependencies
import csv
import os

# Create a variable for a path to load the file
file_to_load = 'Resources/election_results.csv'
# Create a variable for a path to save the file 
file_to_save = 'analysis/election_analysis.txt'

# Open the election results and read the file
with open(file_to_load, 'r') as election_data:
    # To do: perform analytics
    file_reader = csv.reader(election_data)

    # Print the header ro
    headers = next(file_reader)
    print(headers)

# Open the file as a text file
with open(file_to_save, 'w') as txt_file:
    # Write data to the file
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson\n")