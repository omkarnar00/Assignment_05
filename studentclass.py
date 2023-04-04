class Student:
    def __init__(self):
        self.__name=None
        self.__rollnumber=None

    def getname(self):
        return self.__name
    
    def setname(self,name):        
        self.__name=name

    def getrollnumber(self):
        return self.__rollnumber
    
    def setrollnumber(self,rollnumber):        
        self.__rollnumber=rollnumber   

s=Student()            
print(s.getname())
s.setname("omkar")
print(s.getname())
print(s.getrollnumber())
s.setrollnumber(10)
print(s.getrollnumber())

# output:
# None
# omkar
# None
# 10