class student:
    def display(self):
        print(self.name)
        print(self.age)
s1= student()
s1.name="Rahul"
s1.age=20
s2= student()
s2.name="sony"
s2.age=21
s1.display()
#s2.display()
class AIPA(student):
    def display(self):
        print("student of AIPA")
