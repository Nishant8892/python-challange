
import os
import csv
os.chdir(os.path.dirname(__file__))
print("route of program is: " + os.getcwd())
csvpath = os.path.join('Resources', 'budget_data.csv')
Total_months = 0
Total_revenue = 0
previous_revenue = 0
Total_revenue = []
months_change = []
revenue_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]
revenue_change_list = []
revenue_average = 0
Row = []
with open(csvpath) as csvfile:
    Total_months +=1
    Total_revenue = Total_revenue + Row("profit/Losses")
    revenue_change = float(row["profit/losses"]) - previous_revenue
    previous_revenue = float(row["profit/losses"])
    revenue_change_list = revenue_change_list + [revenue_change]
    months_change = months_change +[row["date"]]

if revenue_change > greatest_increase[1]:
    greatest_increase[1] = revenue_change
    greatest_increase[0] = row["date"]
    
if revenue_change < greatest_decrease[1]:
    greatest_decrease[1] = revenue_change
    greatest_decrease[0] = row["date"]

    revenue_average = sum(revenue_change_list)/len(revenue_change_list)
    output_path = os.path.join("Analysis", "Result.txt")
    
with open(output_path, 'W') as txtfile:


    print("Financial Analysis\n")
    print("---------------------\n")
    print("Total Months: %d\n" %Total_months)
    print("Total revenue: $%d\n" %total_revenue)
    print("Average revenue Chang $%d\n" %revenue_change_list)
    print("Greatest Increase in revenue: %s($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    print("Greatest Decrease in Profits:%s($%S)\n" % (greatest_decrease[0], greatest_decrease[1]))