class Book:

    def __init__(self,name,auther,price):

        self.name=name

        self.auther=auther

        self.price=price

    def __str__(self):
        
        return self.name

        


    def display_book(self):

        print(self.name,self.auther,self.price)




book_instance1= Book("goat life", "benyamain",560)

# book_instance1.display_book()

print(book_instance1)

