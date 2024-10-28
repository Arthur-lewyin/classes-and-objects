class Pets():
    def __init__(self,petName,species,petAge):
        self.pet_name = petName
        self.species = species
        self.pet_age = petAge
        self.pet_adoption = ""

    def showDetails(self):
        print("Animal name: " + self.pet_name)
        print("Animal species: " + self.species)
        print("Animal age: ", self.pet_age)
        print()

    def adoptionStatus(self):
        self.pet_adoption =input("Answer yes or no : ")
        if self.pet_adoption == "yes" or self.pet_adoption == "no":
            print(self.pet_adoption)
            print()
        else:
            print("you must only enter yes or no")
        

P1 = Pets("Bangchan", "Wolf", 5)
P2 = Pets("Lee Know", "bunny", 29)
P3 = Pets("Changbin", "pig",15)
P4 = Pets("Hyunjin", "ferret", 7)
P5 = Pets("Han", "chipmunk", 13 )
P6 = Pets("Felix", "chick", 1 )
P7 = Pets("Seungmin", "puppy", 0.3)
P8 = Pets("I.N.", "fox", 6)

P1.showDetails()
P2.showDetails()
P3.showDetails()
P4.showDetails()
P5.showDetails()
P6.showDetails()
P7.showDetails()
P8.showDetails()

P1.adoptionStatus()
P2.adoptionStatus()
P3.adoptionStatus()
P4.adoptionStatus()
P5.adoptionStatus()
P6.adoptionStatus()
P7.adoptionStatus()
P8.adoptionStatus()
