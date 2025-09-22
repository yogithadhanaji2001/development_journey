num=123456789

sum=0

while num !=0:

    digit=num%10

    sum=digit+sum

    # print(sum)

    num=num//10

print(sum)