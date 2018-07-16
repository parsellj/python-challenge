# Assisting with elections using poll data called election_data.csv
# csv file has 3 columns: Voter_ID, County and Candidate
# Producce 5 outputs as follows:
# 1) Total number of votes cast
# 2) list of candidates who received a vote
# 3) Percentage of votes each candidate won
# 4) Total number of votes each candidate won
# 5) The winner of the election based on popular votes

# What to do - where to start?  Import data using file path; declare out put path then figure out calculations for output

#Importing data and providing path
import csv
import os

# Set path for csv file
csv_path = os.path.join("Resources","election_data.csv")

# Input and output
file_to_load = "resources/election_data.csv"
file_to_output = "output/election_results.txt"

#time for all the fun calculations in the order from 1 to 5 listed above
# 1) Total number of votes cast
total_votes = 0

#2) List of candidates who received votes create place to store names then tally votes in dictionary
candidate_options = []
candidate_votes = {}

# 2-5) Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Pull in csv and convert it to a list of dictionaries
with open(csv_path) as election_data:
    reader = csv.DictReader(election_data)

    # Fun loops to go through each line of data
    for row in reader:

        # Add to the total vote count with each line is one    
        total_votes = total_votes + 1

        # Find the each candidates line by row
        candidate_name = row["Candidate"]

        # Need to add loop to consider changes in candidate name as it goes through rows and add candidate names when first appear
        if candidate_name not in candidate_options:

            # This is where it adds name of candidate if not in already in list
            candidate_options.append(candidate_name)

            # In addition to names we need to track votes
            candidate_votes[candidate_name] = 0

        # need to continue with counts when they are already on the list adding 1 for each appearance in row
        candidate_votes[candidate_name] = candidate_votes[candidate_name]+1

# Fingers crossed this loop works to check need to print and export results as initally requested 
# First open the file to export as a writing file which was previously named above
with open(file_to_output, "w") as txt_file:

    #Print the final vote count - first formatting needs to be assigned to variables
    election_results = (
        f"\n\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes:  {total_votes}\n"
        f"--------------------------\n"
    )
    print(election_results)

    #  Also need to add final vote count to the file
    txt_file.write(election_results)

    # Time to find the winner via looping through the counts
    for candidate in candidate_votes:

        # Find the vote tally and percents for 3 and 4 above with no rounding!
        votes = candidate_votes.get(candidate)
        votes_percentage = float(votes) / float(total_votes) * 100

        # Who is the winner - drum roll
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Time to see the results with formatting
        voter_output = f"{candidate}: {votes_percentage:.3f}% ({votes})\n"
        print(voter_output)

        # See candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # almost there - need to print winner with requested format
    winning_candidate_summary = (
        f"__________________________\n"
        f"Winner: {winning_candidate}\n"
        f"__________________________\n"        
    )
    print(winning_candidate_summary)

    # Add this info to the text file
    txt_file.write(winning_candidate_summary)