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

# Initialize total vote counter
total_votes = 0
# Initialize list of candadites
candidate_options = []
# Initialize dictionary to contain candidates and votes
candidate_votes = {}

# Open the election results and read the file
with open(file_to_load, 'r') as election_data:
    # To do: perform analytics
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # Find the total number of votes
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        # Add candidate names to list and dictionary
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percent = 0

# Determine the percentage of votes for each candidate
for candidate_name in candidate_votes:
    # Get the vote count for each candidate
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes
    vote_percent = votes / total_votes * 100
    # Print the candidate name,  percentage of votes, and vote count
    print(f"{candidate_name}: {vote_percent:.1f}% ({votes:,})\n")
    # Determine winning candidate and vote count
    if votes > winning_count and vote_percent > winning_percent:
        winning_candidate = candidate_name
        winning_count = votes
        winning_percent = vote_percent

# Intialize and print winning candidate summary
winning_candidate_summary = (
    f"---------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percent:.1f}%\n"
    f"---------------------------\n"
)
print(winning_candidate_summary)

# Open the file as a text file
with open(file_to_save, 'w') as txt_file:
    # Write data to the file
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson\n")