# Python for Beginners EP.4

# Sublime Text and Visual Studio Code Installation - 002235
	- [Sublime Text Setting Repo](https://github.com/UncleEngineer/Sublime)
	- Tools > Build System > New Build System
		- Replace with above configuration script
# list - 011900
```
list = ['a', 'b', 'c']
list.append('d')
list.remove('d')
list.pop() # remove last index
list.pop(2) # 2 is removing index
list.insert(2, 'd')
list.insert(1, list.pop(2))
llist.index('d')
```
# for - 015000
```
for l in list:
	print(l)

for i, l in enumerate(list):
	print(i, l)

for i, l in enumerate(list, start=1):
	print(i, l)
```
# dict - 022444
```
dict = {'key':'value'}
dict = {'Mon':'ຈັນ', 'Tue':'ອັງຄານ', 'Wed':'ພຸດ', 'Thur':'ພະຫັດ', 'Fri':'ສຸກ', 'Sat':'ເສົາ', 'Sun':'ອາທິດ'}
```