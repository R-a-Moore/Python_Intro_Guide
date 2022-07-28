An intro to Python and how variables work

![python logo](https://www.python.org/static/img/python-logo.png)

To begin with you need to create a 'python file' by right clicking on the project you've created > new > then clicking on Python File, which you must name. 
Click on this new .py file, and try typing `print("Hello World")`. Then run this code, by pressing the green arrow at the top right of pycharm, 
right clicking on the code and selecting run "your python file name". This should show your message in the console. Try writing different messages. 

In python (and other programming languages), variables allow us to operate with identifiable data. There are different data types for variables, here are examples:
```
name = "Maiks 19 + 8" # string
age = 99 # int
salary = 15.5 # float
```
Try copying and running these into your pycharm.

With these variables made, you can dynamically print them without having to state their specific value.
```
print(name)
print(age)
print(salary)
```
You can also find out what the data type is for a variable
```
print(type(name))
print(type(age))
print(type(salary))
```
The `input()` method can be useful for getting user input. Made into a variable you can store their inputs.
```
name = input()
print(name)
```
Finally, with all thise you can do something like this...
```
print("Please fill in the following...")
print("first name: ")
first_name = input()
print("last name: ")
last_name = input()
print("age: ")
age = input()
print("address: ")
address = input()
print("salary: ")
salary = input()
```
Try running the code above and seeing what you get in your results...

