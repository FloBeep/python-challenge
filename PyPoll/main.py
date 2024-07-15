# Import file

import os
import csv

election_data = os.path.join('Resources', 'election_data.csv')

# Set up variables
candidates = []
num_votes = []
percent_votes = []
total_votes = 0

# Open csv file and store in variable

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

# Iterate through rows and add to our vote counter

    for row in csvreader:
        
        total_votes += 1 

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    # Calculte percent of votes received
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    # Find winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

# Print results in code

print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Export to txt file and write

output_file = os.path.join('Elections_Results.txt')

with open(output_file,"w") as file:

    file.write("Election Results")
    file.write("\n")
    file.write("--------------------------")
    file.write("\n")
    file.write(f"Total Votes: {str(total_votes)}")
    file.write("\n")
    file.write("--------------------------")
    file.write("\n")
    for i in range(len(candidates)):
        line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
        file.write('{}\n'.format(line))
    file.write("--------------------------")
    file.write("\n")
    file.write(f"Winner: {str(winning_candidate)}")
    file.write("\n")
    file.write("--------------------------")
    file.write("\n")