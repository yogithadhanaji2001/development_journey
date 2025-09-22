# def max_two(num1,num2):

#     # return max(num1,num2)
#     return 10


# assert max_two(5,10)==10, "text case "

# # print(max_two(20,55))


def exponent (base, power):

    result = base**power

    return result

assert exponent (5,2) == 25 , "text case fail"
assert exponent (2,3) == 8 , "text case failed"
assert exponent (2,0) == 1, "text case failed with bpower as 0"

print ("complete")