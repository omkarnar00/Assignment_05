class Calculator():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        sum=0
        sum=self.num1 + self.num2
        print(sum)
    
    def subtract(self):
        sub=0
        sub=self.num1 - self.num2
        print(sub)
    

    def multiply(self):
       mul=0
       mul=self.num1 * self.num2
       print(mul)
    
    def divide(self):
      div=0
      div=self.num1 / self.num2
      print(div)  

obj=Calculator(94,10)       
obj.add()
obj.subtract()
obj.multiply()
obj.divide()


## output: 104
# 84
# 940
# 9.4