'''Definisikan Class'''


class MyClass():
    attribute = 'Aku adalah atribut kelas'
    
    def __init__(self, parameter1,parameter2):
        self.param1 =parameter1
        self.param2 =parameter2
    
    def instance_method(self):
        return 'Ini adalah instance method dengan ' + self.param1 + ' dan ' +self.param2 +'.'
    
    @classmethod
    def class_method(cls):
        return 'Ini adalah class method ' + cls.attribute+'.'
    @staticmethod
    def static_method():
        return 'Langsung return'
    
    
    
    
benda_1 = MyClass('buah','hewan')
print(benda_1.attribute)

print(benda_1.instance_method())
print(benda_1.class_method())
print(benda_1.static_method())