# import os
import os

# import operator to allow sort function
import operator


# package for reading CSV files
import csv


csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # initialize counter to calculate total votes
    votes = 0

    # initialize candidate list
    candidate_list = []

    # introduce for loop to calculate the total number of votes received
    for v in csvreader:
        candidate = v[2]
        votes += 1
        # create list of candidates with duplicate values
        candidate_list.append(candidate)

    
    # get unique candidates with set function
    unique_candidates = set(candidate_list)


csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csvreader_sorted = sorted(csvreader, key = operator.itemgetter(2))

   

    unique_candidates = set(candidate_list)
    candidates_sorted = sorted(unique_candidates, key = operator.itemgetter(0))

    vote_list = [0, 0, 0, 0]
    election_print = []
    winner = []
    vote_count = []
    most_votes = 0
    candidates_votes = []
    unlist = []
    desired_rows_formatted = []

    #calculate votes for each candidate and the percent of votes. Also begin construction of output text by creating variables.
    for i in range(len(unique_candidates)): 
        vote_index = int(i) - 1

        for row in csvreader_sorted:

            if candidates_sorted[vote_index] == row[2]:
                vote_list[vote_index] += 1
                name = candidates_sorted[vote_index]
                vote_percent = vote_list[vote_index]/votes
                print_candidate = name + ": " + str("{:.3%}".format(vote_percent)) + " (" + str("{:,.0f}".format(vote_list[vote_index])) + ")"
                titleRow = "Election Results"
                splitRow = "-------------------------------------"
                totalVotes = "Total Votes: " + str(votes)
        winner.append(name)
        vote_count.append(vote_list[vote_index])
        candidates_votes.extend([[name, vote_list[vote_index]]])
        election_print.append(print_candidate)

    max_vote  = max(vote_count)

    for row in candidates_votes:
        if row[1] == max_vote:
            elected_official = row[0]
            print_elected = "Winner: " + elected_official


# print rows required for exercise with proper formatting
titleRow = "Election Results"
totalVotes = "Total Votes: " + str("{:,.0f}".format(votes))

desired_rows = [titleRow, splitRow, totalVotes, splitRow]

for x in election_print:
    desired_rows.append(x)

desired_rows.append(splitRow)
desired_rows.append(print_elected)
desired_rows.append(splitRow)  

desired_rows_formatted = "\n".join(desired_rows)
print(desired_rows_formatted)

# write desired output to text file
output_path = "PyPoll/Resources/pypoll_data.txt"

with open(output_path, "w") as text:

    text.writelines(desired_rows_formatted)