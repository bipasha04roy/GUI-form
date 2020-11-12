from tkinter import *
#from tkinter.ttk import*
import datetime
import random
import time;
from math import*
from tkinter import messagebox

windows=Tk()
windows.title("FORM")
windows.geometry('1280x768')

heading=Frame(windows,height=100,width=1366,bg='red',bd=10,relief='raise')
heading.pack(side=TOP)

lb1=Label(heading,text="BIPASHA'S  MANAGEMENT  SYSTEM",font=('Areal bold',45),bg='light green')
lb1.grid(row=0,column=0)

left=Frame(windows,height=668,width=800,bd=8)
left.pack(side=LEFT)

right=Frame(windows,height=668,width=566,bd=8)
right.pack(side=RIGHT)

lefttop=Frame(left,height=400,width=800)
lefttop.pack(side=TOP)


leftbuttom=Frame(left,height=268,width=800)
leftbuttom.pack(side=BOTTOM)


lefttopleft=Frame(lefttop,height=400,width=400,bd=8,bg='pink')
lefttopleft.pack(side=LEFT)

lefttopright=Frame(lefttop,height=400,width=400,bd=8,bg='green')
lefttopright.pack(side=RIGHT)

leftbuttomleft=Frame(leftbuttom,height=248,width=400,bd=8,bg='blue')
leftbuttomleft.pack(side=LEFT)
leftbuttomright=Frame(leftbuttom,height=248,width=400,bd=8,bg='red')
leftbuttomright.pack(side=RIGHT)

righttop=Frame(right,height=350,width=566,bd=8,bg='blue')
righttop.pack(side=TOP)

rightbuttom=Frame(right,height=318,width=566,bd=8,bg='red')
rightbuttom.pack(side=BOTTOM)


def check():
	if(var1.get()==1):
		txt1.configure(state="normal")
	elif(var1.get()==0):
		txt1.configure(state="disable")
		txt_1.set("0")
	if(var2.get()==1):
		txt2.configure(state="normal")
	elif(var2.get()==0):
		txt2.configure(state="disable")
		txt_2.set("0")
	if(var3.get()==1):
		txt3.configure(state="normal")
	elif(var3.get()==0):
		txt3.configure(state="disable")
		txt_3.set("0")

	if(var4.get()==1):
		txt4.configure(state="normal")
	elif(var4.get()==0):
		txt4.configure(state="disable")
		txt_4.set("0")

	if(var5.get()==1):
		txt5.configure(state="normal")
	elif(var5.get()==0):
		txt5.configure(state="disable")
		txt_5.set("0")

	if(var6.get()==1):
		txt6.configure(state="normal")
	elif(var6.get()==0):
		txt6.configure(state="disable")
		txt_6.set("0")

	if(var7.get()==1):
		txt7.configure(state="normal")
	elif(var7.get()==0):
		txt7.configure(state="disable")
		txt_7.set("0")

	if(var8.get()==1):
		txt8.configure(state="normal")
	elif(var8.get()==0):
		txt8.configure(state="disable")
		txt_8.set("0")

	if(var9.get()==1):
		txt9.configure(state="normal")
	elif(var9.get()==0):
		txt9.configure(state="disable")
		txt_9.set("0")


	if(var10.get()==1):
		txt10.configure(state="normal")
	elif(var10.get()==0):
		txt10.configure(state="disable")
		txt_10.set("0")


	if(var11.get()==1):
		txt11.configure(state="normal")
	elif(var11.get()==0):
		txt11.configure(state="disable")
		txt_11.set("0")


	if(var12.get()==1):
		txt12.configure(state="normal")
	elif(var12.get()==0):
		txt12.configure(state="disable")
		txt_12.set("0")


	if(var13.get()==1):
		txt13.configure(state="normal")
	elif(var13.get()==0):
		txt13.configure(state="disable")
		txt_13.set("0")

	if(var14.get()==1):
		txt14.configure(state="normal")
	elif(var14.get()==0):
		txt14.configure(state="disable")
		txt_14.set("0")

	if(var15.get()==1):
		txt15.configure(state="normal")
	elif(var15.get()==0):
		txt15.configure(state="disable")
		txt_15.set("0")


	if(var16.get()==1):
		txt16.configure(state="normal")
	elif(var16.get()==0):
		txt16.configure(state="disable")
		txt_16.set("0")


