<h1 align="center"> BASIC CALCULATOR</h1>

### Introduction

This is first program i have ever made. I believe there is a lot of things that could be better, but i wanted to keep it like this as a memory. 

##

### How does it work?

It all starts here:

```python
# Program start
print("Welcome")

# For endless using
while True:
	print("enter your problem:", end=" ")
	priklad = input()
	
	if priklad == "end": # Way to close program
		break
```
First thing you'll see is Welcome message and then it asks for your math problem. Your problem will store into "priklad" variable.

If you type "end", program will close itself

##

When program is executed, first thing user sees is welcome message and then it can input its math problem. 
Because its basic calculator, there is only 5 operations

| Operator | Name | Example | Result |
|--|--|--|--|
|+  | addition | x = y + 2 | y=5; x=7 |
 |-| Subtraction |x = y - 2| y=5; x=3 |
| * | Multiplication | x = y * 2 | y=5; x=10 |
| ** | Exponentiation  | x = y ** 2 | y=5;x=25 |
| / | Division | x = y / 2 | y=5; x=2,5 |

##

There is imported parse library for searching right operation by using parse.search and regex function.

Regex will find which operation is used. After finding out which operation is used, it will find right case and execute function with variable "priklad" in it. 

There is default case for people who typed wrong operation.

```python
import parse

...
... 

match parse.search('{:D}', priklad)[0]:
	case "+":
		print(soucet(priklad))
	case "-":
		print(rozdil(priklad))
	case "/":
		print(podil(priklad))
	case "*":
		print(soucin(priklad))
	case "**":
		print(umocneni(priklad))
	case _:
		print("wrong input")
```

##


For calculating right answer, there's used function for every operation available. Pushed variable is split into two variables named "arg1" and "arg2". For this we use split function which split the variable by operation.

After that we convert new two variables into integers and we do the right operation.

```python
def soucet(vstup):
	arg1, arg2 = vstup.split("+")
	return(int(arg1) + int(arg2))

def podil(vstup):
	arg1, arg2 = vstup.split("/")
	return(int(arg1) / int(arg2))

def soucin(vstup):
	arg1, arg2 = vstup.split("*")
	return(int(arg1) * int(arg2))

def rozdil(vstup):
	arg1, arg2 = vstup.split("-")
	return(int(arg1) - int(arg2))

def umocneni(vstup):
	arg1, arg2 = vstup.split("**")
	return(int(arg1) ** int(arg2))

```

##
With all these steps, program will give you the right answer to your math problem and because we used `While True:` program will start again till you type "end"

```python
import parse

def soucet(vstup):
	arg1, arg2 = vstup.split("+")
	return(int(arg1) + int(arg2))

def podil(vstup):
	arg1, arg2 = vstup.split("/")
	return(int(arg1) / int(arg2))

def soucin(vstup):
	arg1, arg2 = vstup.split("*")
	return(int(arg1) * int(arg2))

def rozdil(vstup):
	arg1, arg2 = vstup.split("-")
	return(int(arg1) - int(arg2))

def umocneni(vstup):
	arg1, arg2 = vstup.split("**")
	return(int(arg1) ** int(arg2))
	
# Program start
print("Welcome")

# For endless using
while True:
	print("enter your problem:", end=" ")
	priklad = input()
	
	if priklad == "end": # Way to close program
		break

	match parse.search('{:D}', priklad)[0]:
		case "+":
			print(soucet(priklad))
		case "-":
			print(rozdil(priklad))
		case "/":
			print(podil(priklad))
		case "*":
			print(soucin(priklad))
		case "**":
			print(umocneni(priklad))
		case _:
			print("wrong input")
```
##

<p align="center">Only python was used</p>
<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="30" alt="python logo"  />
</div>

###
