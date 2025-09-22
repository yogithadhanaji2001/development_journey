class Animal:

    def sound(self):
        print("animal sound method")

class cat(Animal):

    def sound(self):
        super().sound()

        print("cat sound meow")

cat_inistance=cat()

cat_inistance.sound()
    
