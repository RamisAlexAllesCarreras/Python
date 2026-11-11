
num1 = int(input("Escriu el primer nombre: "))
num2 = int(input("Escriu el segon nombre: "))

def gran(num1, num2):
    if num1 > num2:
        return f"{num1} és més gran que {num2}"
    elif num2 > num1:
        return f"{num2} és més gran que {num1}"
    else:
        return "Els dos nombres són iguals"

print(gran(num1, num2))


