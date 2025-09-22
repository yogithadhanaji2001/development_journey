# single inheritance

# one child class aquireing method  annd atritubute from one parent class


class parent :

    def car(self):

        print("parent swift car")

    def bike(self):

        print("parent passion pro") 


class child (parent):

    def bike (self):

        print("child trimph bike")



child_instance=child()

child_instance.bike()

child_instance.car()


