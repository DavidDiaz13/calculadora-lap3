def addmultiplenumbers(numeros):
    return sum(numeros)


def multiplymultiplenumbers(numeros):
    resultado = 1
    for numero in numeros:
        resultado = resultado * numero
    return resultado


def isitaninteger(num):
    if num == int(num):
        return True
    else:
        return False


def isiteven(num):
    if num % 2 == 0 and isitaninteger(num):
        return True
    else:
        return False


def main():
    print("Bienvenido a la calculadora")
    print("1. Sumar")
    print("2. Multiplicar")
    print("3. Saber si un numero es par")
    print("4. Saber si un numero es entero")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        numero1 = float(input("Escribe el primer numero: "))
        numero2 = float(input("Escribe el segundo numero: "))
        numero3 = float(input("Escribe el tercer numero: "))
        numero4 = float(input("Escribe el cuarto numero: "))
        numero5 = float(input("Escribe el quinto numero: "))

        numeros = [numero1, numero2, numero3, numero4, numero5]

        print(addmultiplenumbers(numeros))

    elif opcion == "2":
        numero1 = float(input("Escribe el primer numero: "))
        numero2 = float(input("Escribe el segundo numero: "))
        numero3 = float(input("Escribe el tercer numero: "))
        numero4 = float(input("Escribe el cuarto numero: "))
        numero5 = float(input("Escribe el quinto numero: "))

        numeros = [numero1, numero2, numero3, numero4, numero5]

        print(multiplymultiplenumbers(numeros))

    elif opcion == "3":
        numero = float(input("Escribe un numero: "))
        print(isiteven(numero))

    elif opcion == "4":
        numero = float(input("Escribe un numero: "))
        print(isitaninteger(numero))

    else:
        print("Opcion no valida")


if __name__ == "__main__":
    main()