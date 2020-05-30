# Add our dependencies.
import csv
import os

# Assign a variable toload a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis/election_analysis.txt")

# Initialize variables
total_votes = 0
candidate_options = []
candidate_votes = {}
counties = []
county_votes = {}
county_results = []
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1
        
        # Get the candidate name from each row.
        candidate_name = row[2]
        county_name = row[1]
        
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
            
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        if county_name not in counties:
            # Add the candidate name to the candidate list.
            counties.append(county_name)
            county_votes[county_name] = 0
            
        county_votes[county_name] += 1
    
    for county in county_votes:
        # Retrieve vote count and percentage.
        c_vote = county_votes[county]
        county_vote_percentage = float(c_vote) / float(total_votes) * 100
        county_results.append(f"{county}: {county_vote_percentage:.1f}% ({c_vote:,})\n")        
        
    max_key = max(county_votes, key=county_votes.get)

    


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")    
    for result in county_results:
        print(result)
    print("-------------------------\nLargest County Turnout:",
    max_key,"\n-------------------------")
    
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    
    for result in county_results:
       txt_file.write(result)
    
    txt_file.write("-------------------------\nLargest County Turnout:")
    txt_file.write(max_key)               
    txt_file.write("\n-------------------------\n")
    
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        
        
        
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
            
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)