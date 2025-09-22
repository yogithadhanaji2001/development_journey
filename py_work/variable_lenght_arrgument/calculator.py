class Calculator:

    def operation (self,*args,**kwargs):

        print(args)
        print(kwargs)

        if kwargs.get("op")== "+":

            return args[0]+args[1]+args[2]
        

        if kwargs.get("op") == "-":

            return args [0] - args[1]
        

calculate_instance= Calculator()

print(calculate_instance.operation(10,20,30,op="+"))
print(calculate_instance.operation(10,20,op="-"))