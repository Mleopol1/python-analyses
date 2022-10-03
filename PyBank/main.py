# CSV headers: Date, Profit/Losses
# Import modules and create a path
import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

# Initialize variables
month_total = 0
PL_total = 0
PL_change = []
current_month = []

# Read CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Log first row to exlude header from loop
    month_total += 1
    first_row = next(csvreader)
    PL_total += int(first_row[1])
    previous_row = first_row

    # Loop through each row
    for row in csvreader:

        # Calculate total months and net total of Profit/Losses
        month_total += 1
        PL_total += int(row[1])

        # Calculate changes in Profit/Losses between current row and previous row 
        PL_change.append(int(row[1]) - int(previous_row[1]))
        current_month.append(row[0])
        # Reset previous row
        previous_row = row 

        # Average of those changes
        average = round((sum(PL_change) / len(PL_change)), 2)

# Calculate greatest increase in profits
inc_index = PL_change.index(max(PL_change))
greatest_inc = (current_month[inc_index], max(PL_change))

# Calculate greatest decrease in profits
dec_index = PL_change.index(min(PL_change))
greatest_dec = (current_month[dec_index], min(PL_change))

# Print final analysis
print(f"Financial Analysis\n",
    f"----------------------------\n",
    f"Total Months: {month_total}\n",
    f"Total: ${PL_total}\n",
    f"Average Change: ${average}\n",
    f"Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})\n",
    f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})")

# Export analysis to text file
folder = 'analysis'
file_name = 'output.txt'
path = os.path.join(folder, file_name)

file = open(path, 'w')
file.write(f"Financial Analysis\n")
file.write(f"----------------------------\n")
file.write(f"Total Months: {month_total}\n")
file.write(f"Total: ${PL_total}\n")
file.write(f"Average Change: ${average}\n")
file.write(f"Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})\n")
file.write(f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})")
file.close()