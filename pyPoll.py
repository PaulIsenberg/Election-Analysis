# The data we need to retreive
# 1. The TOTAL numbher of votes cast
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
# Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")
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
    print(headers)

