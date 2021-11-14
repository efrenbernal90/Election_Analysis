# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit congressional election.
The voter turnout for each county.
1. Calculate the total number of votes cast.
2. Percentage of voters per total vote count. 
3. The county with the highest turnout.
4. Get a complete list of candidates who received votes.
5. Calculate the total number of votes each candidate received.
6. Calculate the percentage of votes each candidate won.
7. Determine the winner of the election based on popular vote.

## Resources 
- Data Sources: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.62.1

## Challenge Results
The analysis of the election is as follows:
- There were 369,711 votes cast in the election.
  - Jefferson county had 38,855 votes, 10.3 % of total vote
  - Denver county had 306,055 votes, 82.8%  of total votes
  - Arapahoe county had 24,801 votes,  6.7% of total votes
- The county with the highest turnout:
  -  Denver county
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes 
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes 
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes

## Challenge Summary

A 'counties' list was decalred and used to tally county votes within the same loop tracking candidate counts:

        #Write an if statement that checks that the county does not match any existing county in the county list.
        if county_name not in counties:

            # Add the existing county to the list of counties.
            counties.append(county_name)

The list was added to a dictionary to begin tracking the count:
            
            # Begin tracking the county's vote count.
            county_votes_dict[county_name] = 0

        # Add a vote to that county's vote count.
        county_votes_dict[county_name] += 1
        
This same method could be used to determine count based on demographical data, such as political party or ethnicity, should that be provided. Simply create a new list and index beginning with zero and iterate within the same 'for' loop:

    # Candidate Options and candidate votes.
    candidate_options = []
    candidate_votes = {}
    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        county_turnout_votes = county_turnout_votes + 1
        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
    
        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        etc.
        
The printing script can also be ammended to include additional information, would just require to define additional conditions under the if statement within the same for loop 
           
    # Print the county with the largest turnout to the terminal.
    largest_county_turnout = (
        f"-------------------------\n"
        f"Largest County Turnout: {county_highest_turnout}\n"
        f"-------------------------\n")
    print(largest_county_turnout)


