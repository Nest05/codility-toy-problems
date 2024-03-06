class Person:


    name= ""
    age = 0
    color = ""
    body_mass = 0

    @classmethod
    def walk(cls, person):
        print(f"{person.name} is walking away")
    
    @staticmethod
    def eat(person):
        print(f"{person.name} is eating")


person_one = Person()
person_one.name = "Clare Oparo"
person_one.age = 50
person_one.color = "chocolate"
person_one.body_mass = 60

person_two = Person()
person_two.name = "Mariam Senzia"
person_two.age = 26
person_two.color = "lightskin"
person_two.body_mass = 60


print(f"{person_one.name} is {person_one.age} years old")
print(f"{person_two.name} is {person_two.age} years old")

person_one.walk(person_one)
person_two.eat(person_two)