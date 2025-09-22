# create a list expence

expenses = [10000,12000,13000,14000]

# update 12000 as 12500

expenses[1]=12500

print(expenses)

# print all expenses

for i in range (0, len(expenses)):

    print(expenses[i])




for i in expenses:

    print(i)



# sum of all expenses

# sum=0

# for i in expenses:
#     sum=sum+i

# print(sum)

total=sum(expenses)
print(total)


print(max(expenses))

avg_expen=total/len(expenses)
print(avg_expen)
