def menu():
    opcio=0
    while(opcio<1 or opcio>4):
        print("""
        Menú principal:
        1.Suma
        2.Resta
        3.Multiplicació
        4.Divisió
        """)
        opcio = int(input("Indiqui el número de la funció que vol executar:"))
    return opcio

# Programa principal

op =menu()
match(op):
    case 1:
        print("Operacions de suma: \n ")
        x = int(input("Escriu el primer nombre: "))
        y = int(input("Escriu el segon  nombre: "))
        print("La suma de {} i {} és {}".format(x,y,x+y))
    case 2:
        print("Operacions de resta: \n ")
        x = int(input("Escriu el primer nombre: "))
        y = int(input("Escriu el segon  nombre: "))
        print("La resta de {} i {} és {}".format(x,y,x-y))
    case 3:
        print("Operacions de multiplicació: \n ")
        x = int(input("Escriu el primer nombre: "))
        y = int(input("Escriu el segon  nombre: "))
        print("La multiplicació de {} i {} és {}".format(x,y,x*y))
    case 4:
        print("Operacions de divisió: \n ")
        x = int(input("Escriu el primer nombre: "))
        y = int(input("Escriu el segon  nombre: "))
        print("La divisió de {} i {} és {}".format(x,y,x/y))
    case _:
        print("En qualsevol atre cas: ")