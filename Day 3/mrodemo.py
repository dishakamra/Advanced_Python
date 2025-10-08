class Flyer:
    def action(self):
        return "fly"
    
class Swimmer:
    def action(self):
        return "swim"

class Duck(Flyer, Swimmer):
    pass

d = Duck()
#print(d.action())
print(Duck.mro())
