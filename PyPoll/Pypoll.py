import os
import csv

# Path to the csv file
csvpath = os.path.join('election_data.csv')

# Create variables
total_votes = 0
candidate_votes = {}
candidates= []
CharlesCasperStockham_votes= 0
DianaDeGette_votes = 0
RaymonAnthonyDoane_votes = 0
winner = ""
winner_votes = 0
candidate_and_votes= {} 

# Read the election_data.csv file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row
    csv_header = next(csvreader)

    #setting up the  Loop through the rows in the CSV file
    for row in csvreader:
        # setting up votes calculation 
        total_votes += 1

 # If candidate is not on the list, add candidate to the list
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate]+=1
# Calculate the percentage of votes per candidate
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Determine the winner based on popular vote
for candidate, votes in candidate_votes.items():
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes
        
print(candidate_votes)
print(candidate_votes["Charles Casper Stockham"])
print(candidate_votes["Diana DeGette"])
print(candidate_votes["Raymon Anthony Doane"])

# Printing the analysis
# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


# Export a text file with the results
output_path = os.path.join("election_results.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate in candidates:
        txtfile.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
