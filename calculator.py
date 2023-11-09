#Created on Tue Oct 24 17:16:09 2023
# Simple Calculator for user

from tkinter import *

mw = Tk()
mw.title("CALCULATOR")

#calculation function 
def calculation():
    exp=display.get()
    try:
        result=str(eval(exp))
        clear()
        display.inset(0,result)
    except:
        display.delete(0,END)
        display.insert(0,result)

#For clearing display 
def clear():
    display.delete(0,END)

#Entering values function 
def btn_clk(num):
    cur_num=display.get()
    clear()
    f_num=cur_num + num
    display.insert(0, f_num)
    

#creating buttons 

display = Entry(mw, width=20, font=("Arial",28), justify=RIGHT)


btn_0 = Button(mw, text="7", padx=36, pady=10, font=("Arial",14),command=lambda:btn_clk("7"))
btn_1 = Button(mw, text="8", padx=36, pady=10, font=("Arial",14),command=lambda:btn_clk("8"))
btn_2 = Button(mw, text="9", padx=36, pady=10, font=("Arial",14),command=lambda:btn_clk("9"))

btn_3 = Button(mw, text="4", padx=36, pady=10, font=("Arial",14),command=lambda:btn_clk("4"))
btn_4 = Button(mw, text="5", padx=36, pady=10, font=("Arial",14),command=lambda:btn_clk("5"))
btn_5 = Button(mw, text="6", padx=36, pady=10, font=("Arial",14), command=lambda:btn_clk("6"))

btn_6 = Button(mw, text="1", padx=36, pady=10, font=("Arial",14),command=lambda:btn_clk("1"))
btn_7 = Button(mw, text="2", padx=36, pady=10, font=("Arial",14),command=lambda:btn_clk("2"))
btn_8 = Button(mw, text="3", padx=36, pady=10, font=("Arial",14),command=lambda:btn_clk("3"))

btn_9 = Button(mw, text="/", padx=30, pady=10,font=("Arial",14),command=lambda:btn_clk("/"))
btn_10 = Button(mw, text="*",padx=30, pady=10,font=("Arial",14),command=lambda:btn_clk("*"))
btn_11= Button(mw, text="-", padx=30, pady=10,font=("Arial",14),command=lambda:btn_clk("-"))

btn_12= Button(mw, text=".", padx=36, pady=10,font=("Arial",14),command=lambda:btn_clk("."))
btn_13= Button(mw, text="0", padx=36, pady=10,font=("Arial",14),command=lambda:btn_clk("0"))
btn_14= Button(mw, text="%", padx=26, pady=10,font=("Arial",14),command=lambda:btn_clk("%"))

btn_15 = Button(mw, text="c", padx=92, pady=10,bg="red",fg="white",font=("Arial",14),command=clear)
btn_16= Button(mw, text="+", padx=30, pady=10,font=("Arial",14),command=lambda:btn_clk("+"))
btn_17= Button(mw, text="=", padx=36 ,pady=37, bg="blue",fg="white",font=("Arial",14),command=lambda:calculation())

#Displaying Buttons

btn_0.grid(row=1, column=0, padx=2, pady=2)
btn_1.grid(row=1, column=1, padx=2, pady=2)
btn_2.grid(row=1, column=2, padx=2, pady=2)
btn_9.grid(row=1, column=3, padx=2, pady=2)

btn_3.grid(row=2, column=0, padx=2, pady=2)
btn_4.grid(row=2, column=1, padx=2, pady=2)
btn_5.grid(row=2, column=2, padx=2, pady=2)
btn_10.grid(row=2, column=3, padx=2, pady=2)

btn_6.grid(row=3, column=0, padx=2, pady=2)
btn_7.grid(row=3, column=1, padx=2, pady=2)
btn_8.grid(row=3, column=2, padx=2, pady=2)
btn_11.grid(row=3, column=3, padx=2, pady=2)

btn_12.grid(row=4, column=0, padx=2, pady=2)
btn_13.grid(row=4, column=1, padx=2, pady=2)
btn_14.grid(row=4, column=3, padx=2, pady=2)
btn_17.grid(row=4, column=2, rowspan=2, padx=2, pady=2)

btn_15.grid(row=5, column=0 ,columnspan=2,padx=2, pady=2)
btn_16.grid(row=5, column=3, padx=2, pady=2)


display.grid(row=0, column=0, columnspan=4, padx=10, pady=10 )





mw.mainloop()
