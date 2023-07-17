import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')
# Path to export data into the analysis folder
output_path = os.path.join('Analysis', 'budget_analysis.txt')

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Header: Date,Profit/Losses 
    header = next(csvreader)

    """ Initialize Vars:
    Counts the number of rows in csv which is equal to the number of monthes """
    totalMonths = 0
    # Use to calc the net total
    netTotal = 0
    # Use to calc the changes in Profit/Losses
    previousProfitLoss = 0
    totalChange = 0
    # Use to calc the Greatest Increase/ Greatest Decrease
    max = 0
    preMax = 0
    min = 0
    preMin = 0
    greatestIncreaseAmount = 0
    greatestIncreaseDate = ""
    greatestDecreaseAmount = 0
    greatestDecreaseDate = ""
    
    # Loop through the data
    for row in csvreader:
        # Increment the total number of months
        totalMonths += 1
        
        # Calculate the net total
        netTotal += int(row[1])
        
        # Calculate the change in profit/losses and keeps track of the greatest increase/decrease
        currentProfitLoss = int(row[1])
        if totalMonths > 1:
            change = currentProfitLoss - previousProfitLoss
            totalChange += change
            
            # Check for greatest increase and decrease
            if change > greatestIncreaseAmount:
                greatestIncreaseAmount = change
                greatestIncreaseDate = row[0]
            if change < greatestDecreaseAmount:
                greatestDecreaseAmount = change
                greatestDecreaseDate = row[0]
                
        previousProfitLoss = currentProfitLoss

    # Calculate the average change
    averageChange = totalChange / (totalMonths - 1)
        
    # Prints into terminal
    print()
    print("Financial Analysis")
    print()
    print("-----------------------------")
    print()
    print(f"Total Monthes: {totalMonths}")
    print()
    print(f"Total: ${netTotal}")
    print()
    print(f"Average Change: ${averageChange:.2f}")
    print()
    print(f"Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncreaseAmount})")
    print()
    print(f"Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecreaseAmount})")
    print()
    
    # Export into budget_analysis.txt
    with open(output_path, 'w') as txtfile:
        txtfile.write("Financial Analysis\n")
        txtfile.write("-----------------------------\n")
        txtfile.write(f"Total Months: {totalMonths}\n")
        txtfile.write(f"Total: ${netTotal}\n")
        txtfile.write(f"Average Change: ${averageChange:.2f}\n")
        txtfile.write(f"Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncreaseAmount})\n")
        txtfile.write(f"Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecreaseAmount})\n")