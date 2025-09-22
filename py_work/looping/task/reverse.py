num=int(input("enter number:"))

reverse=0

# for i in range(num) :

#     digit = num%10

#     reverse=reverse*10+digit

#     num = num//10

    

# print(reverse)



while num !=0:

    digit= num %10

    reverse= reverse*10+digit

    

    num = num//10

print(reverse)    
