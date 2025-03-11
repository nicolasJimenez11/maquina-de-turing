import math
import time

# Convierte un número entero en su representación unaria
def enteroUnario(n):#definicion de la funcion enteroUnario
    return '1' * n if n > 0 else '0'#si n es mayor que 0 retorna 1*n si no retorna 0

# Convierte una representación unaria en número entero
def unarioEntero(unario):#definicion de la funcion unarioEntero
    return unario.count('1')#retorna el numero de veces que aparece el 1 en la cadena unario

# Declaración de la Máquina de Turing y sus parámetros
def MaquinaT(cinta, transiciones, estado_inicial, estado_final, signo_blanco=" "):#declaracion de la maquina de turing y sus parametros
    cinta = list(cinta)#se crea la lista cinta donde se guardara la cinta
    cabezal = 0#estado inicial del cabezal
    estado = estado_inicial#estado inicial de la maquina
    pasos = 0#contador de pasos
    
    while estado != estado_final:#mientras el estado no sea el final se ejecutara el ciclo
        simbolo = cinta[cabezal] if cabezal < len(cinta) else signo_blanco#se obtiene el simbolo actual de la cinta len es para devolver la longitud de un objeto ejeplo si len("hola")=4
        llave = (estado, simbolo)#se crea una tupla con el estado y el simbolo actual que seria llave
        
        if llave in transiciones:#se comprueba si la llave esta en las transiciones y in sirve para comprobar si un valor esta en la lista o tupla etc
            escribir, mover, siguiente_estado = transiciones[llave]#se obtienen
            
            if cabezal < len(cinta):#si el cabezal esta dentro de la cinta se escribe el simbolo len sirve para devolver la longitud de un objeto ejeplo si len("hola")=4
                cinta[cabezal] = escribir  #escribe el simbolo en la cinta en el caso de que el cabezal este dentro de la cinta
            else:
                cinta.append(escribir)#append agreaga un elemento al final de la lista osea que escribe el simbolo en la cinta en el caso de que el cabezal este fuera de la cinta
            
            cabezal += 1 if mover == 'Derecha' else -1 if mover == 'Izquierda' else 0 # se mueve el cabezal a la derecha si el movimiento es D, a la izquierda si el movimiento es I y se queda en el mismo lugar si el movimiento es 0
            estado = siguiente_estado#se cambia el estado al siguiente estado
            pasos += 1#se aumenta el contador de pasos
        else:
            print(f"Error: No hay transición definida para ({estado}, {simbolo})")#si no hay transicion definida se imprime un mensaje de error y se usa las llaves para imprimir variables
            return "", pasos

    return ''.join(cinta).strip(), pasos#se retorna la cinta en forma de cadena-el join es para unir los elementos de una join sirve para unir los elementos de una lista y strip para quitar los espaciossi

