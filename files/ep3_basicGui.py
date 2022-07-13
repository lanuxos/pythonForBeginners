# ep 3 basic GUI
from tkinter import *
from tkinter import ttk # theme of Tk
import csv
from datetime import datetime
# import tkinter
# GUI = tkinter.Tk()
GUI = Tk()
GUI.geometry('500x300+100+10')
GUI.title('Expense Log')
FontTimes = ('Times New Roman', 15)
'''
width-500,
height-300,
x-position[from left edge]-100,
y-position[from top edge]-10
'''
# B1 = Button(GUI, text='B1')
# B1.pack(ipadx=20, ipady=5) # ipadx - internal padding x/y

# F1 = Frame(GUI)
# F1.place(x=20, y=50)

# B2 = ttk.Button(F1, text='B2')
# B2.pack()

# F2 = ttk.LabelFrame(GUI, text='LabelFrame')
# F2.place(x=200, y=100)

# B3 = ttk.Button(F2, text='B3')
# B3.pack()

# WORK SHOP
F = Frame(GUI)
F.pack()

def Save(event=None):
    log = datetime.now().strftime('%Y%m%d%H%M%S')
    priceGet = price.get()
    itemGet = item.get()
    amountGet = amount.get()
    total = float(priceGet) * float(amountGet)
    print(f'{itemGet} is {priceGet}, amount {amountGet}, total {total} @ {log}')
    price.set('')
    item.set('')
    amount.set('')

    with open('expense.csv', 'a', encoding='utf-8', newline='') as f:
        # with open the file and close when done
        # a - append the existed data in file,
        # different from w - write which rewrite the file and replace the old data
        # newline = '' -- mean no empty line on csv file
        fw = csv.writer(f)
        data = [itemGet, priceGet, amountGet, total, log]
        fw.writerow(data)

    I.focus() # focus on Item entry box after save
    
IL = ttk.Label(F, text='Item(s)', font=FontTimes)
IL.pack()

item = StringVar()
I = ttk.Entry(F, textvariable=item, font=FontTimes)
I.pack()

PL = ttk.Label(F, text='Price(s)', font=FontTimes)
PL.pack()

price = StringVar()
P = ttk.Entry(F, textvariable=price, font=FontTimes)
P.pack()

AL = ttk.Label(F, text='Amount(s)', font=FontTimes)
AL.pack()

amount = StringVar()
A = ttk.Entry(F, textvariable=amount, font=FontTimes)
A.pack()

B = ttk.Button(F, text='SAVE', command=Save)
B.pack(pady=5)

GUI.bind('<Return>', Save) # noted - add event=None @ def

GUI.mainloop()
