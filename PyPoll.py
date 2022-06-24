import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Resources","election_analysis.txt")
#election_data = open(file_to_load, 'r')
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:
    #print(election_data)
    #read the file object using the reader funciton
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = (float (votes)/ float(total_votes)) * 100
        #print(f"{candidate_name}: received {vote_percentage}% of the votes")
        if(votes>winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_name = candidate_name
        #print(winning_count)
        #print(winning_percentage)
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        for candidate in candidate_votes:
            winning_candidate_summary = (
            f"----------------------------------\n"
            f"Winner: {winning_name}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"--------------------------------------\n"
            )
    print(winning_candidate_summary)   
