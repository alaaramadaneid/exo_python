#demandez de l'utilisteur d'entre deux number
num1 = float(input("entrez num1 :"))
#coisir une operation
p =input("+ - / * : ")
num2 = float(input("entrez num 2 :"))

#les function des operations
def sum (x, y):
    return x+y
def sub(x,y):
    return x-y
def mult(x, y):
    return x*y
def dev(x, y):
    return x/y
# Effectuez l'opération et affichez le résultat

if p =="+":
    print(sum(num1, num2))
elif p =="-":
    print(sub(num1, num2))
elif p == "*":
    print(mult(num1, num2))
elif p =="/":
    print(dev(num1, num2))
else:
    print("invalid")
    exit()