class person:
    count = 0 
    def __init__ (self,name,age, collegename):
        self.name = name
        self.age = age
        self.collegename = collegename
        person.count += 1
#accessing the class variables using the name of the class
person1 = person("Madhura",25,"APSWRS")
person2 = person("Elisha",30,"APSWRS")
person3 = person("Mahima",27,"APSWRS")
print(person.count)
print(person1.name)
print(person2.age)
print(person1.collegename)
print(person3.name)