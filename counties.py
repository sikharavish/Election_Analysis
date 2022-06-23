""" #python3
counties = ["a", "Denver", "c"]
print(counties)
if counties[1] == 'Denver':
    print(counties[1]) """
""" my_votes = int(input("How many votes did you get in the election"))
# total number of votes
total_votes = int(input("How many votes are there in the election?"))
percentage_votes = (my_votes/ total_votes) * 100
print("I received" + str(percentage_votes)+ " % of the total votes") """
counties = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties.items():
    print(county,"county has", str(voters), "registered voters")
