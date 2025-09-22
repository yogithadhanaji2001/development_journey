# employe (id,name,depat,salary) [set_employe,display employe]


class employee:

    id:int
    name:str

    depat:str

    salary:int


    def set_employe(self,id,name,depat,salary):

        self.id=id

        self.name=name

        self.depat= depat

        self.salary=salary


    def display_employe(self):

        print(self.id,self.name,self.depat,self.salary)


emp_instance=employee()

emp_instance.set_employe(1000,"ram","hr",230000)

emp_instance.display_employe()