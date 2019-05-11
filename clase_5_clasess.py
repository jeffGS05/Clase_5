class First: # empty class
    pass
a=First()
print(type(a))

class sec:
    def __init__(self): # this example show us how to create method without parameters, this allow call it an used latter
        print('contructor ejecutando')
a=sec()
print(a)

class duck:
    def __init__(self,nombre):
        self.duck_nombre=nombre
    def quack(self):
        print('Quakkk')
    def walk(self):
        print('Walk like duck')
donald=duck('Donald')
donald.quack()
donald.walk()
print('cual es tu nombre ' , donald.duck_nombre)

