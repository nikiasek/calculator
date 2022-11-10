import parse

#DEFINUJÍ SE FUNKCE
#def - definice funkcí
#return - návratová hodnota
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


#START PROGRAMU
print("Yo, vítej v mé kalkulačce")

#while true - vždy pravda (běží do nekonečna)
while True:
    print("Zadej příklad:", end=" ")
    priklad = input()

    if priklad == "ukoncit": #tady to vypneš trotle
        break
    # regex - regulérní výraz
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
            print("chybný vstup")