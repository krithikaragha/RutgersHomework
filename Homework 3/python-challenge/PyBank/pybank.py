# Import the operating system package
import os

# Import a package to read in csv
import csv

# Create the path for the file
# Save as Path = '../Resources/budget_data.csv'
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r', errors='ignore') as fileHandle:
    reader = csv.reader(fileHandle)
    months = []
    total = 0
    profits_and_losses = []
    budget_dict = {}
    next(reader) # Skip the first row
    for row in reader:   # row is String
        months.append(row[0].split("-")[0])
        total = total + int(row[1])
        profits_and_losses.append(int(row[1]))
        budget_dict[row[0]] = int(row[1])
    
    greatest_increase_profit_loss = max(profits_and_losses)
    greatest_decrease_profit_loss = min(profits_and_losses)
    average_change = (profits_and_losses[-1] - profits_and_losses[0]) / (len(profits_and_losses) - 1)

    for k, v in budget_dict.items():
        if v == greatest_increase_profit_loss:
            greatest_increase_month = k
        if v == greatest_decrease_profit_loss:
            greatest_decrease_month = k

    print("---------------------------------------------")
    print("Financial Analysis")
    print("---------------------------------------------")
    print("Total months: ", len(months))
    print("Total: $", total)
    print("Average Change: $%.2f" % average_change)
    print("Greatest increase in profits: ", greatest_increase_month, "($",greatest_increase_profit_loss,")")
    print("Greatest decrease in profits: ", greatest_decrease_month, "($",greatest_decrease_profit_loss,")")

f = open("results.txt", "w")
f.write("Financial Analysis\n")  
f.write("---------------------------------------------\n") 
f.write("Total months: ")
f.write(str(len(months)))
f.write("\n")
f.write("Total: $")
f.write(str(total))
f.write("\n")
f.write("Average Change: $")
f.write(str(str(average_change)))
f.write("\n")
f.write("Greatest increase in profits: ")
f.write(str(greatest_increase_month))
f.write("  ($")
f.write(str(greatest_increase_profit_loss))
f.write(")")
f.write("\n")
f.write("Greatest decrease in profits: ")
f.write(str(greatest_decrease_month)) 
f.write("  ($")
f.write(str(greatest_decrease_profit_loss))
f.write(")")
f.write("\n")
f.write("---------------------------------------------\n")    




