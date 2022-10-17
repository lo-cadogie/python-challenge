'''
PyPoll Challenge

Written by Lauren Cadogan

'''
#imports
import os
import csv

#Open the file
csvpath = os.path.join("Resources", "election_data.csv")

# Starting variables / counters
num_votes = 0
candidate_list = []
num_ccs = 0
num_dd = 0
num_rad = 0


with open (csvpath) as poll_csv:
    csvreader = csv.reader(poll_csv, delimiter = ",")
    poll_header = next(csvreader)
    for line in csvreader:
        if line != poll_header:
            # total number of votes
            num_votes += 1
            # Candidate Name
            cand_name = line[2]
            if cand_name not in candidate_list:
                # add name to candidate list
                candidate_list.append(cand_name)
            # calculate votes per candidate
            if cand_name == "Charles Casper Stockham":
                num_ccs += 1
            elif cand_name == "Diana DeGette":
                num_dd += 1
            else:
                num_rad += 1

#Calculate % of votes for each candidate and reformat to 3 decimal places
perc_ccs = (num_ccs / num_votes) * 100
perc_ccs = "{:.3f}".format(perc_ccs)

perc_dd = (num_dd / num_votes) * 100
perc_dd = "{:.3f}".format(perc_dd)

perc_rad = (num_rad / num_votes) * 100
perc_rad = "{:.3f}".format(perc_rad)

# winner based on popular vote
list_winners = [perc_ccs, perc_dd, perc_rad]
if max(list_winners) == perc_ccs:
    winner = candidate_list[0]
elif max(list_winners) == perc_dd:
    winner = candidate_list[1]
else:
    winner = candidate_list[2]


#Output to terminal
print("Election Results \n")
print('-' * 30)
print()
print(f'Total Votes: {num_votes} \n')
print('-' * 30)
print()
print(f"{candidate_list[0]}: {perc_ccs}% ({num_ccs}) \n")
print(f"{candidate_list[1]}: {perc_dd}% ({num_dd}) \n")
print(f"{candidate_list[2]}: {perc_rad}% ({num_rad}) \n")
print('-' * 30)
print()
print (f'Winner: {winner} \n')
print('-' * 30)


# Output File

output_path = os.path.join("Analysis", "Election_Results.txt")

with open (output_path, 'w', newline = '') as output_file:
    # write to txt file
    output_file.write('Election Results \n')
    output_file.write(' \n')
    output_file.write('-' * 30)
    output_file.write(' \n')
    output_file.write(' \n')
    output_file.write(f'Total Votes: {num_votes} \n')
    output_file.write(' \n')
    output_file.write('-' * 30)
    output_file.write(' \n')
    output_file.write(' \n')
    output_file.write(f"{candidate_list[0]}: {perc_ccs}% ({num_ccs}) \n")
    output_file.write(' \n')
    output_file.write(f"{candidate_list[1]}: {perc_dd}% ({num_dd}) \n")
    output_file.write(' \n')
    output_file.write(f"{candidate_list[2]}: {perc_rad}% ({num_rad}) \n")
    output_file.write(' \n')
    output_file.write('-' * 30)
    output_file.write(' \n')
    output_file.write(' \n')
    output_file.write(f'Winner: {winner} \n')
    output_file.write(' \n')
    output_file.write('-' * 30)
