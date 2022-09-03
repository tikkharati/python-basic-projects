from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -1") 
st=Tk()
st.title("shutdowm app")
st.geometry("500x500")
st.config(bg="Blue")
r_button=Button(st,text="restart",font=("mickey",12,"bold"),relief=RAISED,cursor="plus",command=restart )
r_button.place(x=120,y=400,height=40,width=100)

rt_button=Button(st,text="restart time",font=("mickey",12,"bold"),relief=RAISED,cursor="plus",command=restart_time )
rt_button.place(x=250,y=400,height=40,width=100)

lg_button=Button(st,text="log out",font=("mickey",12,"bold"),relief=RAISED,cursor="plus" ,command=logout)
lg_button.place(x=120,y=300,height=40,width=100)

lo_button=Button(st,text="log in",font=("mickey",12,"bold"),relief=RAISED,cursor="plus" )
lo_button.place(x=120,y=200,height=40,width=100)
st.mainloop()