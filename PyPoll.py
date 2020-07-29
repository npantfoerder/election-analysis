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
# Initialize list of the candadite options
candidate_options = []
# Initialize dictionary to contain candidate vote counts
candidate_votes = {}
# Initialize winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percent = 0

# Open the election results and read the file
with open(file_to_load, 'r') as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
    # Iterate through each row in the CSV file
    for row in file_reader:
        # Increment the total vote count
        total_votes += 1
        # Get the candidate name
        candidate_name = row[2]
        # Add candidate names to list and dictionary
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        # Increment the candidate's vote count
        candidate_votes[candidate_name] += 1

# Save the results to a text file
with open(file_to_save, 'w') as txt_file:
    # Declare and print the total vote count 
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
    )
    print(election_results, end="")
    # Save the total vote count to the file
    txt_file.write(election_results)

    # Iterate through each candidate
    for candidate_name in candidate_votes:
        # Get the candidate's vote count
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percent = votes / total_votes * 100
        # Declare and print the candidate, their vote count, and percentage
        candidate_results = f"{candidate_name}: {vote_percent:.1f}% ({votes:,})\n"
        print(candidate_results, end="")
        # Save the candidate results to the file
        txt_file.write(candidate_results)
        # Determine winning candidate, vote count, and percentage
        if votes > winning_count and vote_percent > winning_percent:
            winning_candidate = candidate_name
            winning_count = votes
            winning_percent = vote_percent

    # Declare and print the winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percent:.1f}%\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary, end="")
    # Save the winning candidate summary to the file
    txt_file.write(winning_candidate_summary)