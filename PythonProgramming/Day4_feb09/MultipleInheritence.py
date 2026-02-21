#multiple inheritance is 2 parents and one child class


class parent1:
    pass
class parent2:
    pass
class child(parent1,parent2):
    pass


class Father:
    def driving(self):
        print("Father has the driving skills to drive")

class Mother:
    def cooking(self):
        print("Mother has the cooking skills")

class Child(Father,Mother):
    def bothskills(self):
        print("Child has the skills to study")
        print("Child has both skills of driving and cooking")
c=Child()
c.driving()
c.cooking()
c.bothskills()