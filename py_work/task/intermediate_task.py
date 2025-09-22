# Write a program that accept a persons age classifies them as 
# child 0-12
# teen 13-19
# adult 20-59
# senior 60+


age = int(input("enter age"))


if age <=12 and age >=0 :

    print("child")

elif age <=19 and age >0:
    print("teen")   

elif age <=59 and age >0:
    print("adult")

elif age !=100  and age >0 :
    print("senior")

else:
    print("invalid")


