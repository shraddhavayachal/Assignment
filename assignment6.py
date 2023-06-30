def ds(rollno,name):
    ls=[]
    ls.append((rollno,name))
    print("The list is:",ls)
    t=(rollno,name)
    print("The tuple is:",t)
    s=set()
    s={(rollno,name)}
    print("The set is:",s)
    d={
        "rollno":rollno,
        "name":name
    }
    print("The dictionary is:",d)
    ls[0] = (30,"Raj")
    t=(30,"Raj")
    s.pop()
    s.add((30,"Raj"))
    d["rollno"]=30
    d["name"]="Raj"
    print("The updated list is:",ls)
    print("The updated tuple is:",t)
    print("The updated set is:",s)
    print("The updated dictionary is:",d)
ds(34,"Shraddha")