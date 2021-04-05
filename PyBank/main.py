# Importing the os module and reading csv file
import os
import csv

csvpath = os.path.join ("..", "PyBank", "Resources", "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

# Storing data for the append variables 
num_months = []
net_total = []
profitloss_change_months = []

# Setting the numeric variables equal to zero
profit_loss_change = 0
previous_profit_loss = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    
    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    

    for row in csvreader: 
        # Finding total number of months
        num_months.append(row[0])
        Months = len(num_months)
        
        # Finding net total amount of profit/losses
        net_total.append(int(row[1]))
        total = sum(net_total)

        

    # Calcuating the profits and losses over the entire period and appending to the monthly change in profit/losses
    for t in range(len(net_total)-1):
        profitloss_change_months.append(net_total[t+1] - net_total[t])

# Finding the average of the profit and loss changes by month
profit_loss_average = round((sum(profitloss_change_months)/len(profitloss_change_months)),2)

# Finding the greatest increase in profits and matching the date
greatest_increase = max(profitloss_change_months)
increase_month = profitloss_change_months.index(max(profitloss_change_months)) + 1


# Finding the greatest decrease in profits and matching date index
greatest_decrease = min(profitloss_change_months)
decrease_month = profitloss_change_months.index(min(profitloss_change_months)) + 1

    

print(f"Financial Analyst")
print(f"--------------------------")
print(f"Total: ${total}")
print(f"Total Months: {Months}")
print(f"Average Change: ${profit_loss_average}")
print(f"Greatest Increase in Profits: {num_months[25]} , ${str(greatest_increase)}")
print(f"Greatest Decrease in Profits: {num_months[44]} , ${str(greatest_decrease)}")

# Exporting results to text file
results = (
    f"Financial Analyst\n"
    f"--------------------------\n"
    f"Total: ${total}\n"
    f"Total Months: {Months}\n"
    f"Average Change: ${profit_loss_average}\n"
    f"Greatest Increase in Profits: {num_months[25]} , ${str(greatest_increase)}\n"
    f"Greatest Decrease in Profits: {num_months[44]} , ${str(greatest_decrease)}\n"
)
print(results)

results_output = os.path.join("Election_Poll_Results.txt")

with open(results_output, "w")as txt_file:
    for results in results:
        txt_file.write(results)
