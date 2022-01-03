# import os
import os

import operator


# package for reading CSV files
import csv
import statistics

csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # initialize counter
    votes = 0

    # initialize candidate list
    candidate_list = []

    # introduce counter to calculate the number of votes received
    for v in csvreader:
        candidate = v[2]
        votes += 1
        candidate_list.append(candidate)

    # test calculator and print value calculated
    print(f"Total Votes: {votes}")
    
    # initialize votes for each candidate
    candidateVotes = 0

    # get unique candidates
    unique_candidates = set(candidate_list)
    print("List of candidates:")
    print("\n".join(unique_candidates))


csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csvreader_sorted = sorted(csvreader, key = operator.itemgetter(2))

    votes = [0, 0, 0, 0]

    unique_candidates = set(candidate_list)
    candidates_sorted = sorted(unique_candidates, key = operator.itemgetter(0))
    print(candidates_sorted[0])

    # calculate the votes received for each candidate. use loop at candidate level and counter to tally.
    
     
    
    
    for name in unique_candidates:
        for row in csvreader_sorted:
            if name == row[2]:
                candidateVotes += 1
        print(name, candidateVotes)        
    #print(unique_candidates[2])

csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csvreader_sorted = sorted(csvreader, key = operator.itemgetter(2))

    # print(csvreader_sorted[2])
    # print(candidates_sorted[2])

    votes = [0, 0, 0, 0]
    election_list = []

    for i in range(len(unique_candidates)): 
        vote_index = int(i) - 1

        for row in csvreader_sorted:

            if candidates_sorted[vote_index] == row[2]:
                votes[vote_index] += 1
                name = candidates_sorted[vote_index]
    
        election_list.extend([name, votes[vote_index]])
                #print("This is a candidate print test: " + candidates_sorted[vote_index])

    print(name, votes[vote_index])  
    print(election_list)
    print(votes)






