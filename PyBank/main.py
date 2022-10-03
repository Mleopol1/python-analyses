# CSV headers: Date, Profit/Losses
# Import modules and create a path
import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

# Initialize variables
month_total = 0
net_total = 0
month_track = []
change_list = []
greatest_inc = ["", 0]
greatest_dec = ["", 999999999999]

# Read CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Get data from first row so header is not calculated in the loop
    first_row = next(csvreader)
    month_total += 1
    net_total += int(first_row[1])
    # Set current profit/loss as the previous one after totals have been calculated
    previous_PL = int(first_row[1])

    for row in csvreader:
        # Calculate totals
        month_total += 1
        net_total += int(row[1])

        # Track changes in Profits/Losses over the entire period
        PL_change = int(row[1]) - previous_PL
        previous_PL = int(row[1])
        change_list += [PL_change]
        month_track += [row[0]]

        # Track and record the greatest increase
        if PL_change > greatest_inc[1]:
            greatest_inc[0] = row[0]
            greatest_inc[1] = PL_change
        
        # Track and record greatest decrease
        if PL_change < greatest_dec[1]:
            greatest_dec[0] = row[0]
            greatest_dec[1] = PL_change
        
        # Calculate Average of Profits/Losses changes
        average = round(sum(change_list) / (month_total - 1), 2)

# Print final analysis
print(f"Financial Analysis\n",
    f"----------------------------\n",
    f"Total Months: {month_total}\n",
    f"Total: ${net_total}\n",
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
file.write(f"Total: ${net_total}\n")
file.write(f"Average Change: ${average}\n")
file.write(f"Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})\n")
file.write(f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})")
file.close()