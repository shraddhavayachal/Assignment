import StudentManagement.newStudent as ns
def search():   
    rn=input("Enter The Roll NO. To See Details: ")
    i=ns.RollNo.index(rn)
    print("Student Roll No.= "+ns.RollNo[i])
    print("Student Name= "+ns.Name[i])
    print("Student Address= "+ns.Address[i])
    print("Student Phone NO.= "+ns.PhoneNo[i])