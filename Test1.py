import math
class perimeter:
   
   


   def __init__(self,l,w,r,a):
       self.length = l
       self.width = w
       self.radius = r
       self.perimeter = a

   def PerimeterofRectangle(self):
       perimeter1 = (2*self.length) + (2*self.width)
       print ("Perimeter of Rectangle:",perimeter1,"m")

   def circumferenceofcircle(self):
       perimeter2 = (2*math.pi*self.radius)
       print ("Circumference of Circle:",perimeter2,"m")

   def PerimeterofaEqualateralTriangle(self):
       perimeter3 = (3*self.perimeter)
       print ("PerimeterofTEqualateralTriangle:",perimeter3,"inch")

    
    


    

