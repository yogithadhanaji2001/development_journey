# read a number from user

# display ping if number is /3
# display pong in number is / 5
# display pingpong if number is/ 15

number = int(input("enter number"))

if number %15 ==0:
    print("pingpong")

elif number % 5 ==0:
    print("pong")

elif number % 3 ==0:
    print("ping")    

else: 
    print("invalid!!!!")  

  
