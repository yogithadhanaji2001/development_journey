# more than one form(many forms)

# 1 -- method overloading
# 2-- method overriding



class calculate:
    def add (self,num1,num2):
        print(num1+num2)

    def add(self,num1,num2,num3):
        print(num1+num2+num3)

    def add (self,num1,num2,num3,num4):

        print(num1+num2+num3+num4)

class Calculator:
    def add(self,*args):
        print(sum(args))        

calculate_instance=calculate()

calculate_instance.add(10,20,30,40)

class opertator:

    def add(self,*args):

        print(sum(args))


opertator_instance=opertator()


opertator_instance.add(10,20)
opertator_instance.add(10,20,30)
opertator_instance.add(10,20,30,40)


# *args **kwargs




def add_number(*args):

    print(sum(args))
    # args take any number of parameter as tuple

add_number(10,20)
add_number(10,20,30)    
add_number(10,20,30,40)    
