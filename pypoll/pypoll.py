import os
import csv


with open("c:/Users/Brian/Desktop/homework3/election_data.csv","r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    output = []
    input = []
    for row in csvreader:
        input.append(row[2])
    print("Election Results")
    print("----------------------")
    print(f'Total Votes: {len(input)}')
    print("----------------------")
    for x in input:
        if x not in output:
            output.append(x)
    #print(output)  good so far
    vote_totals = []
    i = 0
    vote_counter = 0
    winner = 0
    winner_votes = 0
    while i < len(output):
        j = 0
        while j < len(input):
            if output[i] == input[j]:
                vote_counter = vote_counter +1
            j = j + 1
        #print(output[i])
        #print(vote_counter)
        vote_totals.append(vote_counter)#might not need
        #Find %:
        percent = vote_counter/len(input) * 100
        percent = str(round(percent, 3))
        print(f'{output[i]}: {percent}% ({vote_totals[i]})')
        ###if winner_votes < vote_totals[i]
        vote_counter = 0
        i = i + 1
    #print(vote_totals)#testing
    #find winner
    winner = 0
    winner_votes = 0
    k = 0
    while k < len(output):
        if winner_votes < vote_totals[k]:
            winner_votes = vote_totals[k]
            winner = k
        k = k + 1

    print("----------------------")
    print(f'WINNER: {output[winner]}')
    