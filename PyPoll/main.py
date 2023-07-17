import os
import csv

# Path to data
election_csv = os.path.join('Resources', 'election_data.csv')
# Path to export data into the analysis folder
output_path = os.path.join('Analysis', 'election_analysis.txt')

# Read CSV file
with open(election_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Ballot ID,County,Candidate .
    header = next(csvreader)

    # Initialize vars
    totalVotes = 0
    candidates = {}
    
    # Loop through data
    for row in csvreader:
        # Increment the total number of votes
        totalVotes += 1
        
        candidate_name = row[2]
        
        # Check if the candidate exists in the dictionary
        # If candidate doesn't exist in the dictionary, then add them with vote count of 1
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1
            
# Calculates winner
def find_winner(candidate_votes):
    max_votes = 0
    winner = ""
    for candidate, votes in candidate_votes.items():
        if votes > max_votes:
            max_votes = votes
            winner = candidate
    return winner

## Print the Election Results
print()
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")

# Calculate and print the results for each candidate
for candidate, vote_count in candidates.items():
    percentage = (vote_count / totalVotes) * 100
    print(f"{candidate}: {percentage:.3f}% ({vote_count})")

# Calculates the winner based on the candidate with the maximum votes
winner = find_winner(candidates)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
print()

## Export into election_analysis.txt
with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {totalVotes}\n")
    txtfile.write("-------------------------\n")

    # Calculate and write the results for each candidate
    for candidate, vote_count in candidates.items():
        percentage = (vote_count / totalVotes) * 100
        txtfile.write(f"{candidate}: {percentage:.3f}% ({vote_count})\n")
    
    # Calculates the winner based on the candidate with the maximum votes
    winner = find_winner(candidates)
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")