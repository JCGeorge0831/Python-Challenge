# Importing the os module and the csv file
import os
import csv

csvpath = os.path.join ("..", "Pypoll", "Resources", "02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

# Storing votes data
votes = []

votes_for_khan = 0 
votes_for_correy = 0
votes_for_li = 0
votes_for_otooley = 0

# Appending results


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    
    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:

        # Finding total number of votes cast using append
        votes.append(row[0])
        poll_votes = len(votes)

        # Establishing the unique votes for each candidate using +=
        if row[2] == "Khan":
            votes_for_khan += 1
        elif row[2] == "Correy":
            votes_for_correy += 1
        elif row[2] == "Li":
            votes_for_li += 1
        elif row[2] == "O'Tooley": 
            votes_for_otooley += 1

# Finding the percentages of the votes for each candidate
khan_voting_percent = round(((votes_for_khan/poll_votes) * 100), 3)
correy_voting_percent = round(((votes_for_correy/poll_votes) * 100), 3)
li_voting_percent = round(((votes_for_li/poll_votes) * 100), 3)
otooley_voting_percent = round(((votes_for_otooley/poll_votes) * 100), 3)

# Making a dictionary of lists the candidate names and their votes
candidate_name = ["Khan", "Correy", "Li", "O'Tooley"]
pollvotes = [votes_for_khan, votes_for_correy, votes_for_li, votes_for_otooley]

# Zipping the candidate names and their votes together into tupules and creating a dictionary for the poll outcome
poll_outcome = dict(zip(candidate_name, pollvotes))

# Finding the winner of the election using the max function on the dictionary
key = max(poll_outcome, key=poll_outcome.get)

print(f"Election Results")
print(f"--------------------")
print(f"Total Votes: {poll_votes}")
print(f"--------------------")
print(f"Khan: {khan_voting_percent}% ({votes_for_khan})")
print(f"Correy: {correy_voting_percent}% ({votes_for_correy})")
print(f"Li: {li_voting_percent}% ({votes_for_li})")
print(f"O'Tooley: {otooley_voting_percent}% ({votes_for_otooley})")
print(f"-------------------")
print(f"Winner: {key}")

# Exporting results to a text file
results = []
results.append(f"Election Results")
results.append("\n")
results.append(f"--------------------")
results.append("\n")
results.append(f"Total Votes: {poll_votes}")
results.append("\n")
results.append(f"--------------------")
results.append("\n")
results.append(f"Khan: {khan_voting_percent}% ({votes_for_khan})")
results.append("\n")
results.append(f"Correy: {correy_voting_percent}% ({votes_for_correy})")
results.append("\n")
results.append(f"Li: {li_voting_percent}% ({votes_for_li})")
results.append("\n")
results.append(f"O'Tooley: {otooley_voting_percent}% ({votes_for_otooley})")
results.append("\n")
results.append(f"-------------------")
results.append("\n")
results.append(f"Winner: {key}")
print(results)

results_output = os.path.join("Election_Poll_Results.txt")

with open(results_output, "w")as txt_file:
    for results in results:
        txt_file.write(results)