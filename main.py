#OOPS - Object Oreinted Programming Structure

class Student():
    #properties/ attributes
    #inbuilt function
    def __init__(self,name,age,grade,favColour,hobby):
        self.name=name
        self.age = age
        self.grade = grade
        self.favColour = favColour
        self.hobby = hobby
        self.intro = " "
    
    #function
    def showDetails(self):
        print("the details of the students are: ")
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Grade : ", self.grade)
        print("Favourite Colour : ", self.favColour)
        print("Hobby : ", self.hobby)
        print()
    
    def intro_student(self):
        self.intro =input("please introduce yourself : ")
        print(self.intro)
        print()

#objects for the class

s1 = Student("Ijin Yu", 19,"13th grade","N/A", "N/A")

#objectName.functionNAme() - calling the functions

s1.showDetails()
s1.intro_student()

s2 = Student("Sukeo Ko", 19, "13th grade", "Blue", "MMA")

s2.showDetails()
s2.intro_student()