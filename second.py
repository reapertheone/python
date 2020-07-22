import tkinter as tk
import random

self=tk.Tk()
self.geometry("200x40")
self.title("Szamologep")

#variables
op='none'

temp=[]

op=[]



def Plus():
    op.append('+')
    i=int(str(num.get()))
    temp.append(i)
    print(op)
    print (temp)
    num.delete(0,tk.END)
    
 
def Minus():
    op.append('-')
    i=int(str(num.get()))
    temp.append(i)
    print(op)
    print (temp)
    num.delete(0,tk.END)

def Multi():
    op.append('*')
    i=int(str(num.get()))
    temp.append(i)
    print(op)
    print (temp)
    num.delete(0,tk.END)

def Divide():
    op.append('/')
    i=int(str(num.get()))
    temp.append(i)
    print(op)
    print (temp)
    num.delete(0,tk.END)

def finish():
    count=0
    c=0
    i=int(str(num.get()))
    temp.append(i)
    op.append('=')
    print(op)
    print (temp)
    while(op[count]!='='):
        if(op[count]=='+'):
           c+=temp[count]
        elif(op[count]=='-'):
            c-=temp[count]
        elif(op[count]=='*'):
            c*=temp[count]
        elif(op[count]=='='):
            num.insert(0,str(c))
        count+=1
    num.insert(0,str(c))
    count=0
    op.clear()
    temp.clear()
    c=0

#init widgets
num=tk.Entry(width=50)
plus=tk.Button(self, text="plus", padx=80, pady=50, command=Plus)
minus=tk.Button(self,text="-",padx=80, pady=50,command=Minus)
multi=tk.Button(self,text="*",padx=80, pady=50,command=Multi)
divide=tk.Button(self,text="/",padx=88, pady=50,command=Divide)
equate=tk.Button(self,text="=",padx=80, pady=50,command=finish)


#design
num.grid(row=0,column=0,columnspan=3)
plus.grid(row=1,column=0)
minus.grid(row=1,column=1)
multi.grid(row=1,column=2)
divide.grid(row=2,column=0)
equate.grid(row=2,column=1)

self.update()
self.mainloop()