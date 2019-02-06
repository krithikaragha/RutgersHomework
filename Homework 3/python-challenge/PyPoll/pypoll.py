# Import the operating system package
import os

# Import a package to read in csv
import csv

# Import Counter
from collections import Counter

# Create the path for the file
# Save as Path = '../Resources/budget_data.csv'
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, 'r', errors='ignore') as fileHandle:
    reader = csv.reader(fileHandle)
    votes = []
    for row in reader:
        votes.append(row[2])
    
    total_votes = len(votes)
    print("Total votes: ", total_votes)
    vote_tally = Counter(votes)
    print(vote_tally)

    khan_votes = vote_tally['Khan']
    correy_votes = vote_tally['Correy']
    li_votes = vote_tally['Li']
    otooley_votes = vote_tally['O\'Tooley']

    votes_list = [khan_votes, correy_votes, li_votes, otooley_votes]
    winner_votes = max(votes_list)

    khan_perc = (khan_votes / total_votes) * 100
    correy_perc = (correy_votes / total_votes) * 100
    li_perc = (li_votes / total_votes) * 100
    otooley_perc = (otooley_votes / total_votes) * 100

    winner = ""
    for k, v in vote_tally.items():
        if v == winner_votes:
            winner = k

    # winner = max(khan_votes, correy_votes, li_votes, otooley_votes) 
    # print(winner)   

    print("---------------------------------------------")
    print("Election Results")
    print("---------------------------------------------")
    print("Total Votes: ", total_votes)
    print("---------------------------------------------")
    print("Khan:         ", round(khan_perc, 2), "%", "(", khan_votes, ")")
    print("Correy:       ", round(correy_perc, 2), "%", "(", correy_votes, ")")
    print("Li:           ", round(li_perc, 2), "%", "(", li_votes, ")")
    print("O'Tooley:     ", round(otooley_perc, 2), "%", "(", otooley_votes, ")")
    print("---------------------------------------------")
    print("Winner: ", winner)
    print("---------------------------------------------")

f = open("results.txt", "w")
f.write("Election Results\n")
f.write("---------------------------------------------\n")
f.write("Total Votes: ")
f.write(str(total_votes))
f.write("\n")
f.write("---------------------------------------------\n")
f.write("Khan:         ")
f.write(str(round(khan_perc, 2)))
f.write("%   (")
f.write(str(khan_votes))
f.write(")")
f.write("\n")
f.write("Correy:         ")
f.write(str(round(correy_perc, 2)))
f.write("%   (")
f.write(str(correy_votes))
f.write(")")
f.write("\n")
f.write("Li:         ")
f.write(str(round(li_perc, 2)))
f.write("%   (")
f.write(str(li_votes))
f.write(")")
f.write("\n")
f.write("O'Tooley:         ")
f.write((str(round(otooley_perc, 2))))
f.write("%   (")
f.write(str(otooley_votes))
f.write(")")
