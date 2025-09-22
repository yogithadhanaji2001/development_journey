# create a function odd_even with one parameter

# function display count of odd number and count of even number 

# odd_even_number(1234)
# odd_count=1
# even_count=1


def odd_even_counter(numbers):
    
    numbers= int(input("enter number"))
    even_count = 0
    odd_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print(f"Number of even numbers: {even_count}")
    print(f"Number of odd numbers: {odd_count}")


    





    
