import os
import csv



with open("c:/Users/Brian/Desktop/homework3/budget_data.csv","r") as revenue_data:
    csv_reader = csv.reader(revenue_data)

    next(csv_reader) 
    Total_Revenue = []
    Months = []
    rev_change = []

    for row in csv_reader:

        Total_Revenue.append(int(row[1]))
        Months.append(row[0])
 
    for i in range(1,len(Total_Revenue)):
        rev_change.append(Total_Revenue[i] - Total_Revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)
        avg_rev_change = round(avg_rev_change,2)
        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(Months[rev_change.index(max(rev_change))+1])
        min_rev_change_date = str(Months[rev_change.index(min(rev_change))+1])


print("Financial Analysis")
print("-----------------------------------")
print("Total Months:", len(Total_Revenue))
print("Total Revenue: $", sum(Total_Revenue))

print(f'Average Revenue Change: ${avg_rev_change}')
print(f'Greatest Increase in Revenue: {max_rev_change_date}, ${max_rev_change}')
print(f'Greatest Decrease in Revenue: {min_rev_change_date}, ${min_rev_change}')

output= open("pybank_report.txt","w+")
output.write('Financial Analysis')


