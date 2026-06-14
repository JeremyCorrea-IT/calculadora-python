"""
Calculadora con operaciones aritméticas básicas y manejo de errores.
Features: Salida a colores ANSI, proteccion contra division/residuo entre cero,
          blindaje contra potencias execivas, e historial de opreaciones.
version: 1.0
Autor: Jeremy.C
"""
CYAN = "\033[96m"
VERDE = "\033[92m"
ROJO = "\033[91m"
NEGRILLA = "\033[1m"
RESET = "\033[0m"

historial = []

while True:
    print(f"\n{NEGRILLA}{CYAN}--- NUEVA OPERACIÓN ---{RESET}\n")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    print(f"{CYAN}{'=' * 30}{RESET}")

    # Suma
    suma = num1 + num2
    print(f"{VERDE}Suma: {num1} + {num2} = {suma}{RESET}")
    historial.append(f"Suma: {num1} + {num2} = {suma}")

    # Resta
    resta = num1 - num2
    print(f"{VERDE}Resta: {num1} - {num2} = {resta}{RESET}")
    historial.append(f"Resta: {num1} - {num2} = {resta}")

    # Multiplicación
    mult = num1 * num2
    print(f"{VERDE}Multiplicación: {num1} * {num2} = {mult}{RESET}")
    historial.append(f"Multiplicación: {num1} * {num2} = {mult}")

    # División con protección contra cero
    if num2 != 0:
        div = num1 / num2
        print(f"{VERDE}División: {num1} / {num2} = {div}{RESET}")
        historial.append(f"División: {num1} / {num2} = {div}")
    else:
        print(f"{ROJO}División: No se puede dividir por cero{RESET}")
        historial.append("División: Error - División entre cero")

    # Potencia
    try:
        potencia = num1 ** num2
        print(f"{VERDE}Potencia: {num1} ** {num2} = {potencia}{RESET}")
        historial.append(f"Potencia: {num1} ** {num2} = {potencia}")
    except OverflowError:
        print(f"{ROJO}Potencia: Error - Número demasiado grande para calcular{RESET}")
        historial.append("Potencia: Error - Número demasiado grande")

    # Residuo con protección contra cero
    if num2 != 0:
        residuo = num1 % num2
        print(f"{VERDE}Residuo: {num1} % {num2} = {residuo}{RESET}")
        historial.append(f"Residuo: {num1} % {num2} = {residuo}")
    else:
        print(f"{ROJO}Residuo: No se puede calcular el residuo con cero como divisor{RESET}")
        historial.append("Residuo: Error - División entre cero")

    # Preguntar si sigue
    seguir = input(f"\n{CYAN}¿Quieres realizar otra operación? (s/n): {RESET}").lower()

    if seguir == "n":
        total = len(historial)
        mostrar = min(5, total)
        print(f"\n{NEGRILLA}{CYAN}┌─ HISTORIAL ─┐{RESET}")
        print(f"{NEGRILLA}{VERDE}Mostrando últimos {mostrar} de {total} ejercicios{RESET}")
        print(f"{CYAN}└─────────────┘{RESET}\n")
        for operacion in historial[-5:]:
            print(operacion)
        print(f"\n{CYAN}Gracias por usar la calculadora, hasta luego!{RESET}")
        break
