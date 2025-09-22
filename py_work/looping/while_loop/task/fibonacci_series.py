# generate fibonacci seriess(upto n number)

# use a while loop to generate and print first n term of fibonacci sequence

# 0 1 1 3 4 7 .....

p=0
c=1
print(p,end=" ")

for i in range (1,5):

    n=c+p
    c=p
    p=n

    print(n,end=" ")


   