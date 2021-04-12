from tkinter import *
import tkinter as tk
from tkinter import ttk


window = Tk()

window.title("Face Recogniser")
window.geometry('1200x700')
dialog_title = 'QUIT'
dialog_text= "Are you sure?"
window.configure(background="#900C3F")
window.grid_rowconfigure(0,weight =1)
window.grid_columnconfigure(0,weight=20)

banner =tk.Label(window,
                  text="Attendance System",
                  bg="#807A80",
                  fg="#ffeab0",
                  width=30,
                  height=1,
                  font=("Helvetica", 30, "bold"))  # 200 200 #text filed 550 210

banner.place(x=100, y=20)

#-profile Label------------------------------------
lbl = tk.Label(window, text="Enter ID",width=20  ,height=1  ,fg="#F6ECF6"  ,bg="#900C3F" ,font=('Helvetica', 15, ' bold ') )
lbl.place(x=1, y=150)

txt = tk.Entry(window,width=30 ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
txt.place(x=200, y=150)

#---------------2
lbl2 = tk.Label(window, text="Enter Name",width=20  ,fg="#F6ECF6"  ,bg="#900C3F" ,height=1 ,font=('Helvetica', 15, ' bold '))
lbl2.place(x=1, y=200)

txt2 = tk.Entry(window,width=30,bg="yellow"  ,fg="red",font=('times', 15, ' bold ')  )
txt2.place(x=200, y=200)


#-----------------3
"""notification"""
lbl3 = tk.Label(window, text="Notification : ",width=20  , fg="#F6ECF6"  ,bg="#900C3F" ,height=2 ,font=('Helvetica', 15, ' bold '))
lbl3.place(x=1, y=250)

message = tk.Label(window, text="" ,bg="yellow"  ,fg="red"  ,width=30  ,height=6, activebackground = "yellow" ,font=('times', 15, ' bold '))
message.place(x=200, y=250)

#-------------------------------
lbl3 = tk.Label(window, text="Attendance : ",width=20  ,fg="#F6ECF6"  ,bg="#900C3F"  ,height=2 ,font=('Helvetica', 15, ' bold'))
lbl3.place(x=50, y=500)


message2 = tk.Label(window, text="" ,fg="red"   ,bg="white",activeforeground = "green",width=30  ,height=2  ,font=('times', 15, ' bold '))
message2.place(x=250, y=500)


# --------------------functionality------------------
def clear():
   txt.delete(0, 'end')
   res = ""
   message.configure(text=res)


def clear2():
   txt2.delete(0, 'end')
   res = ""
   message.configure(text=res)


def is_number(s):
   try:
      float(s)
      return True
   except ValueError:
      pass

   try:
      import unicodedata
      unicodedata.numeric(s)
      return True
   except (TypeError, ValueError):
      pass

   return False






window.mainloop()