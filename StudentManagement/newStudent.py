Name=[]
RollNo=[]
Address=[]
PhoneNo=[]

def add():
    i=0
    f=open("Sturecord.txt","+a")
    try:
        print("Enter Students Details: ")
        Name.append(input("Enter Name Of The Student: "))
        RollNo.append(input("Enter Roll No. Of Student: "))
        Address.append(input("Enter Address Of Student:"))
        PhoneNo.append(input("Enter Phone No. Of Student: "))

        f.writelines(["Student Roll No.= "+RollNo[i]+"\n"])
        f.writelines(["Student Name= "+Name[i]+"\n"])
        f.writelines(["Student Address= "+Address[i]+"\n"])
        f.writelines(["Student Phone NO.= "+PhoneNo[i]+"\n"])    
        i+=1
    except:
        if(IOError):
            print("Error In Storing Data")
        elif(IndexError):
            print("Error In Accessing Index")
        else:
            print("Record Added Successfully")