# Definición de transiciones para operaciones básicas
def Dtransiciones():
    return {
        # SUMA: 111+11 → 11111
        ('q0', '1'): ('1', 'Derecha', 'q0'),# si el estado es q0 y el simbolo es 1, escribe 1, mueve a la derecha y permanece en q0
        ('q0', '+'): (' ', 'Derecha', 'q1'),# si el estado es q0 y el simbolo es +, escribe un espacio, mueve a la derecha y cambia a q1
        ('q1', '1'): ('1', 'Derecha', 'q1'),# si el estado es q1 y el simbolo es 1, escribe 1, mueve a la derecha y permanece en q1
        ('q1', ' '): ('1', 'Izquierda', 'q2'),# si el estado es q1 y el simbolo es un espacio, escribe 1, mueve a la izquierda y cambia a q2
        ('q2', '1'): ('1', 'Izquierda', 'q2'),# si el estado es q2 y el simbolo es 1, escribe 1, mueve a la izquierda y permanece en q2
        ('q2', ' '): (' ', 'Derecha', 'EstadoFinal'),#  si el estado es q2 y el simbolo es un espacio, escribe un espacio, mueve a la derecha y cambia a EstadoFinal

        # RESTA: 111-11 → 1
        ('q0', '-'): (' ', 'Derecha', 'q3'),# si el estado es q0 y el simbolo es -, escribe un espacio, mueve a la derecha y cambia a q3
        ('q3', '1'): (' ', 'Derecha', 'q4'),# si el estado es q3 y el simbolo es 1, escribe un espacio, mueve a la derecha y cambia a q4
        ('q4', '1'): (' ', 'Derecha', 'q5'),# si el estado es q4 y el simbolo es 1, escribe un espacio, mueve a la derecha y cambia a q5
        ('q5', ' '): (' ', 'Izquierda', 'q6'),# si el estado es q5 y el simbolo es un espacio, escribe un espacio, mueve a la izquierda y cambia a q6
        ('q6', '1'): ('1', 'Izquierda', 'q6'),# si el estado es q6 y el simbolo es 1, escribe 1, mueve a la izquierda y permanece en q6
        ('q6', ' '): (' ', 'Derecha', 'EstadoFinal'),# si el estado es q6 y el simbolo es un espacio, escribe un espacio, mueve a la derecha y cambia a EstadoFinal

        # MULTIPLICACIÓN: 11*11 → 1111
        ('q0', '*'): (' ', 'Derecha', 'q7'),# si el estado es q0 y el simbolo es *, escribe un espacio, mueve a la derecha y cambia a q7
        ('q7', '1'): (' ', 'Derecha', 'q8'),# si el estado es q7 y el simbolo es 1, escribe un espacio, mueve a la derecha y cambia a q8
        ('q8', '1'): ('1', 'Derecha', 'q8'),# si el estado es q8 y el simbolo es 1, escribe 1, mueve a la derecha y permanece en q8
        ('q8', ' '): (' ', 'Izquierda', 'q9'),# si el estado es q8 y el simbolo es un espacio, escribe un espacio, mueve a la izquierda y cambia a q9
        ('q9', '1'): ('1', 'Izquierda', 'q9'),# si el estado es q9 y el simbolo es 1, escribe 1, mueve a la izquierda y permanece en q9
        ('q9', ' '): (' ', 'Derecha', 'q10'),# si el estado es q9 y el simbolo es un espacio, escribe un espacio, mueve a la derecha y cambia a q10
        ('q10', '1'): ('1', 'Derecha', 'q10'),# si el estado es q10 y el simbolo es 1, escribe 1, mueve a la derecha y permanece en q10
        ('q10', ' '): (' ', 'Izquierda', 'q11'),# si el estado es q10 y el simbolo es un espacio, escribe un espacio, mueve a la izquierda y cambia a q11
        ('q11', '1'): ('1', 'Izquierda', 'q11'),# si el estado es q11 y el simbolo es 1, escribe 1, mueve a la izquierda y permanece en q11
        ('q11', ' '): (' ', 'Derecha', 'q12'),# si el estado es q11 y el simbolo es un espacio, escribe un espacio, mueve a la derecha y cambia a q12
        ('q12', '1'): ('1', 'Derecha', 'q12'),# si el estado es q12 y el simbolo es 1, escribe 1, mueve a la derecha y permanece en q12
        ('q12', ' '): (' ', 'Izquierda', 'q13'),# si el estado es q12 y el simbolo es un espacio, escribe un espacio, mueve a la izquierda y cambia a q13
        ('q13', '1'): ('1', 'Izquierda', 'q13'),# si el estado es q13 y el simbolo es 1, escribe 1, mueve a la izquierda y permanece en q13
        ('q13', ' '): (' ', 'Derecha', 'EstadoFinal'),# si el estado es q13 y el simbolo es un espacio, escribe un espacio, mueve a la derecha y cambia a EstadoFinal

        # DIVISIÓN: 111/11 → 1
        ('q0', '/'): (' ', 'Derecha', 'q14'),# si el estado es q0 y el simbolo es /, escribe un espacio, mueve a la derecha y cambia a q14
        ('q14', '1'): (' ', 'Derecha', 'q15'),# si el estado es q14 y el simbolo es 1, escribe un espacio, mueve a la derecha y cambia a q15
        ('q15', '1'): (' ', 'Derecha', 'q16'),# si el estado es q15 y el simbolo es 1, escribe un espacio, mueve a la derecha y cambia a q16
        ('q16', ' '): ('1', 'Izquierda', 'q17'),# si el estado es q16 y el simbolo es un espacio, escribe 1, mueve a la izquierda y cambia a q17
        ('q17', '1'): ('1', 'Izquierda', 'q17'),# si el estado es q17 y el simbolo es 1, escribe 1, mueve a la izquierda y permanece en q17
        ('q17', ' '): (' ', 'Derecha', 'EstadoFinal')# si el estado es q17 y el simbolo es un espacio, escribe un espacio, mueve a la derecha y cambia a EstadoFinal
    }

