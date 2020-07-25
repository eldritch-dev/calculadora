import re
print("Calculadora!")
print("Escribe 'salir' para salir\n")

previo = 0
validador = True

def realizar_calculo():
    global validador
    global previo
    ecuacion = ""
    if previo == 0:
        ecuacion = input("Escribe tu ecuación: ")
    else:
        ecuacion = input(str(previo))


    if ecuacion == 'salir':
        print("Hasta la vista, humano.")
        validador = False
    else:
        # Usamos RegEx para prevenir vulnerabilidades de la función eval().
        ecuacion = re.sub('[a-zA-Z,.:()" "]','',ecuacion)

        if previo == 0:
            previo = eval(ecuacion)
        else:
            previo = eval(str(previo) + ecuacion)

while validador:
    realizar_calculo()