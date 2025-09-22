digit_max=(lambda n1,n2:n1 if n1%10 > n2%10 else n2)

print(digit_max(124,119))