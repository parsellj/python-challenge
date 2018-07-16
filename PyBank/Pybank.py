# Analyzing Financial records using financial data called budget_data.cvs
# csv file has 2 columns: Date and Profit/Losses
# Use python to produce the following text outputs
# 1) Total number of months
# 2) Total revenue (sum of profit/losses)
# 3) Average change in "Profit/Losses" between months over the entire period
# 4) Greatest increase in profit with date and amount
# 5) Greatest decrease in losses with date and amount

# What to do?  First will need to import csv file using file pathe; declare output path then
# figure out the calculations to accurately produce requested output

# Importing data and providing path

import csv
import os

# Set path for csv file
csv_path = os.path.join ("Resources", "budget_data.csv")

# Input and output
file_to_load = "resources/budget_data.csv"
file_to_output = "output/budget_results.txt"

# Calculation fun starts here - I will attempt to follow the order 1-5 above when possible
# First need to provide variables

# 1) Total number of months
total_months = 0

# 2) Total revenue
total_revenue = 0

# 3) Will pull this in a calulation after 1 and 2 
prev_revenue = 0
month_of_change = []
revenue_change_list = []

# 4)  Greatest increase with date and amount
greatest_increase = ["",0]

# 5) Greatest decrease with date and amount
greatest_decrease = ["", 999999999999999]


# Pull in csv file and reading file
with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)
    
    for row in reader:

        # Want to keep track of the total
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Revenue"])

        # Want to keept track of the revenue change
        revenue_change = int(row["Revenue"]) - prev_revenue
        prev_revenue = int(row["Revenue"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]

        # Fun fun! - calculate the greatest increase
        if(revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        # Even more fun - calculate the greatest decrease
        if(revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

    # My son just got home from camp and last nigh I had the joy of doing 5 loads of disgusting laundry!
    # Almost as much fun as this homework!  
    # Last calculation is the average revenue change
    
    
   
    revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

    # Almost done!  Now it's time to generate Output Summary
    output = (
        f"\nFinancial Analysis\n"
        f"-----------------------------\n"
        f"Total Months:  {total_months}\n"
        f"Total Revenue:  ${total_revenue}\n"
        f"Average Revenue Change: ${revenue_avg}\n"
        f"Greatest Increase in Revenue: {greatest_increase[0]}  (${greatest_increase[1]})\n"
        f"Greatest Decrease in Revenue: {greatest_decrease[0]}  (${greatest_decrease[1]})\n"
    )

    # Fingers crossed - Print the output 
    print(output)

    # Create a text file of the results
    with open(file_to_output,"w") as txt_file:
     txt_file.write(output)       
