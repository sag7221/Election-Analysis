import os
import csv


csv_file_name = "election_results.csv"
csv_file_path = os.path.join('Resources', 'election_results.csv')
print("csv_file_path: ", csv_file_path)

total_vote_count = 0
total_candidates_list = []
candidate_votes_dictionary = {}
# Read the csv file using csv module reader function
with open(csv_file_path, "r") as csv_file_reader:
    csv_reader = csv.reader(csv_file_reader, delimiter=',')
    headers = next(csv_file_reader)
    print("headers: ", headers)

    for row in csv_reader:
        print(row)
        total_vote_count += 1
        if row[2] not in total_candidates_list:
            total_candidates_list.append(row[2])

        # Total number of votes received by every candidate
        if row[2] not in candidate_votes_dictionary:
            candidate_votes_dictionary[row[2]] = 1
        else:
            candidate_votes_dictionary[row[2]] += 1

# The total number of votes cast in this election
print("total_number_of_votes: ", total_vote_count)
# Complete list of candidates who received votes
print("total_candidates_list: ", total_candidates_list)
print("candidate_votes_dictionary: ", candidate_votes_dictionary)

file_to_save = os.path.join("analysis", "election_analysis.txt")

election_summary = (
    f"\n Election Results\n"
    f"------------------------\n"
    f"Total Votes: {total_vote_count:,}\n"
    f"------------------------\n"
)

print(election_summary)
with open(file_to_save, "a") as results_file:
    results_file.write(election_summary)

# Calculate vote percentage for each candidate
vote_percentage = 0
winning_candidate = ""
winning_count = 0
winning_percentage = 0
for key in candidate_votes_dictionary.keys():
    with open(file_to_save, "a") as results_file:
        votes = candidate_votes_dictionary[key]
        vote_percentage = (votes / total_vote_count) * 100
        # Percentage of votes won by each candidate
        print(f"\n{key}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_summary = f"\n{key}: {vote_percentage:.1f}% ({votes:,})\n"
        results_file.write(candidate_summary)

        if(votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = key

with open(file_to_save, "a") as results_file:
    # Winner of the election based on popular vote
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    results_file.write(winning_candidate_summary)
    results_file.close()
















