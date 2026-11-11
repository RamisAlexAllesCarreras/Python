
# Calculadora amb operacions aritmètiques i canvis de base

print("=== CALCULADORA ===")
print("1. Operacions aritmètiques")
print("2. Canvi de base")

opcio = input("Tria una opció: ")

if opcio == "1":

    num1 = float(input("Introdueix el primer nombre: "))
    num2 = float(input("Introdueix el segon nombre: "))

    print("\nOperacions disponibles:")
    print("+  Suma")
    print("-  Resta")
    print("*  Multiplicació")
    print("/  Divisió")
    print("// Divisió entera")
    print("%  Mòdul")
    print("** Potència")

    operacio = input("Tria una operació: ")

    if operacio == "+":
        print("Resultat:", num1 + num2)

    elif operacio == "-":
        print("Resultat:", num1 - num2)

    elif operacio == "*":
        print("Resultat:", num1 * num2)

    elif operacio == "/":
        if num2 != 0:
            print("Resultat:", num1 / num2)
        else:
            print("Error: no es pot dividir per zero.")

    elif operacio == "//":
        if num2 != 0:
            print("Resultat:", num1 // num2)
        else:
            print("Error: no es pot dividir per zero.")

    elif operacio == "%":
        if num2 != 0:
            print("Resultat:", num1 % num2)
        else:
            print("Error: no es pot dividir per zero.")

    elif operacio == "**":
        print("Resultat:", num1 ** num2)

    else:
        print("Operació no vàlida.")

elif opcio == "2":

    print("\n=== CANVI DE BASE ===")
    print("1. Binari (base 2)")
    print("2. Octal (base 8)")
    print("3. Decimal (base 10)")
    print("4. Hexadecimal (base 16)")

    base_origen = int(input("Tria la base d'origen (1-4): "))
    base_desti = int(input("Tria la base de destinació (1-4): "))

    bases = {
        1: 2,
        2: 8,
        3: 10,
        4: 16
    }

    if base_origen in bases and base_desti in bases:

        nombre = input("Introdueix el nombre que vols convertir: ")

        try:
            # Convertim el nombre a decimal
            decimal = int(nombre, bases[base_origen])

            # Convertim de decimal a la base de destinació
            base = bases[base_desti]

            if base == 2:
                resultat = bin(decimal)
            elif base == 8:
                resultat = oct(decimal)
            elif base == 10:
                resultat = str(decimal)
            else:
                resultat = hex(decimal)

            # Eliminam els prefixos 0b, 0o i 0x
            if base != 10:
                resultat = resultat[2:]

            print("Resultat de la conversió:", resultat.upper())

        except ValueError:
            print("Error: el nombre no és vàlid per a la base seleccionada.")

    else:
        print("Error: has de seleccionar una opció entre 1 i 4.")

else:
    print("Opció no vàlida.")

