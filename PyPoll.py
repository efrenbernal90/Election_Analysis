# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total numbers of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies
import csv
import os

# Assign variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_results.txt")

# Initialize vote counter
total_votes = 0

# Declare list of potential candidates
candidate_options = [] 

# Create dictionay 
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total count.
        total_votes += 1
        
        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match existing candidate...
        if candidate_name not in candidate_options:
            # Add candidate name to list
            candidate_options.append(candidate_name)

            # Track candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add vote to candidate's count
        candidate_votes[candidate_name] += 1 
    
    # Determine percentage of votes each candidate by looping through the counts
    # Iterate through the list of candidates
    for candidate_name in candidate_votes:
        # Retrieve votes count of candidate.
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        #  To do: print out the winning candidate, vote count and percentage to
        #  terminal.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name 

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
