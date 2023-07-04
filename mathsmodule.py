import math as m
i=1
class Calculator:  
    i=1  
    def sqrtOfNum(self,a):
        return m.sqrt(a)
    
    def powOfNum(self,a,b):
        return m.pow(a,b)
    
    def degreeOfNum(self,a):
        return m.degrees(a)
    
    def radiansOfNum(self,a):
        return m.radians(a)
    
    def expOfNum(self,a):
        return m.exp(a)
    
    def sinOfNUm(self,a):
        return m.sin(a)
        
    def cosOfNum(self,a):
         return m.cos(a)
        
    def tanOfNum(self,a):
        return m.tan(a)
    
    def add(self,a,b):
        return(a+b)
    
    def sub(self,a,b):
        return(a-b)
    
    def mul(self,a,b):
        return(a*b)
    
    def div(self,a,b):
        return(a/b)

    def trigofunc(self):
        while self.i==1:
            print("Enter 1 value  For Sin Operation\n"\
                  "Enter 2 value For Cos Operation\n"\
                  "Enter 3 value For Tan Operation")
            c=int(input('Enter number: '))
            if(c==1):
                print(self.sinOfNUm(int(input("Enter a number for Operation: "))))
            elif(c==2):
                print(self.cosOfNum(int(input("Enter a number for Operation: "))))
            elif(c==3):
                print(self.tanOfNum(int(input("Enter a number for Operation: "))))
            else:
                print("Enter correct choice")
            a=int(input('Enter 1 to continue else any key exit: '))
            if a!=1:
                break
            else:
                self.i=a
                
    def powerfunctions(self):
        while self.i==1:
            print("Enter 1 For Squareroot Operation\n"\
                  "Enter 2 For power Operation\n")
            c=int(input('Enter number: '))
            if(c==1):
                print(self.sqrtOfNum(int(input("Enter a number for Operation: "))))
            elif(c==2):
                x=int((input("Enter first num: ")))
                y=int((input("Enter Second num: ")))
                print(self.powOfNum(x,y))
            else:
                print("Enter correct choice")
            a=int(input('Enter 1 to continue else any key exit: '))
            if a!=1:
                break
            else:
                self.i=a
        
    def arithfunc(self):
        while self.i==1:
            print("Enter 1 For Addition Operation\n"\
                "Enter 2 For Subtraction Operation\n"\
                "Enter 3 For Multiplication Operation\n"\
                "Enter 4 for Division Operation")
            c=int(input('Enter number: '))
            if(c==1):
                x=int((input("Enter first num: ")))
                y=int((input("Enter Second num: ")))
                print(self.add(x,y))
            elif(c==2):
                x=int((input("Enter first num: ")))
                y=int((input("Enter Second num: ")))
                print(self.sub(x,y))
            elif(c==3):
                x=int((input("Enter first num: ")))
                y=int((input("Enter Second num: ")))
                print(self.mul(x,y))
            elif(c==4):
                x=int((input("Enter first num: ")))
                y=int((input("Enter Second num: ")))
                print(self.div(x,y))
            else:
                print("Enter correct choice")
            a=int(input('Enter 1 to continue else any key exit: '))
            if a!=1:
                break
            else:
                self.i=a
m=Calculator()
class inavlidOption(Exception):
        def __init__(self, *msg):
            super().__init__(*msg)