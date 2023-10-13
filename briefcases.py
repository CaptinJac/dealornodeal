### All briefcases are the same, the only diffrence is what case number is assigned
### and what each case contains. In order to populate each case I have made them an 
### Object. That way we can minipulate them much easier compared to being dictionaries
### or lists.

#begin code

from random import randint

class Briefcase:            #Creating the class for the briefcase
    def __init__(self, number, value):          #Each case has 1 number and 1 value
        self.number = number
        self.value = value

    def __str__(self):
        return f"{self.number}({self.value})"           #If we print case as a string for debug purposes  # noqa: E501

def create_cases(values):           #Create each case with a random value 
    cases = []
    for x in range(len(values)):
        randomvalue = values[randint(0, len(values) - 1)]
        briefcase = Briefcase(x + 1, randomvalue)
        values.remove(randomvalue)
        cases.append(briefcase)
    return cases          #returns a list of all cases with random values


### Simple Script thaat creates and randomizes the values that each case can have
