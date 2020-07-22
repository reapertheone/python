import tkinter as tk
import keyboard
import random

self=tk.Tk()

#variables

global total
global count
op=[]
numbers=[]




#functions
def Plus():
    i=float(str(num.get()))
    numbers.append(i)
    op.append('+')
    num.delete(0,tk.END)
    print(op)

def Minus():
    i=float(str(num.get()))
    numbers.append(i)
    op.append('-')
    num.delete(0,tk.END)
    print(op)

def Multi():
    i=float(str(num.get()))
    numbers.append(i)
    op.append('*')
    num.delete(0,tk.END)
    print(op)

def Divide():
    i=float(str(num.get()))
    numbers.append(i)
    op.append('/')
    num.delete(0,tk.END)
    print(op)


def finish():
    i=float(str(num.get()))
    numbers.append(i)
    print(numbers)
    num.delete(0,tk.END)
    count=1
    count_op=0
    op.append('=')
    print(op)
    total=numbers[0]
    while(count<len(op)):
        if(op[count_op]=='+'):
            total+=numbers[count]
        elif(op[count_op]=='-'):

            total-=numbers[count]
        elif(op[count_op]=='*'):

            total*=numbers[count]
        elif(op[count_op]=='/'):

            total/=numbers[count]     
        count+=1
        count_op+=1
       # print(count)
    print(total)
    num.insert(0,str(total))
    total=0
    count=1
    count_op=0
    numbers.clear()
    op.clear()




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