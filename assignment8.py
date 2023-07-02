class A:
    def __init__(self,x,y,z):
        self.__x=x
        self._y=y
        self.z=z
    def display(self):
        print("This is a class A display()")
        print("Value of x is %d"%(self.__x))
        print("Value of y is %d"%(self._y))
        print("value of z is {}".format(self.z))

class B(A):
    def display(self):
        super().display()
        print("This is a class B display()")
        try:
            print("Value of x is %d"%(self.__x))
        except AttributeError: 
            print("YOU CAN'T ACCESS PRIVATE ELEMENTS")
        print("Value of y is %d"%(self._y))
        print(f"value of z is {self.z}")


b=B(40,50,60)
b.display()
