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
    # regex - regular expresssion
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