# Python for Beginners EP.5

# GUI Tab - 002735
```
from tkinter import *
from tkinter import ttk, messagebox # theme of Tk
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

T = ttk.Notebook(GUI)
T1 = Frame(T)
T2 = Frame(T)
T.pack(fill=BOTH, expand=1)

Ticon = PhotoImage(file='icon.png').subsample(10) 
# .subsample(10) to reduce image size 10 times

T.add(T1, text=f'{"Expense":^{20}}', image=Ticon, compound='left') 
# f-string to expand string to 20 chars
# compound - icon position [right, left, top, bottom]
T.add(T2, text=f'{"List":^{20}}', image=Ticon, compound='right')

F = Frame(T1)
F.pack()

def Save(event=None):
	log = datetime.now().strftime('%Y%m%d%H%M%S')
	priceGet = price.get()
	itemGet = item.get()
	amountGet = amount.get()

	if itemGet == '':
		messagebox.showwarning('Error', 'Please fill item info')
		I.focus()
		return
	elif priceGet == '':
		messagebox.showwarning('Error', 'Please fill the priceGet')
		P.focus()
		return
	elif amountGet == '':
		amountGet = 1

	try:
		total = float(priceGet) * float(amountGet)
		print(f'{itemGet} is {priceGet}, amount {amountGet}, total {total} @ {log}')
		text = f'{itemGet} is {priceGet}, amount {amountGet}, total {total} @ {log}'
		result.set(text)
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
	except:
		# messagebox.showerror('Error', 'There is an error occured while saving expense item.')
		# messagebox.showwarning('Error', 'There is an error occured while saving expense item.')
		messagebox.showinfo('Error', 'There is an error occured while saving expense item.')
		price.set('')
		item.set('')
		amount.set('')
IL = ttk.Label(F, text='Item(s)', font=FontTimes)
IL.pack()

item = StringVar()
I = ttk.Entry(F, textvariable=item, font=FontTimes)
I.pack()

I.focus()

PL = ttk.Label(F, text='Price(s)', font=FontTimes)
PL.pack()

price = StringVar() # or using FloatVar() to get as float value
P = ttk.Entry(F, textvariable=price, font=FontTimes)
P.pack()

AL = ttk.Label(F, text='Amount(s)', font=FontTimes)
AL.pack()

amount = StringVar()
A = ttk.Entry(F, textvariable=amount, font=FontTimes)
A.pack()

B = ttk.Button(F, text='SAVE', command=Save)
B.pack(pady=5)

result = StringVar()
result.set('-=Result display here=-')
RL = ttk.Label(F, textvariable=result, font=FontTimes, foreground='green')
RL.pack(pady=5)

GUI.bind('<Return>', Save) # noted - add event=None @ def

GUI.mainloop()

```
# try/except - 011919
```
try:
	print(nonExistedVariable)
except:
	print('There is an error occured')
```
```
try:
	print(nonExistedVariable)
except Exception as e:
	print('There is an error occured')
	print(e)
```
# messagebox - 013225
# Indentation error [Tab/Space] - 014900
# if/else - 020400
# return - 020500