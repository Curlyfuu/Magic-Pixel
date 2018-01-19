from tkinter import *
def to_Hex(a):
	b=hex(a)
	c=str(b)
	if a<16:
		c=c[2:]
		c='0'+c
	else:
		c=c[2:]
	return c
def to_Color(a,b,c):
	i=to_Hex(a)
	j=to_Hex(b)
	k=to_Hex(c)
	m='#'+k+i+j
	return m

window=Tk()
window.title('my window')
window.geometry('600x400')


var1=IntVar()
var2=IntVar()
var3=IntVar()
var='#fff'

l_1=Label(window,bg='#f0f',width=20,text='Azaleine: 0')
l_1.pack()
def print_selection1(v):
	l_1.config(text='Azaleine: '+v)
	var=to_Color(var1.get(),var2.get(),var3.get())
	l_4.config(bg=var,text=var)
s1=Scale(window,label='try me',from_=0,to=255,orient=HORIZONTAL,
	length=400,showvalue=1,variable=var1,tickinterval=20,
	resolution=1,command=print_selection1)

s1.pack()

l_2=Label(window,bg='yellow',width=20,text='Yellow: 0')
l_2.pack()
def print_selection2(v):
	l_2.config(text='Yellow: '+v)
	var=to_Color(var1.get(),var2.get(),var3.get())
	l_4.config(bg=var,text=var)


s2=Scale(window,label='try me',from_=0,to=255,orient=HORIZONTAL,
	length=400,showvalue=0,variable=var2,tickinterval=20,
	resolution=1,command=print_selection2)
s2.pack()
l_3=Label(window,bg='cyan',width=20,text='Cyan: 0')
l_3.pack()
def print_selection3(v):
	l_3.config(text='Cyan: '+v)
	var=to_Color(var1.get(),var2.get(),var3.get())
	l_4.config(bg=var,text=var)

s3=Scale(window,label='try me',from_=0,to=255,orient=HORIZONTAL,
	length=400,showvalue=0,variable=var3,tickinterval=0,
	resolution=1,command=print_selection3)
s3.pack()


l_4=Label(window,bg='#000',width=20,height=8,text='')
l_4.pack()

window.mainloop()
