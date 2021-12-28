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
    max_list = []
        
    # Read each row of data after the header
    for row in csvreader:
        month = row[0]
        int_chg = int(row[1])
        profLossAgg += int(row[1])
        row_count += 1
        avg = profLossAgg/row_count
        mth_list.extend([month, row_count, int_chg, profLossAgg, avg])
        chg_list.append(int_chg)

    print(mth_list)
    print(chg_list)
    mean_chg = statistics.mean(chg_list)
    max_chg  = max(chg_list)
    min_chg = min(chg_list)

    print("break")

    for x in csvreader:
        if int(x[1]) == max_chg:
            max_mth = x[0]
            max_value = x[1]
            max_list.extend([max_mth, max_value])

        print(max_list)
    
    print("Financial Analysis")
    print("------------------------------------------------")
    print(f"Total Months: {row_count}")
    print(f"Net Profit/Loss: {profLossAgg}")
    print(f"Average Change: {round(mean_chg, 2)}")


    print(f"Greatest Increase in Profits: {max_chg}")
    print(f"Greatest Decrease in Profits: {min_chg}")       
   