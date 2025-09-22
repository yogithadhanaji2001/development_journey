# bill amount => read bill amount 450

# dines_count = > read  dines_count 5

# calculate tip as 12% of bill amount

# add 8% of gst along with bill amount

# calculate total amount and individual split

bill_amount = int(input("enter bill amount"))

dines_count = int(input("enter dines count"))

tip = (12/100)*bill_amount

gst = (8/100)*bill_amount

total_amount = bill_amount + tip + gst

individual_split = total_amount/dines_count

print(individual_split)