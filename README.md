# PyPoll with Python

## Overview of Election Audit
Tom, a Colorado Board of Elections employee, needs assitance with the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of counties that had a turnout.
3. Calculate the voter turnout for each county.
4. Calculate the percentage of votes each county cast.
5. Determine the county with the highest turnout.
6. Get a complete list of candidates who recieved votes.
7. Calculate the total number of votes each candidate recieved.
8. Calculate the percentage of votes each candidate won.
9. Determine the winner of the election based on popular vote.

Tom's manager wants to automate the process of generating a vote count report using Python.

## Election-Audit Results
The analysis of the election shows that:
- There were 369,711 total votes cast in this congressional election.
- The county results for the precinct:
  - Jefferson cast 10.5% of the vote and 38,855 votes.
  - Denver cast 82.8% of the vote and 306,055 votes.
  - Arapahoe cast 6.7% of the vote and 24,801.
- Denver county had the largest number of votes.
- The candidate results were:
  - Charles Casper Stockham recieved 23.0% of the vote and 85,213 votes.
  - Diana DeGette recieved 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane recieved 3.1% of the vote and 11,606 votes.
- The winner of the election was Diana DeGette, who recieved 73.8% of the vote and 272,892 votes.

See the output of the code below:

<img src="https://github.com/npantfoerder/election-analysis/blob/master/analysis/Code_Output.png" width="350">

## Election-Audit Summary
I propose that the election commission can use the PyPoll_Challenge.py script, with some modifications, for other elections. Currently, the program is written to analyze the election_results.csv file by iterating through each row and reading the data in the second and third columns, 'County' and 'Candidate', in order to calculate and print the results. There are many different ways in which this code can be altered to be used for future elections.

For example, the program can be modified to iterate through the header row and determine which column to read data from. Then files with columns that are arranged in a different order will be analyzed accordingly and the programmer will no longer have to inspect the data to ensure that the code is reading the correct columns. Another possiblity is to read data from additional columns in order to calculate and print further results. This is useful for files containing more information, such as the type of ballot or the date that the vote was cast. 

### Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.47.2
