import os
import csv


csv_file_name = "election_results.csv"
csv_file_path = os.path.join('Resources', 'election_results.csv')
print("csv_file_path: ", csv_file_path)

# Read the csv file using csv module reader function
with open(csv_file_path, "r") as csv_file_reader:
    csv_reader = csv.reader(csv_file_reader, delimiter=',')
    headers = next(csv_file_reader)
    print("headers: ", headers)

    # for row in csv_reader:
        # print(row)




# with open(csv_file_path) as election_data:
#     print(election_data)
#
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# with open(file_to_save,"w") as election_analysis:
#     election_analysis.write("Hello World !")


# The total number of votess cast in this election
# Complete list of candidates who received votes
# Percentage of votes won by each candidate
# Total number of votes received by every candidate
# Winner of the election based on popular vote

