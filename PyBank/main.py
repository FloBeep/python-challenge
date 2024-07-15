# Import and declare file location
import os, csv

input_file = os.path.join('Resources', 'budget_data.csv')

# Set up variables
total_months = []
total_profit = []
monthly_profit_change = []
 
# Open csv file and store in variable
with open(input_file,newline="", encoding="utf-8") as budget:

    csvreader = csv.reader(budget,delimiter=",") 

    # Skip the header and iterate through rows
    header = next(csvreader)  

    for row in csvreader: 

        # Append the totals
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Use a loop to get the monthly change in profits
    for i in range(len(total_profit)-1):
        
        # Calculate the difference between two months and append monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
# Get the max and min of the the montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Add +1 to correlate max and min to the proper month

max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print results in code

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Output txt file and write
output_file = os.path.join('Financial_Analysis_Results.txt')

with open(output_file,"w") as file:
    
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")