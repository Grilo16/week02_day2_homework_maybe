from random import choice as random_choice_generator

class People():
    def __init__(self):
        self.ability_to_draw_diagrams = self.reasonable_choices()
        
    def reasonable_choices(self):
        choices = ["Yay diagrams !!", "Hmm not a fan, but ok"]
        choice =  random_choice_generator(choices)
        return choice
        
    def __str__(self):
        return f"Hi, my name is {self.name}, im {self.age} years old and when I need to make a diagram i think : {self.ability_to_draw_diagrams}, its a pleasure to meet you =)"
    

class Someone_else(People):
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age
         
class Tom(People):
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age

    def reasonable_choices(self):
        output = ""
        choices = ["Oh god no, help me!", "System overloading begin restart procedures", "OH NO NONO NO", "I can't do this, quit?", "NO dont", "Rebooting", "Finding alternative solution"]
        for choice in choices:
            output += f"{choice}\n"
        return output
        


tom = Tom("Tom", 30)
someone_else = Someone_else("Salvador dali", 118)

print(someone_else)
print()
print(tom)