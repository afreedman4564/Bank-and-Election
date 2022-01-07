# import os
import os

# package for reading CSV files
import csv

# identify the path to read in a csv file
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# look for path of csv file and call csvfile
with open(csvpath) as csvfile:

    # CSV reader function to apply delimiter and allow variables to be read as a list
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # initialize counters, lists and variables to call on later
    mth_cnt = 0
    profLossAgg = 0
    chg_from_prior = 0
    mean_chg = 0
    chg_agg = 0
    mth_list = []
    chg_list = []
    profLoss_list = []
    mth_chg = []
    profLoss_chg = []
    profLoss_zip = []
    month_zip = []
    max_list = []
    min_list = []

        
    # Read each row of data after the header
    for row in csvreader:
        month = row[0]
        int_chg_number = int(row[1])

        # calculate net profit/loss
        profLossAgg += int(row[1])

        # counter for number of months
        mth_cnt += 1

        #average profit/loss


        # create lists to reference later
        month_zip.append(month)
        chg_list.append(int_chg_number)
        profLoss_list.append(int_chg_number)


    # initiate for loop to calculate the month over month profit/loss, starting on index 1 (2nd month) since 1st month of data will have nothing to compare
    for i in range(2, (mth_cnt + 1)):
        # account for zero index subtract 1
        chg_index = i - 1

        # calculate the month over month profit/loss
        chg = profLoss_list[chg_index] - profLoss_list[(chg_index - 1)]
        chg_agg = chg_agg + chg
        mth_chg.extend([chg_index, chg])
        mean_chg = chg_agg/chg_index
        profLoss_chg.append(chg)
        
        # create additional list with profit/loss change so can zip file and have record align with month file. Calculating the month over month change reduces record count by one.
        profLoss_zip.append(chg)
  

    # insert value of zero in list to zip with month list. This will allow the proper alignment of month over month change with the correct month.
    profLoss_zip.insert(0, 0)

    # zip lists to create tuple with month and profit/loss month over month change.
    chg_zip = zip(month_zip, profLoss_zip)

    # convert the tuple to a list
    chg_zip_to_list = list(chg_zip)

    # grab max and min profit/loss change
    max_chg  = max(profLoss_chg)
    min_chg = min(profLoss_chg)

    # identify the month with the max month over month change by using a boolean to search through the list of all month over month changes.
    for row in chg_zip_to_list:
        if max_chg == row[1]:
            max_list.extend([row[0], row[1]])


    # identify the month with the min month over month change by using a boolean to search through the list of all month over month changes.
    for row in chg_zip_to_list:
        if min_chg == row[1]:
            min_list.extend([row[0], row[1]])

# print rows required for exercise with proper formatting
titleRow = "Financial Analysis"
splitRow = "-------------------------------------"
total = "Total Months: " + str(mth_cnt)
net = "Net Profit/Loss: " + str("${:,.0f}".format(profLossAgg))
avg_chg = "Average Change: " + str("${:,.2f}".format(round(mean_chg, 2)))
grt_inc = "Greatest Increase in Profits: " + max_list[0] + " " + str("${:,.0f}".format(max_chg))
grt_dec = "Greatest Decrease in Profits: " + min_list[0] + " " + str("${:,.0f}".format(min_chg))


# create list of desired rows
desired_rows = [titleRow, splitRow, total, net, avg_chg, grt_inc, grt_dec]

# use join function to integrate a carriage return for each variable
desired_rows_formatted = "\n".join(desired_rows)
print(desired_rows_formatted)

# write desired output to text file
output_path = "PyBank/Resources/pybank_data.txt"

with open(output_path, "w") as text:

    text.writelines(desired_rows_formatted)
   