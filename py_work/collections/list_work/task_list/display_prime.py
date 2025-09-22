def is_prime(number):

    is_prime=True

    for i in range (2,number):

        if number %i==0:

            is_prime=False

            break

    return is_prime

numbers=[151,152,153,1634,8891,345,678,11]


for num in numbers:

    if is_prime(num):
        print(num)
