# Python for Beginners EP.2

# Google Colab - 001415
	- [Google Colab](www.colab.research.google.com)
# print('command') - 010500
	- print()
		```
			print('string')
			print(variable)
			print(number)
		```
	- print().format - 010600
		```
			name = 'la'
			age = 30
			balance = 123456.789
			cash = 4321
			print('{} is {} years old have total balance: {}'.format(name, age, balance))
			print('{} is {} years old have total balance: {:,.2f} via {:,d} in cash'.format(name, age, balance, cash))
		```
	- f-string - 010920
		```
			name = 'la'
			age = 30
			balance = 123456.789
			cash = 4321
			print(f'{name} is {age} years old have total balance: {balance}')
			print(f'{name} is {age} years old have total balance: {balance:,.2f} via {cash:,d} in cash')
		```
	- %s [string]; %d[decimal integer]; %f[floating point] - 011110
		```
			name = 'la'
			age = 30
			balance = 123456.789
			cash = 4321
			print('%s is %d years old have total balance: %f{}'%(name, age, balance))
			print('%s is %d years old have total balance: %f{:,.2f} via {:,d} in cash'%(name, age, balance, cash))
		```
# Python turtle - 013200
	```
		import turtle

	```
# for loop - 015755
	```
		for i in range(5):
			print('step ', i)
	```
# list
	```
		list = ['a', 'b', 'c']
	```
# Homework
	```
		import turtle, random
		tao = turtle.Turtle()
		tao.shape('turtle')
		tao.pensize(5)
		color = ['red', 'orange', 'blue', 'grey', 'green',
				 'black', 'yellow', 'purple', 'brown', 'cyan']
		for i in color:
			tao.color(i)
			f = random.randint(50, 100)
			for j in range(4):
				tao.forward(f)
				tao.left(90)
			tao.penup()
			tao.goto(random.randint(-100, 100), random.randint(-100,100))
			tao.pendown()
	```