# read a year display year is leap year or not

year = int(input("enter year"))


if year%100!=0 and year %4==0 or year%100==0 and year%400==0:
    print("leap year")

else:
    print("not leap year")    

