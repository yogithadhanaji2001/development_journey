"""

*args(receives parameter as tuple)

**kwargs (key word argument) (receives parameter as dictonary)


"""



def add_number(*args):

    return sum(args)


print(add_number(10,20))
print(add_number(10,20,30))
print(add_number(10,20,30,40))



def display_person_details(*args):

    print(args)

    name= args[0]

    print(name)

display_person_details("yogi","street1","uk","london")


def display_student_details(**kwargs):

    print(kwargs)

    

display_student_details(roll=1234, name="yogitha", place="london" )    