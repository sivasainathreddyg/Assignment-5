class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        a=self.x*self.x
        b=self.y*self.y
        c=self.z*self.z
        sum_total=f"square of numbers:{a+b+c}"
        return sum_total

    
point=Point(1,3,5)
print(point.sqSum())
