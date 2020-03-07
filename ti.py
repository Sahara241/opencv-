import sys
import tkinter as tk
import cv2
import opencv35

def callback():
    txt=var.get()
    #label2=tk.Label(r,text=txt).pack()
    print(txt)
    if txt:
        opencv35.callbackfun()
    return
    
r=tk.Tk()
var=tk.StringVar()

r.geometry('550x250+500+200')
r.title('register')


#label=tk.Label(r, text='File name').pack()
fbutton=tk.Button(r,text='face and object detect',command = callback,fg='black',bg='white').pack()

mbutton=tk.Button(r,text='add new face',command = callback,fg='black',bg='white').pack()


mEntry=tk.Entry(r,textvariable=var).pack()

r.mainloop()