def reset():

	
	txt_1.set("")
	txt_2.set("")
	txt_3.set("")
	txt_4.set("")
	txt_5.set("")
	txt_6.set("")
	txt_7.set("")
	txt_8.set("")
	txt_9.set("")
	txt_10.set("")
	txt_11.set("")
	txt_12.set("")
	txt_13.set("")
	txt_14.set("")
	txt_15.set("")
	txt_16.set("")
	txt_17.set("")
	txt_18.set("")
	txt_19.set("")
	txt_20.set("")
	txt_21.set("")
	txt_22.set("")

	var1.set(0)
	var2.set(0)
	

	var3.set(0)

	var4.set(0)
	var5.set(0)
	var6.set(0)
	

	var7.set(0)

	var8.set(0)
	
	var9.set(0)
	var10.set(0)
	

	var11.set(0)

	var12.set(0)
	
	var13.set(0)
	var14.set(0)
	

	var15.set(0)


	var16.set(0)
	

	

def exit():
	x=messagebox.askyesno("Exit","Do you want to exit")
	if(x>0):
		windows.destroy()
		return()
	
def sum():
	a=txt_1.get()
	a=float(a)

	b=txt_2.get()
	b=float(b)

	c=txt_3.get()
	c=float(c)

	d=txt_4.get()
	d=float(d)

	e=txt_5.get()
	e=float(e)

	f=txt_6.get()
	f=float(f)

	g=txt_7.get()
	g=float(g)

	h=txt_8.get()
	h=float(h)

	i=txt_9.get()
	i=float(i)

	j=txt_10.get()
	j=float(j)

	k=txt_11.get()
	k=float(k)

	l=txt_12.get()
	l=float(l)

	m=txt_13.get()
	m=float(m)

	n=txt_14.get()
	n=float(n)

	o=txt_15.get()
	o=float(o)

	p=txt_16.get()
	p=float(p)

	total_1=a*20
	
	total_1=str(total_1)
	total1.set(total_1)

	l1=(20*a)+(45*b)+(75*c)+(15*d)+(78*e)+(20*f)+(79*g)+(27*h)
	
	l2=(20*i)+(45*j)+(75*k)+(15*l)+(78*m)+(20*n)+(79*o)+(27*p)
	
	sc=(l1+l2)*0.10
	tax=(sc+l1+l2)*0.05
	
	subtotal=(sc+tax+l1+l2)
	
	total=int(subtotal)
	l1=str(l1)
	l2=str(l2)
	sc=str(sc)
	tax=str(tax)
	subtotal=str(subtotal)
	total=str(total)


	txt_17.set(l1)
	txt_18.set(l2)
	txt_19.set(sc)
	txt_20.set(tax)
	txt_21.set(subtotal)
	txt_22.set(total)


def printbill():
	txt_bill.delete("1.0",END)
	z=random.randint(000,100)
	randomRef=str(z)
	rec.set("BILL NO:"+randomRef)	
	txt_bill.insert(END,'Reference Number:'+rec.get()+" \t"+"Date:"+dateoforder.get()+"\n")
	txt_bill.insert(END,'	PARTICULARS	' +'	QUANTITY	'+'	PRICE	'+"\n")
	txt_bill.insert(END,'........................................'+"\n")
	txt_bill.insert(END,"Iced Latte"+txt_1.get()+total1.get()+"\n")


#textbox variables for checkboxs
dateoforder=StringVar()
rec=StringVar()

txt_1=StringVar()
txt_2=StringVar()
txt_3=StringVar()
txt_4=StringVar()
txt_5=StringVar()
txt_6=StringVar()
txt_7=StringVar()
txt_8=StringVar()
txt_9=StringVar()
txt_10=StringVar()
txt_11=StringVar()
txt_12=StringVar()
txt_13=StringVar()
txt_14=StringVar()
txt_15=StringVar()
txt_16=StringVar()
##############################################################


txt_17=StringVar()

txt_18=StringVar()

txt_19=StringVar()

