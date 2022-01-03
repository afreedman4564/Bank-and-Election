# import os
import os

# package for reading CSV files
import csv
import statistics

csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    row_count = 0
    mth_cnt = 0
    mth_list = []
    profLossAgg = 0
    profLossAgg_last = 0
    chg_list = []
    profLoss_list = []
    mth_chg = []
    profLoss_chg = []

        
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
        profLoss_list.append(int_chg_number)


    print(row_count)
  
    for i in range(2, (row_count + 1)):
        chg_index = i - 1
        # if chg_index == 0:
        #     profLossAgg_last = 0
        #     chg = profLoss_list[chg_index] - profLossAgg_last
        #     chg_per = 0
        #     mth_chg.extend([chg_index, chg, profLossAgg_last, chg_per])
        #     profLoss_chg.append(chg)
        # else:
        profLossAgg_last = profLoss_list[(chg_index - 1)]
        chg = profLoss_list[chg_index] - profLoss_list[(chg_index - 1)]
        chg_per = chg / profLossAgg_last
        mth_chg.extend([chg_index, chg, profLossAgg_last, chg_per])
        profLoss_chg.append(chg) 
    print(profLoss_chg)

    # print(mth_list)
    # print(chg_list)
    mean_chg = statistics.mean(profLoss_chg)
    max_chg  = max(profLoss_chg)
    min_chg = min(profLoss_chg)

    print(mean_chg, max_chg, min_chg)

    # print("------------------------------------------------")
    # print("break")
    # print("------------------------------------------------")

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


# print("Financial Analysis")
# print("------------------------------------------------")
# print(f"Total Months: {row_count}")
# print("Net Profit/Loss: " + str("${:,.0f}".format(profLossAgg)))
# print("Average Change: " + str("${:,.2f}".format(round(mean_chg, 2))))
# print("Greatest Increase in Profits: " + max_list[0] + " " + str("${:,.0f}".format(max_chg)))
# print("Greatest Decrease in Profits: " + min_list[0] + " " + str("${:,.0f}".format(min_chg)))       

titleRow = "Financial Analysis"
splitRow = "-------------------------------------"
total = "Total Months: " + str(row_count)
net = "Net Profit/Loss: " + str("${:,.0f}".format(profLossAgg))
avg_chg = "Average Change: " + str("${:,.2f}".format(round(mean_chg, 2)))
grt_inc = "Greatest Increase in Profits: " + max_list[0] + " " + str("${:,.0f}".format(max_chg))
grt_dec = "Greatest Decrease in Profits: " + min_list[0] + " " + str("${:,.0f}".format(min_chg))

list_zip = [titleRow, splitRow, total, net, avg_chg, grt_inc, grt_dec]
new_zip = "\n".join(list_zip)
#print(list_zip)
print(new_zip)

output_path = "PyBank/Resources/pybank_data.txt"

with open(output_path, "w") as text:

    text.writelines(new_zip)

    # text.write(f"{titleRow}\n")
    # text.write(f"{splitRow}\n")
    # text.write(f"{total}\n")
    # text.write(f"{net}\n")
    # text.write(f"{avg_chg}\n")
    # text.write(f"{grt_inc}\n")
    # text.write(f"{grt_dec}\n")
   