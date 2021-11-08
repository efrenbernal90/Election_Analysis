counties_dict = {"Arapahoe": 422829, 
                "Denver": 463353, 
                "Jefferson": 432438}

for keys in counties_dict:
        print(keys)

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("what is the total votes in the election? "))
print(f"I receieved {my_votes / total_votes *100}% of the total votes.")