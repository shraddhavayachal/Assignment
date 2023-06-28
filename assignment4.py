print("Break and While With Else Statement")
i=1                
while i<=10:
    if i==5:
        break
    else:
        print(i)
        i+=1
else:
    print("It has a break") 


print("Pass and For With Else Statement")
str="Shraddha"
for i in str:
    if i=="l":
       pass         
    else:
        print(i)
else:
    print("It has a Pass")  
print()


print("Continue Statement")
i=1
while i<=10:
    if i==6:
        i+=1
        continue     
    print(i)
    i+=1
print()
