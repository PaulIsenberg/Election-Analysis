# The data we need to retreive
# 1. The TOTAL number of votes cast
# 2. A list of CANDIDATES who received a vote
# 3. The PERCENTAGE of the TOTAL each CANDIDTATE won
# 4. The TOTAL number of votes for each CANDIDATE
# 5. The WINNER of the election, based on popular vote

# Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.
# with open(file_to_load) as election_data:
    # To Do: Perform analysis.
    # print(election_data)
# Add our Dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources/election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:
    #print the file object
    #print(election_data)
# Create a filename variable to a direct or indirect path to the file.
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")
# Add the vote counter function before the with open() function statement.
# 1. Initialize a total vote counter.
total_votes = 0
# Candidate Options
candidate_options = []
# Declare an empty dictionary to tall candidadte votes.
candidate_votes = {}
# Winning candidate and Winning Count Tracker.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Using the with statement open the file as a text file.
# outfile = open(file_to_save, "w")
# Open the election results and read the file.
# with open(file_to_save, "w") as txt_file:
with open(file_to_load) as election_data:
    # Write some data to the file.
    #outfile.write("Hello World")
    #txt_file.write("Counties in the Election\n -------------------------\nArapahoe\nDenver\nJefferson")
# Close the file
#outfile.close()
    # To Do: Read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the csv file.
    # Read and print only the header row.
    #for row in file_reader:
    #print(row)
    headers = next(file_reader)
    #print(headers)
    #Print each row in the csv file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Print the candidate name for each row.
        candidate_name = row[2]
        # Rename print command
        # print(row)
        # print(total_votes)
        # Print the candidate name to the candidate list
        # If candidate does not match any existing candidate then..
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate
        candidate_votes[candidate_name] += 1


# Save the results to a text file for 3.6.1
with open(file_to_save, "w") as txt_file:
# Print the final vote count in terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

    ## Commenting out for 3.6.2 
    print(election_results, end="")
    ## commenting out for 3.6.2 
    txt_file.write(election_results)
    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.



    for candidate in candidate_votes:
        # 2. Retreive vote count of candidate
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # To Do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
    
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        #print candidate results
        print(candidate_results)
        # Save the final vote count to the text file
        txt_file.write(candidate_results)
    ## commenting out for text file 3.6.1 
    # #print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And set the winning_candidate equal to the candidate's name
            winning_candidate = candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        # 4. Print the candidate name and percentage of votes
        #print(f"{candidate}: received {vote_percentage:.1f}% of the vote.")
    # Print the candidate list
    # Print the candidate vote dictionary
    #print(candidate_options)
    # Print(candidate_votes)
    ## commenting out for 3.6.1 
    print(winning_candidate_summary)
    # save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)


