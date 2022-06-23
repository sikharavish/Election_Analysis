import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
#election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:
    #print(election_data)
    #read the file object using the reader funciton
    file_reader = csv.reader(election_data)
    for row in file_reader:
       print(row)