import StudentManagement.newStudent as ns
def display():
    print("~~~~~~Students Details~~~~~~")
    for i in range(0,len(ns.RollNo)):
            print("Student Roll No.= "+ns.RollNo[i])
            print("Student Name= "+ns.Name[i])
            print("Student Address= "+ns.Address[i])
            print("Student Phone NO.= "+ns.PhoneNo[i])
            i+=1