class employe:
    def __init__(self,name,salary):

        self.name=name

        self.salary=salary

    def calculate_salary(self):

        print(self.salary)


class Manager(employe):

    def __init__(self, name, salary):

        super().__init__(name,salary)

    def calculate_salary(self):
        self.salary+=5000

        print(self.salary) 


class Developer(employe):

    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_salary(self):
        self.salary+=2500

        print(self.salary)          


manager_instance= Manager("vvijay",150000)

developer_instance=Developer("ajay", 25000)

manager_instance.calculate_salary()

