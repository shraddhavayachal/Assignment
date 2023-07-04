import tkinter as tk
import webbrowser as wb
obj=tk.Tk()
e=tk.Entry(obj,font=("Times new Roman",30),
           width=30)
e.grid()

def display():
    s=e.get()
    print(s)
    wb.open("https://www.youtube.com/search?q="+s)
    # wb.open("https://www.spotify.com/")
b=tk.Button(obj,text="Open Youtube",font=("Times New Roman",30),command=display,bg="blue",
             activebackground="orange")
# b1=tk.Button(obj,text="Open Spotify",font=("Times New Roman",30),command=display,bg="purple",
#             activebackground="cyan")
b2=tk.Button(obj,text="Close",font=("Times New Roman",30),command=obj.destroy,bg="purple",
            activebackground="yellow")
b.grid(row=1,column=0)
# b1.grid(row=2,column=0)
b2.grid(row=3,column=0)
obj.mainloop()