txt_20=StringVar()

txt_21=StringVar()

txt_22=StringVar()

total1=StringVar()

#############################################################

txt_1.set("0")
txt_2.set("0")
txt_3.set("0")
txt_4.set("0")
txt_5.set("0")
txt_6.set("0")
txt_7.set("0")
txt_8.set("0")
txt_9.set("0")
txt_10.set("0")
txt_11.set("0")
txt_12.set("0")
txt_13.set("0")
txt_14.set("0")
txt_15.set("0")
txt_16.set("0")
dateoforder.set(time.strftime("%d-%m-%Y"))




var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()


var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)


check1=Checkbutton(lefttopleft,text="Latte",variable=var1,command=check,font=('Areal bold',20))
check1.grid(row=0,column=0)

check2=Checkbutton(lefttopleft,text="Espresso",variable=var2,command=check,font=('Areal bold',20))
check2.grid(row=1,column=0)

check3=Checkbutton(lefttopleft,text="Iced Latte",variable=var3,command=check,font=('Areal bold',20))
check3.grid(row=2,column=0)

check4=Checkbutton(lefttopleft,text="Vale Coffee",variable=var4,command=check,font=('Areal bold',20))
check4.grid(row=3,column=0)

check5=Checkbutton(lefttopleft,text="Cappuccino",variable=var5,command=check,font=('Areal bold',20))
check5.grid(row=4,column=0)

check6=Checkbutton(lefttopleft,text="African Coffee",variable=var6,command=check,font=('Areal bold',20))
check6.grid(row=5,column=0)

check7=Checkbutton(lefttopleft,text="American Coffee",variable=var7,command=check,font=('Areal bold',20))
check7.grid(row=6,column=0)

check8=Checkbutton(lefttopleft,text="Iced Cappuccino",variable=var8,command=check,font=('Areal bold',20))
check8.grid(row=7,column=0)

txt1=Entry(lefttopleft,width=20,state='disable',font=('Areal bold',10),textvariable=txt_1)
txt1.grid(row=0,column=10)

txt2=Entry(lefttopleft,width=20,state='disable',font=('Areal bold',10),textvariable=txt_2)
txt2.grid(row=1,column=10)

txt3=Entry(lefttopleft,width=20,state='disable',font=('Areal bold',10),textvariable=txt_3)
txt3.grid(row=2,column=10)

txt4=Entry(lefttopleft,width=20,state='disable',font=('Areal bold',10),textvariable=txt_4)
txt4.grid(row=3,column=10)

txt5=Entry(lefttopleft,width=20,state='disable',font=('Areal bold',10),textvariable=txt_5)
txt5.grid(row=4,column=10)

txt6=Entry(lefttopleft,width=20,state='disable',font=('Areal bold',10),textvariable=txt_6)
txt6.grid(row=5,column=10)

txt7=Entry(lefttopleft,width=20,state='disable',font=('Areal bold',10),textvariable=txt_7)
txt7.grid(row=6,column=10)

txt8=Entry(lefttopleft,width=20,state='disable',font=('Areal bold',10),textvariable=txt_8)
txt8.grid(row=7,column=10)



check9=Checkbutton(lefttopright,text="Coffee Cake",variable=var9,command=check,font=('Areal bold',20))
check9.grid(row=0,column=0)

check10=Checkbutton(lefttopright,text="Red Velvet Cake",variable=var10,command=check,font=('Areal bold',20))
check10.grid(row=1,column=0)

check11=Checkbutton(lefttopright,text="Black Forest Cake",variable=var11,command=check,font=('Areal bold',20))
check11.grid(row=2,column=0)

check12=Checkbutton(lefttopright,text="Boston Cream Cake",variable=var12,command=check,font=('Areal bold',20))
check12.grid(row=3,column=0)

check13=Checkbutton(lefttopright,text="Lagos Chocolate Cake",variable=var13,command=check,font=('Areal bold',20))
check13.grid(row=4,column=0)

check14=Checkbutton(lefttopright,text="Kilburn Chocolate Cake",variable=var14,command=check,font=('Areal bold',20))
check14.grid(row=5,column=0)

