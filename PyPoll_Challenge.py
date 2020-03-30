# Add our Dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# 1. Initialize a total vote counter.
total_votes = 0
# Candidate Options
candidate_options = []
## CHALLENGE
county_options = []
# Declare an empty dictionary to total candidadte votes.
candidate_votes = {}
## CHALLENGE  Declare an empty dictionary for total county votes
county_votes = {}
# Winning candidate and Winning Count Tracker.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
## CHALLENGE winning county and winning county tracker
#largest_county_turnout = ""
winning_county = ""
county_count = 0
county_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    #Print each row in the csv file.
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
     
        county_name = row[1]
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1

with open(file_to_save, "w") as txt_file:
# Print the final vote count in terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    ## CHALLENGE Do for county votes here what I do for candidate votes below
    for county in county_votes:
        votes = county_votes[county]
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results)
        txt_file.write(county_results)
    ## CHALLENGE This is where I display the Largest County Turnout data.  Mirrored of Winner Candidate logic
    ## CHALLENGE I not fully sure if the "County Winner" variables need to be unique to county or can copy the same variable names from the Candidate code
        if (votes > county_count) and (vote_percentage > county_percentage):
            county_count = votes
            county_percentage = vote_percentage
            winning_county = county
    winning_county_summary = (
        #f" \n"  CHALLENGE commented put due to terminal error, but this is what the assignment calls for
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(winning_county_summary)
    txt_file.write(winning_county_summary)
  
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)


