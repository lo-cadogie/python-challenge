'''
PyBank Challenge

Analyze financial records from a company.
Given Data is month and profit/loss for that month.

written by Lauren Cadogan

'''

import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

num_months = 0 # month counter
total_profit = 0 # profit counter
monthly_change = [] # empty list to add monthly changes
last_pl= 0 # variable to track last months profit/loss

with open (csvpath) as budget_csv:
    csvreader = csv.reader(budget_csv, delimiter = ",")
    budget_header = next(csvreader)
    for line in csvreader:
        if line != budget_header:
            # total number of months counter
            num_months += 1
            # net total profit/loss over period
            total_profit += float(line[1])
            # change in profit/loss over period - average of those change
            current_pl = float(line[1])
            change = current_pl - last_pl
            monthly_change.append(change)
            last_pl = current_pl
            # greatest increase in profits with date and amt
            if change == max(monthly_change):
                max_mo_change = line[0] + " ($" + str(int(change)) + ")"
            # greatest decrease in profits with date and amt
            if change == min(monthly_change):
                min_mo_change = line[0] + " ($" + str(int(change)) + ")"


del monthly_change[0] # first month value should not be included in monthly change
ave_mo_change = sum(monthly_change) / (len(monthly_change))

# change total from float to int
total_profit = int(total_profit)

# Print to Terminal
print('Finanacial Analysis \n')
print('-' * 30)
print()
print(f'Total Months: {num_months}\n')
print(f'Total: ${total_profit}\n')
ave_mo_change = "{:.2f}".format(ave_mo_change) #formats it to two decimal places
print(f'Average Change: ${ave_mo_change}\n')
print(f'Greatest Increase in Profits: {max_mo_change}\n')
print(f'Greatest Decrease in Profits: {min_mo_change}')

# writing a file
output_path = os.path.join("Analysis", "Financial_Analysis.txt")

with open (output_path, 'w', newline = '') as output_file:
    # write to txt file
    output_file.write('Finanacial Analysis \n')
    output_file.write(' \n')
    output_file.write('-' * 30)
    output_file.write(' \n')
    output_file.write(' \n')
    output_file.write(f'Total Months: {num_months}\n')
    output_file.write(' \n')
    output_file.write(f'Total: ${total_profit}\n')
    output_file.write(' \n')
    output_file.write(f'Average Change: ${ave_mo_change}\n')
    output_file.write(' \n')
    output_file.write(f'Greatest Increase in Profits: {max_mo_change}\n')
    output_file.write(' \n')
    output_file.write(f'Greatest Decrease in Profits: {min_mo_change}')
