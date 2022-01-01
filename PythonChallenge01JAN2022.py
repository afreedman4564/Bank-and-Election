# import os
import os

# package for reading CSV files
import csv
import statistics

csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    row_count = 0
    mth_cnt = 0
    mth_list = []
    profLossAgg = 0
    chg_list = []

        
    # Read each row of data after the header
    for row in csvreader:
        month = row[0]
        int_chg_number = int(row[1])
        int_chg_string = row[1]
        profLossAgg += int(row[1])
        row_count += 1
        avg = profLossAgg/row_count
        mth_list.extend([month, row_count, int_chg_number, int_chg_string, profLossAgg, avg])
        chg_list.append(int_chg_number)

    print(mth_list)
    print(chg_list)
    mean_chg = statistics.mean(chg_list)
    max_chg  = max(chg_list)
    min_chg = min(chg_list)

    print("------------------------------------------------")
    print("break")
    print("------------------------------------------------")

    max_list = []
    min_list = []

csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        if str(max_chg) == row[1]:
            max_list.extend([row[0], row[1]])

    print(max_list)


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        if str(min_chg) == row[1]:
            min_list.extend([row[0], row[1]])


print("Financial Analysis")
print("------------------------------------------------")
print(f"Total Months: {row_count}")
print(f"Net Profit/Loss: {profLossAgg}")
print(f"Average Change: {round(mean_chg, 2)}")
print(f"Greatest Increase in Profits: {max_list[0]} {max_chg}")
print(f"Greatest Decrease in Profits: {min_list[0]} {min_chg}")       

titleRow = "Financial Analysis"
splitRow = "-------------------------------------"
total = "Total Months: " + str(row_count)
net = "Net Profit/Loss: " + str("${:,.0f}".format(profLossAgg))
avg_chg = "Average Change: " + str("${:,.2f}".format(round(mean_chg, 2)))
grt_inc = "Greatest Increase in Profits: " + max_list[0] + " " + str("${:,.0f}".format(max_chg))
grt_dec = "Greatest Decrease in Profits: " + min_list[0] + " " + str("${:,.0f}".format(min_chg))

list_zip = zip(titleRow, splitRow, total, net, avg_chg, grt_inc, grt_dec)
print(list_zip)

output_path = "PyBank/Resources/pybank_data.txt"

with open(output_path, "w") as text:

    text.write(f"{titleRow}\n")
    text.write(f"{splitRow}\n")
    text.write(f"{total}\n")
    text.write(f"{net}\n")
    text.write(f"{avg_chg}\n")
    text.write(f"{grt_inc}\n")
    text.write(f"{grt_dec}\n")
   