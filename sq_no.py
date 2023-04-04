class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        sum=0
        self.x=self.x * self.x
        self.y=self.y * self.y
        self.z=self.z * self.z

        sum=self.x + self.y + self.z 
        return sum

obj=Point(1,3,5)  
result=obj.sqSum()
print(result)

## output: 35