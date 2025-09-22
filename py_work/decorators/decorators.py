# decorators are a function that change the behaviour of another function without changing defition



class Socilmedia:

    def __init__(self,name):

        self.name=name


    def add_post(self):

        print(self.name, "adding new post")    


    def list_all_post(self):

        print(self.name, "listiing all post")

    def add_story(self):

        print(self.name,"adding post")



fb_instance=Socilmedia("facebook")

fb_instance.add_post()




# decorator are normal function that receive function as a parameter

# there will be another wrapper function inside decorator function


def swap_dec(func):
     
    def wrapper(n1,n2):

        if n1<n2:
             
             (n1,n2)=(n2,n1)


        return func(n1,n2)
    
    return wrapper



@swap_dec
def sub (n1,n2):


    return n1-n2


@swap_dec
def div (n1,n2):
     
    return n1/n2
    


print(sub(10,5))
print(div(5,10))



def abs_dec(fun):

    def wrapper(num1,num2):

        return fun(abs(num1),abs(num2))
    

    return wrapper


@abs_dec

def add_number(num1,num2):

    return num1+num2


print(add_number(-10,10))