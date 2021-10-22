#Author(s): 766431

#File: Basic_Calculator.py
"""
Simple calculator

"""

from tkinter import *


root = Tk()
root.title('Basic Calculator')


screen = Entry(root, width=55, borderwidth=5)
screen.grid(row=0, column=0, columnspan=4)

def Button_press(number):
    '''Call the different numbers pressed'''
    current = screen.get()
    screen.delete(0,END)
    screen.insert(0, str(current) + str(number))

def Button_clc():
    '''Function used too clear the screen'''
    screen.delete(0, END)


def Button_add():
    '''This function is called when the add button is pressed, and it performs the addition task'''
    first_number = screen.get()
    global f_num   # global variable is used here which is also present in every function, to utilize for it's operation
    global math
    math = 'addition'
    f_num = int(first_number)
    screen.delete(0, END)
    
def Button_subtract():
    '''This function is called when the subtract button is pressed, and it performs the subtraction task'''
    first_number = screen.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    screen.delete(0, END)

def Button_multiply():
    '''This function is called when the multiply button is pressed, and it performs the multiplication task'''
    first_number = screen.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    screen.delete(0, END)

def Button_divide():
    '''This function is called when the divide button is pressed, and it performs the division task'''
    first_number = screen.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    screen.delete(0, END)

def Button_equal():
    '''This function is called when the equal button is pressed, and it toggles through each function before finding the particular task
       to print the solution on the screen'''
    second_number = screen.get()
    screen.delete(0, END)

    if math == 'addition':
        screen.insert(0, f_num + int(second_number))

    if math == 'subtraction':
        screen.insert(0, f_num - int(second_number))

    if math == 'multiplication':
        screen.insert(0, f_num * int(second_number))

    if math == 'division':
        screen.insert(0, f_num / int(second_number))






'''first row of buttons'''
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda:Button_press(7)).grid(row=1,column=0)

button_8 = Button(root, text='8', padx=40, pady=20, command=lambda:Button_press(8)).grid(row=1,column=1)

button_7 = Button(root, text='9', padx=40, pady=20, command=lambda:Button_press(9)).grid(row=1,column=2)

button_divide = Button(root, text='/', padx=40, pady=20, command=Button_divide).grid(row=1,column=3)

'''second row of buttons'''
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda:Button_press(4)).grid(row=2,column=0)

button_5 = Button(root, text='5', padx=40, pady=20, command=lambda:Button_press(5)).grid(row=2,column=1)

button_6 = Button(root, text='6', padx=40, pady=20, command=lambda:Button_press(6)).grid(row=2,column=2)

button_multiply = Button(root, text='X', padx=40, pady=20, command=Button_multiply).grid(row=2,column=3)


'''third row of buttons'''
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda:Button_press(1)).grid(row=3,column=0)

button_2 = Button(root, text='2', padx=40, pady=20, command=lambda:Button_press(2)).grid(row=3,column=1)

button_3 = Button(root, text='3', padx=40, pady=20, command=lambda:Button_press(3)).grid(row=3,column=2)

button_subtract = Button(root, text='-', padx=40, pady=20, command=Button_subtract).grid(row=3,column=3)

'''fourth row of buttons'''
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda:Button_press(0)).grid(row=4,column=0)

button_clear = Button(root, text='C', padx=40, pady=20, command=Button_clc).grid(row=4,column=1)

button_equal = Button(root, text='=', padx=40, pady=20, command=Button_equal).grid(row=4,column=2)

button_add = Button(root, text='+', padx=40, pady=20, command=Button_add).grid(row=4,column=3)










root.mainloop()

input('.....')

