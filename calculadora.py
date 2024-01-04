def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"


if __name__ == "__main__":

    # Mostrar opciones de operación
    print("Seleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    # Obtener la elección del usuario
    opcion = input("Ingrese el número de la operación deseada (1-4): ")

    # Solicitar entrada del usuario
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Realizar operación seleccionada
    if opcion == "1":
        resultado = sumar(num1, num2)
    elif opcion == "2":
        resultado = restar(num1, num2)
    elif opcion == "3":
        resultado = multiplicar(num1, num2)
    elif opcion == "4":
        # Verificar división por cero
        if num2 != 0:
            resultado = dividir(num1, num2)
        else:
            resultado = "Error: División por cero"
    else:
        resultado = "Opción no válida"

    # Mostrar resultado
    print(f"Resultado: {resultado}")
