
class Employee(object):
    def __init__(self, sirname):
        self.__sirname = sirname
        self.__pay = 0

    def addSalary(self, value):
        self.__pay += value

    def pay(self):
        return self.__pay