
#with open(r"C:\Users\IanAK\Desktop\Rutgers_Data_boot_camp\Py_Poll_Class_3\Class_stuff_3\Election_Analysis\Resources\election_results.csv") as ftl:
#     eld = csv.reader(ftl, delimiter = ',')
#     for row in eld:
#        print(', '.join(row))
# ftl = file_to_load
# eld = election data 
# Be careful all the data was deleted after using this script
#open(r"C:\Users\IanAK\Desktop\Rutgers_Data_boot_camp\Py_Poll_Class_3\Class_stuff_3\Election_Analysis\Resources\election_results.csv",'r')
# <_io.TextIOWrapper name='election_results.csv' mode='r' encoding='cp1252'>
# To do: performance analysis
# Close the file
#with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
#    txt_file.write("Counties in the Election\n ---------------\n Arapahoe\n Denver \n Jefferson\n")

    # Print the file object.
#     print(election_data) # <_io.TextIOWrapper name='election_results.csv' mode='r' encoding='cp1252'>



import csv
import os



total_votes = 0
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
 # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

    # Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

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
    
 # 4. Print the candidate name and percentage of votes.
#print(f"{candidate_name}: received {round(vote_percentage,1)}% of the vote.")
