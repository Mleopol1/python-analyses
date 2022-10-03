# CSV headers: Ballot ID, County, Candidate
# Import modules and create a path
import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

# Initialize variables
vote_total = 0
candidate_list = []
charles_votes = 0
diana_votes = 0
raymon_votes = 0

# Read CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Calculate total number of votes cast
    for row in csvreader:
        vote_total += 1
        
        # Create list of every candidate
        if row[2] not in candidate_list:
            candidate_list.append(row[2])

        # Total the votes for each candidate
        if row[2] == 'Charles Casper Stockham':
            charles_votes += 1
        elif row[2] == 'Diana DeGette':
            diana_votes += 1
        else: 
            raymon_votes += 1
        
        # Calculate percentages of votes for each candidate
        charles_percentage = round((charles_votes / vote_total) * 100, 3)
        diana_percentage = round((diana_votes / vote_total) * 100, 3)
        raymon_percentage = round((raymon_votes / vote_total) * 100, 3)

        # Determine the winner
        if charles_votes > diana_votes and charles_votes > raymon_votes:
            winner = 'Charles Casper Stockham'
        elif diana_votes > charles_votes and diana_votes > raymon_votes:
            winner = 'Diana DeGette'
        else:
            winner = 'Raymon Anthony Doane'

# Print final analysis
print(f"Election Results\n",
    f"-------------------------\n",
    f"Total Votes: {vote_total}\n",
    f"-------------------------\n",
    f"Charles Casper Stockham: {charles_percentage}% ({charles_votes})\n",
    f"Diana DeGette: {diana_percentage}% ({diana_votes})\n",
    f"Raymon Anthony Doane: {raymon_percentage}% ({raymon_votes})\n",
    f"-------------------------\n",
    f"Winner: {winner}\n",
    f"-------------------------")

# Export analysis to text file
folder = 'analysis'
file_name = 'output.txt'
path = os.path.join(folder, file_name)

file = open(path, 'w')
file.write(f"Election Results\n")
file.write(f"-------------------------\n")
file.write(f"Total Votes: {vote_total}\n")
file.write(f"-------------------------\n")
file.write(f"Charles Casper Stockham: {charles_percentage}% ({charles_votes})\n")
file.write(f"Diana DeGette: {diana_percentage}% ({diana_votes})\n")
file.write(f"Raymon Anthony Doane: {raymon_percentage}% ({raymon_votes})\n")
file.write(f"-------------------------\n")
file.write(f"Winner: {winner}\n")
file.write(f"-------------------------\n")
file.close()