transiciones = Dtransiciones()

operacion = input("Ingrese la operación que desea realizar (+, -, *, /, sqrt, ln, ^, sin): ").strip()#strip elimina los espacios en blanco al principio y al final de la cadena
if operacion not in ['+', '-', '*', '/', 'sqrt', 'ln', '^', 'sin']:#not in sirve para comprobar si un valor no esta en la lista
    print("Operación no válida")
else:
    start_time = time.time()  # Inicia el temporizador

    if operacion == 'sqrt':#si la operacion es sqrt
        a = int(input("Ingrese el número: "))#
        resultado = 0
        contador = 1
        while a > 0:
            a -= contador
            if a >= 0:
                resultado += 1
            contador += 2
        resultado_unario = enteroUnario(resultado)
        print("Estado final de la cinta:", resultado_unario)
        print("Resultado en número entero:", resultado)
        print("Resultado calculado normalmente:", int(a ** 0.5))  # Resultado calculado normalmente
    elif operacion == 'ln':#si la operacion es ln
        x = float(input("Ingrese el número: "))
        if x <= 0:
            print("El logaritmo natural solo está definido para valores positivos.")
        else:
            y = (x - 1) / (x + 1)
            resultado = 0
            iteraciones = 20
            for k in range(iteraciones):#range sirve para generar una lista de numeros
                resultado += (2 * (y ** (2 * k + 1))) / (2 * k + 1)
            resultado_entero = int(2 * resultado)
            resultado_unario = enteroUnario(resultado_entero)
            print("Resultado en número real:", 2 * resultado)
            print("Resultado en unario:", resultado_unario)
            print("Número de transiciones realizadas:", iteraciones)
            print("Resultado calculado normalmente:", math.log(x))  # Resultado calculado normalmente
    elif operacion == '^':#si la operacion es ^
        base = int(input("Ingrese la base: "))
        exponente = int(input("Ingrese el exponente: "))
        resultado = base ** exponente
        resultado_unario = enteroUnario(resultado)
        print("Estado final de la cinta:", resultado_unario)
        print("Resultado en número entero:", resultado)
        print("Número de transiciones realizadas:", exponente)
        print("Resultado calculado normalmente:", base ** exponente)  # Resultado calculado normalmente
    elif operacion == 'sin':
        x = float(input("Ingrese el ángulo en radianes: "))
        resultado = 0
        iteraciones = 10
        for k in range(iteraciones):
            signo = (-1) ** k#** es el operador de potenciacion
            numerador = x ** (2 * k + 1)# ** es el operador de potenciacion
            denominador = math.factorial(2 * k + 1)#factorial calcula el factorial de un numero
            resultado += (signo * numerador) / denominador#se calcula el resultado
        resultado_entero = int(abs(resultado) * 100)  # abs devuelve el valor absoluto de un número
        resultado_unario = enteroUnario(resultado_entero)#se convierte el resultado en unario
        print("Resultado en número real:", resultado)
        print("Resultado en unario:", resultado_unario)
        print("Número de transiciones realizadas:", iteraciones)
        print("Resultado calculado normalmente:", math.sin(x))  # Resultado calculado normalmente
    else:#si no es ninguna de las anteriores
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        cinta = enteroUnario(a) + operacion + enteroUnario(b)
        resultado, pasos = MaquinaT(cinta, transiciones, 'q0', 'EstadoFinal')
        print("Número de transiciones realizadas:", pasos)
        print("Estado final de la cinta:", resultado)
        print("Resultado en número entero:", unarioEntero(resultado))#se imprime el resultado en numero entero
        if operacion == '+':
            print("Resultado calculado normalmente:", a + b)  # Resultado calculado normalmente
        elif operacion == '-':
            print("Resultado calculado normalmente:", a - b)  # Resultado calculado normalmente
        elif operacion == '*':
            print("Resultado calculado normalmente:", a * b)  # Resultado calculado normalmente
        elif operacion == '/':
            print("Resultado calculado normalmente:", a // b)  # Resultado calculado normalmente (división entera)

    end_time = time.time()  # Detiene el temporizador
    print("Tiempo de ejecución: {:.6f} segundos".format(end_time - start_time))  # Imprime el tiempo de ejecución y manda 6 decimales que es {:.6f} y se usa format para dar formato a la salida
