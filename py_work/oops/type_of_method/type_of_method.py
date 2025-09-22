# method are type of function define inside class

# there are type of methods

#   * intance method

#   * class method

#   * static method



class Employe:

    def __init__(self,id,name):

        self.id=id

        self.name=name


    def display_employe(self):

        print(self.id,self.name) 


    @classmethod
    def cls_method(cls):

        print("inside class method")

    @staticmethod
    def static_method():
        print("inside static method")    

school=Employe(101, "ravi")
school.display_employe()

Employe.cls_method()

Employe.static_method()