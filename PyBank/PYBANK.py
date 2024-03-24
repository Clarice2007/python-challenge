import os
import csv
#Path to  cvs files
csvpath = os.path.join('..','Resources','budget_data.csv')

# Create variables
total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
profit_losses_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999]

# RCvs - delimiter and variable of contents 
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read each row of data after the header 
    csv_header = next(csvreader)

    # Loop through the rows in the CSV file
    for row in csvreader:
        # Calculate total months
        total_months += 1
       
        # Calculate the change in profit/losses
        profit_loss_change = int(row[1]) - previous_profit_loss
        previous_profit_loss = int(row[1])
        profit_losses_changes.append(profit_loss_change)
        # Calculate total profit/losses
        total_profit_losses += int(row[1])
        # Calculate the greatest increase in profits
        if profit_loss_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_loss_change

        # Calculate the greatest decrease in profits
        if profit_loss_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_loss_change

# Calculate the average change in profit/losses
average_change = sum(profit_losses_changes[1:]) / len(profit_losses_changes[1:])

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Export a text file with the results
output_path = os.path.join("financial_analysis.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_losses}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")