check15=Checkbutton(lefttopright,text="Carlton Hill Chocolate Cake",variable=var15,command=check,font=('Areal bold',20))
check15.grid(row=6,column=0)

check16=Checkbutton(lefttopright,text="Queen's Park Chocolate Cake",variable=var16,command=check,font=('Areal bold',20))
check16.grid(row=7,column=0)

txt9=Entry(lefttopright,width=20,state='disable',font=('Areal bold',10),textvariable=txt_9)
txt9.grid(row=0,column=10)

txt10=Entry(lefttopright,width=20,state='disable',font=('Areal bold',10),textvariable=txt_10)
txt10.grid(row=1,column=10)

txt11=Entry(lefttopright,width=20,state='disable',font=('Areal bold',10),textvariable=txt_11)
txt11.grid(row=2,column=10)

txt12=Entry(lefttopright,width=20,state='disable',font=('Areal bold',10),textvariable=txt_12)
txt12.grid(row=3,column=10)

txt13=Entry(lefttopright,width=20,state='disable',font=('Areal bold',10),textvariable=txt_13)
txt13.grid(row=4,column=10)

txt14=Entry(lefttopright,width=20,state='disable',font=('Areal bold',10),textvariable=txt_14)
txt14.grid(row=5,column=10)

txt15=Entry(lefttopright,width=20,state='disable',font=('Areal bold',10),textvariable=txt_15)
txt15.grid(row=6,column=10)

txt16=Entry(lefttopright,width=20,state='disable',font=('Areal bold',10),textvariable=txt_16)
txt16.grid(row=7,column=10)



lb1=Label(leftbuttomleft,text="Cost of Drinks",font=('Areal bold',20))
lb1.grid(row=0,column=0)

txt17=Entry(leftbuttomleft,width=20,state='disable',font=('Areal bold',10),textvariable=txt_17)
txt17.grid(row=0,column=4)

lb2=Label(leftbuttomleft,text="Cost of Cakes",font=('Areal bold',20))
lb2.grid(row=1,column=0)

txt18=Entry(leftbuttomleft,width=20,state='disable',font=('Areal bold',10),textvariable=txt_18)
txt18.grid(row=1,column=4)

lb3=Label(leftbuttomleft,text="Sevice charge",font=('Areal bold',20))
lb3.grid(row=2,column=0)

txt19=Entry(leftbuttomleft,width=20,state='disable',font=('Areal bold',10),textvariable=txt_19)
txt19.grid(row=2,column=4)


lb4=Label(leftbuttomright,text="Tax",font=('Areal bold',20))
lb4.grid(row=0,column=0)

txt20=Entry(leftbuttomright,width=20,state='disable',font=('Areal bold',10),textvariable=txt_20)
txt20.grid(row=0,column=4)

lb5=Label(leftbuttomright,text="Sub Total",font=('Areal bold',20))
lb5.grid(row=1,column=0)

txt21=Entry(leftbuttomright,width=20,state='disable',font=('Areal bold',10),textvariable=txt_21)
txt21.grid(row=1,column=4)

lb6=Label(leftbuttomright,text="Total",font=('Areal bold',20))
lb6.grid(row=2,column=0)

txt22=Entry(leftbuttomright,width=20,state='disable',font=('Areal bold',10),textvariable=txt_22)
txt22.grid(row=2,column=4)


lbl_bill=Label(righttop,text='Bill',bd=2,font=('Areal bold',20))
lbl_bill.grid(row=0,column=0,sticky=W)

txt_bill=Text(righttop,font=('Areal bold',10),bd=8,width=50,height=25)
txt_bill.grid(row=1,column=0)

btn1=Button(rightbuttom,text="TOTAL",font=('Areal bold',15),command=sum)
btn1.grid(row=1,column=0)
btn2=Button(rightbuttom,text="RECEIPT",font=('Areal bold',15),command=printbill)
btn2.grid(row=1,column=1)
btn3=Button(rightbuttom,text="RESET",font=('Areal bold',15),command=reset)
btn3.grid(row=1,column=2)
btn4=Button(rightbuttom,text="EXIT",font=('Areal bold',15),command=exit)
btn4.grid(row=1,column=3)

windows.mainloop()