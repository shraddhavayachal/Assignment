import StudentManagement.newStudent as ns
def dele():
    rn=input("Enter The Roll NO. To Delete Details: ")
    i=ns.RollNo.index(rn)
    ns.Name.pop(i)
    ns.RollNo.pop(i)
    ns.Address.pop(i)
    ns.PhoneNo.pop(i)
    print("Record is Deleted Successfully!!!!")