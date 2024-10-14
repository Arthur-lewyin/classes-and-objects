class Superhero():
    def __init__(self,SuperheroName,realName,Age,SuperPower,rating):
        self.SuperheroName = SuperheroName
        self.RealName = realName
        self.Age = Age
        self.Superpower = SuperPower
        self.rating = rating
    
    def ShowDetails (self):
        print("Superhero Name: ", self.SuperheroName)
        print("Real name : " , self.RealName)
        print("Age : ", self.Age)
        print("SuperPower : ", self.Superpower)
        print("Score out of 10 :",self.rating,"/10")
        print()
    

h1 = Superhero("De arm","Fransje", 17, "strength",-100)
h2 = Superhero("Joe speedboot", "??? Ratzinger", 16, "Stupidity", 10 )
h3 = Superhero("Johnny","Christoff", 16, "Friendship",6)

h1.ShowDetails()
h2.ShowDetails()
h3.ShowDetails()