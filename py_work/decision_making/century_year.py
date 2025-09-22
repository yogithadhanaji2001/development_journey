# read a year

# display year is century year or not

year = int(input("enter year : "))

if year % 100==0:
    print("century year")

elif year % 100!=0:
    print("not century year")    