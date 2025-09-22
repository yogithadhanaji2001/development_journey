class shape:

    def __init__(self,name,edge_count):

        self.name=name

        self.edge_count=edge_count


    def calculate_area(self):

        print(f"calculating {self.name} area")


class square(shape):

    def __init__(self, name, edge_count,s):
        super().__init__(name, edge_count)

        self.s=s

    def calculate_area(self):
        a=self.s**2

        print(f"area of {self.name} is {a}")     


class rectangle(shape):

    def __init__(self, name, edge_count,h,w):
        super().__init__(name, edge_count)

        self.h=h
        self.w=w

    def calculate_area(self):
        a=self.h*self.w

        print(f"area of {self.name} is {a}")
        
square_instance=square("square",4,8)

square_instance.calculate_area()

        
retangele_instance=rectangle("rectange",4,4,7)

retangele_instance.calculate_area()