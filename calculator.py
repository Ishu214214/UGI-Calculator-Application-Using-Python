from tkinter import *
import time
from tkinter import messagebox
from functools import reduce

expression = ""
i=0
'''time auto maticis count hoga ya function sa'''
def counter_fun(label1):
    def count():
        global i
        i+=1
        label1.config(text=str(i))
        label1.after(1000,count)
    count()

j=0 
a=0
a1=0
def press_button():
    #print('button press')
    global a
    if(a==0):
        messagebox.showinfo('SUBMIT🍃🍃','Respond WIL COUNT AT RIGHT BOTTOM 👇👇👇')
        a+=1
        
    global j
    j+=1
    l2.config(text=str(j))
    
    enter_data=e1.get()
    print(enter_data)
    e1.delete(0,END)


def on_clicks(text):
    entry.delete(0, END) 
  
    
def press_button1(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
 

def factorial(n):
    try:
        return 1 if (n==1 or n==0) else n * factorial(n - 1)
    except:
        equation.set(" error ")
        #e1.set("error")

jj=0 
def calculate():
    try:
        global jj
        result=factorial(int(e1.get()))
        e1.delete(0,END)
        e1.insert(jj,result)
    except:
        equation.set(" error ")
        #e1.set("error")

    
def equalpress():
    try:
        global a1
        if(a1==0):
            messagebox.askquestion('INFORAMATIONS 🤟🤟','Are YOU SURE TO RUN YOUR FIRST CALCULATION 🙂🙂')
            a1+=1
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""    
 

'''root user ma windowes create kar raha ha'''        
root=Tk()
root.geometry('1500x1500')
root.title('CALCULATOR')
root.configure(background="aquamarine")

#lable
l1 = Label( root,text="CALCULATE " ,height=2 ,width=90 ,bg="#FFFDD0"  , fg="#F70D1A"  , font = ("Times New Roman" ,23, 'bold') )
#BUTTON COUNT
l2 = Label( root,text="0" ,height=2 ,width=3 ,bg="#00BFFF"  , fg="#000000" ,  relief= RAISED , font = ("Times New Roman" ,28, 'bold') )
#TIME COUNT
l3 = Label( root,text="0" ,height=1 ,width=3 ,bg="Yellow"  , fg="red" ,  relief= RAISED , font = ("Times New Roman" ,28, 'bold') )

#text
t1 = Label( root,text="Respond from users where output and input will store  ......"  ,bg="aquamarine" ,   font = ("Times New Roman" ,18, 'bold') )
t2 = Label( root,text="Input from numbers  .."  ,bg="aquamarine" ,   font = ("Times New Roman" ,18, 'bold') )
#lable for numbers
m2 = Label( root,text="" ,height=31 ,width=55 ,bg="white" , relief= RAISED )
#bouttons
s0 = Button( root,text=" 0" ,height=2 ,width=3 ,bg="Silver"  , fg="black"  , font = ("Times New Roman" ,23, 'bold'),command=lambda:press_button1(0) )
s1 = Button( root,text=" 1" ,height=2 ,width=3 ,bg="Silver"  , fg="black"  , font = ("Times New Roman" ,23, 'bold'),command=lambda:press_button1(1) )
s2 = Button( root,text=" 2" ,height=2 ,width=3 ,bg="Silver"  , fg="black"  , font = ("Times New Roman" ,23, 'bold'),command=lambda:press_button1(2) )
s3 = Button( root,text=" 3" ,height=2 ,width=3 ,bg="Silver"  , fg="black"  , font = ("Times New Roman" ,23, 'bold'),command=lambda:press_button1(3) )
s4 = Button( root,text=" 4" ,height=2 ,width=3 ,bg="Silver"  , fg="black"  , font = ("Times New Roman" ,23, 'bold'),command=lambda:press_button1(4) )
s5 = Button( root,text=" 5" ,height=2 ,width=3 ,bg="Silver"  , fg="black"  , font = ("Times New Roman" ,23, 'bold'),command=lambda:press_button1(5) )
s6 = Button( root,text=" 6" ,height=2 ,width=3 ,bg="Silver"  , fg="black"  , font = ("Times New Roman" ,23, 'bold'),command=lambda:press_button1(6) )
s7 = Button( root,text=" 7" ,height=2 ,width=3 ,bg="Silver"  , fg="black"  , font = ("Times New Roman" ,23, 'bold'),command=lambda:press_button1(7) )
s8 = Button( root,text=" 8" ,height=2 ,width=3 ,bg="Silver"  , fg="black"  , font = ("Times New Roman" ,23, 'bold'),command=lambda:press_button1(8) )
s9 = Button( root,text=" 9" ,height=2 ,width=3 ,bg="Silver"  , fg="black"  , font = ("Times New Roman" ,23, 'bold'),command=lambda:press_button1(9) )
sc = Button( root,text="." , height=2 ,width=3 ,bg="silver"  , fg="red"  ,   font = ("Times New Roman" ,23, 'bold'),command=lambda:press_button1('.') )
sd = Button( root,text="= " ,height=2 ,width=3 ,bg="silver"  , fg="orange"  ,font = ("Times New Roman" ,23, 'bold'),command=equalpress )
o0 = Button( root,text=" +" ,height=2 ,width=3 ,bg="orange"  , fg="black"  , font = ("Times New Roman" ,23, 'bold'),command=lambda:press_button1('+') )
o1 = Button( root,text=" -" ,height=2 ,width=3 ,bg="orange"  , fg="black"  , font = ("Times New Roman" ,23, 'bold'),command=lambda:press_button1('-') )
o2 = Button( root,text=" *" ,height=2 ,width=3 ,bg="orange"  , fg="black"  , font = ("Times New Roman" ,23, 'bold'),command=lambda:press_button1('*') )
o3 = Button( root,text=" /" ,height=2 ,width=3 ,bg="orange"  , fg="black"  , font = ("Times New Roman" ,23, 'bold'),command=lambda:press_button1('/') )
o4 = Button( root,text=" %" ,height=2 ,width=3 ,bg="orange"  , fg="black"  , font = ("Times New Roman" ,23, 'bold'),command=lambda:press_button1('%') )
o5 = Button( root,text="sqr",height=2 ,width=3 ,bg="orange" , fg="black"  , font = ("Times New Roman" ,23, 'bold'),command=lambda:press_button1('**') )
o6 = Button( root,text="fact",height=2 ,width=3,bg="orange" , fg="black"  , font = ("Times New Roman" ,23, 'bold'),command=calculate )
m1 = Button( root,text="AC",height=2 ,width=3 ,bg="#FF4500",  fg="white"  , font = ("Times New Roman" ,23, 'bold'),command=lambda:on_clicks('🧹') )

#TEXT ENTERY
equation = StringVar()
entry=Entry(root,textvariable=equation   ,width=20,bg="white" , fg="black" , relief= RAISED , font = ("Times New Roman" ,23, 'bold') )
 
e1=Entry(root, textvariable=equation  ,width=32, bg='white' ,  fg ='black', relief= RAISED , font = ("Times New Roman" ,28, 'bold') )

#SUBMIT VALUE
b1=Button(root, text ="Submit" , height=1, width=8,   bg='#0000FF' , fg='#E5E4E2' ,  relief= RAISED , font = ("Times New Roman" ,28, 'bold'),command=press_button )

'''ya function count kar raha ha or call kar raha ha uupar warala function ko'''
counter_fun(l3)

entry.place(x=10,y=450)

t1.place(x=10,y=145)
t2.place(x=10,y=415)

m2.place(x=1005,y=105)

l1.place(x=0,y=0)
l2.place(x=1360,y=730)
l3.place(x=0,y=0)

e1.place(x=5,y=190)
b1.place(x=120,y=650)

sd.place(x=1320,y=530)
sc.place(x=1120,y=530)
s0.place(x=1220,y=530)
s1.place(x=1120,y=230)
s2.place(x=1220,y=230)
s3.place(x=1320,y=230)
s4.place(x=1120,y=330)
s5.place(x=1220,y=330)
s6.place(x=1320,y=330)
s7.place(x=1120,y=430)
s8.place(x=1220,y=430)
s9.place(x=1320,y=430)

o0.place(x=1020,y=530)
o1.place(x=1020,y=430)
o2.place(x=1020,y=330)
o3.place(x=1020,y=230)
o4.place(x=1120,y=115)
o5.place(x=1220,y=115)
o6.place(x=1320,y=115)

m1.place(x=1020,y=115)

root.mainloop()