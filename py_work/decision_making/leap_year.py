year = int(input("enter year"))


if year %100!=0 and year%4==0 or year%100==0 and year%400==0:
    print("leap yer")

else:
    print("non century year") 


      