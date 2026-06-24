from typing import TypeDict
 
class Person(TypeDict):
    name : str
    age : int
    
new_person = Person(name="xyc",age="29")

