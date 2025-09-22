class SuperHero:

    name:str

    super_power:str

    universe:str



    def set_super_hero(self,name,super_power,universe):

        self.name=name

        self.super_power=super_power

        self.universe=universe

    def display_super_hero(self):

        print(self.name,self.super_power,self.universe) 


batman_instance=SuperHero()

batman_instance.set_super_hero("batman","fly,run","dc")

minnal_instance=SuperHero()

minnal_instance.set_super_hero("minnalmuraly","run","basil universe")

batman_instance.display_super_hero()
minnal_instance.display_super_hero()