class User:
    def __init__(self,c_number1,c_number2):
        self.c_number1 = c_number1
        self.c_number2 = c_number2
    
    def getResults(self):
        adding = self.c_number1 + self.c_number2
        subtracting = self.c_number1 - self.c_number2
        multiplying = self.c_number1 * self.c_number2
        dividing = self.c_number1 / self.c_number2
        return Results(adding, subtracting, multiplying, dividing)

class Results:
    def __init__(self,adding,subtracting,multiplying,dividing):
        self.adding = adding
        self.subtracting = subtracting
        self.multiplying = multiplying
        self.dividing = dividing
        
    def getAdd(self):
        return self.adding
    
    def getSub(self):
        return self.subtracting

    def getMult(self):
        return self.multiplying

    def getDiv(self):
        return self.dividing

#test case
user = User(complex(1,1),complex(2,2))
results = user.getResults()
print(results.getAdd())
print(results.getSub())
print(results.getMult())
print(results.getDiv())