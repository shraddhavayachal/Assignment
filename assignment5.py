print("Enter any 5 numbers you want to store in the list:")
num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())
num5=int(input())
print()

ls=[num1,num2,num3,num4,num5]
print("Elements Present In The List Are :",ls)
print("1. Sum Of All The Elements In The List :",sum(ls))
print("2. Smallest Number is :",min(ls))
print("3. Largest Number is :",max(ls))
ls.sort()
print("4. List In Ascending Order :",ls)
ls.reverse()
print("5. List In Descending Order :",ls)
tuple1=tuple(ls)
print("6. List After Coversion Into Tuple :",tuple1)
ls.clear()
print("7. List Deleted: ",ls)
