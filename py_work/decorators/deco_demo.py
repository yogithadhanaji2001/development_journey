# @classmethod

# @staticmethod

# @property




class Employe:

    def __init__(self,id,name,department):
        

        self.id=id

        self.name=name

        self.department=department

    @property
    def get_name(self):  
        print(self.name) 



Employe_instance=Employe(101,"vipin","hr")

Employe_instance.get_name

print(Employe_instance.id)
print(Employe_instance.department)