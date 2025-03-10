import math

def MaquinaT(cinta, transiciones, estado_inicial, estado_final, signo_blanco=" "): #declaracion de la maquina de turing y sus parametros
    cinta = list(cinta) #se crea la lista cinta donde se guardara la cinta
    cabezal = 0 #estado inicial del cabezal
    estado = estado_inicial #estado inicial de la maquina
    pasos = 0 #contador de pasos
    
    while estado != estado_final: #mientras el estado no sea el final se ejecutara el ciclo
        simbolo = cinta[cabezal] if cabezal < len(cinta) else signo_blanco #se obtiene el simbolo actual de la cinta len es para devolver la longitud de un objeto ejeplo si len("hola")=4
        llave = (estado, simbolo) #se crea una tupla con el estado y el simbolo actual que seria llave
        
        if llave in transiciones: #se comprueba si la llave esta en las transiciones y in sirve para comprobar si un valor esta en la lista o tupla etc
            escribir, mover, siguiente_estado = transiciones[llave] #se obtienen los valores de la transicion
            
            if cabezal < len(cinta): #si el cabezal esta dentro de la cinta se escribe el simbolo
                cinta[cabezal] = escribir #escribe el simbolo en la cinta en el caso de que el cabezal este dentro de la cinta
            else:
                cinta.append(escribir) #append agreaga un elemento al final de la lista osea que escribe el simbolo en la cinta en el caso de que el cabezal este fuera de la cinta
            
            cabezal += 1 if mover == 'Derecha' else -1 if mover == 'Izquierda' else 0 # se mueve el cabezal a la derecha si el movimiento es D, a la izquierda si el movimiento es I y se queda en el mismo lugar si el movimiento es 0
            estado = siguiente_estado #se cambia el estado al siguiente estado
            pasos += 1 #incrementa el contador de pasos

    return ''.join(cinta).strip(), pasos, ''.join(cinta) #se retorna la cinta en forma de cadena-el join es para unir los elementos de una lista y strip para quitar los espacios

# Funciones para operaciones matemáticas
def suma(x, y): return x + y
def resta(x, y): return x - y
def multi(x, y): return x * y
def div(x, y): return x / y if y != 0 else 'No es posible dividir por cero'
def sqrt(x): return math.sqrt(x)
def power(x, y): return math.pow(x, y)
def log(x): return math.log(x) if x > 0 else 'no es posible calcular el logaritmo'
def sin(x): return math.sin(x)

transiciones = {
    ('q0', '1'): ('1', 'Derecha', 'q0'),  # Si el estado es 'q0' y el símbolo es '1', escribe '1', mueve a la derecha, y permanece en 'q0'
    ('q0', '0'): ('0', 'Derecha', 'q0'),  # Si el estado es 'q0' y el símbolo es '0', escribe '0', mueve a la derecha, y permanece en 'q0'
    ('q0', '+'): (' ', 'Derecha', 'q1'),  # Si el estado es 'q0' y el símbolo es '+', escribe un espacio, mueve a la derecha, y cambia a 'q1'
    ('q1', '1'): ('1', 'Derecha', 'q1'),  # Si el estado es 'q1' y el símbolo es '1', escribe '1', mueve a la derecha, y permanece en 'q1'
    ('q1', '0'): ('0', 'Derecha', 'q1'),  # Si el estado es 'q1' y el símbolo es '0', escribe '0', mueve a la derecha, y permanece en 'q1'
    ('q1', ' '): ('1', 'Izquierda', 'q2'),  # Si el estado es 'q1' y el símbolo es un espacio, escribe '1', mueve a la izquierda, y cambia a 'q2'
    ('q2', '1'): ('1', 'Izquierda', 'q2'),  # Si el estado es 'q2' y el símbolo es '1', escribe '1', mueve a la izquierda, y permanece en 'q2'
    ('q2', '0'): ('0', 'Izquierda', 'q2'),  # Si el estado es 'q2' y el símbolo es '0', escribe '0', mueve a la izquierda, y permanece en 'q2'
    ('q2', ' '): (' ', 'Derecha', 'EstadoFinal')  # Si el estado es 'q2' y el símbolo es un espacio, escribe un espacio, mueve a la derecha, y cambia a 'EstadoFinal'
}

ejecucion = input("Ingrese la cinta que desea operar en formato binario (ejemplo: 111+11): ") 
if '+' in ejecucion:#si en la ejecucion se encuentra un + se ejecutara la maquina de turing
    resultado, pasos, estado_final_cinta = MaquinaT(ejecucion, transiciones, 'q0', 'EstadoFinal')#se ejecuta la maquina de turing con los parametros de la ejecucion
    print("Numero de trancisiones realizadas:", pasos)
    print("Estado final de la cinta:", estado_final_cinta)
else: #si no se encuentra un + en la ejecucion se mostrara un mensaje de error
    print("Operacion no valida")

print("Operaciones Matematicas:")

print("Suma:", suma(int(input("Ingrese el primer valor: ")), int(input("Ingrese el segundo valor: "))))
print("Resta:", resta(int(input("Ingrese el primer valor: ")), int(input("Ingrese el segundo valor: "))))
print("Multiplicacion:", multi(int(input("Ingrese el primer valor: ")), int(input("Ingrese el segundo valor: "))))
print("Division:", div(int(input("Ingrese el primer valor: ")), int(input("Ingrese el segundo valor: "))))
print("Raiz Cuadrada:", sqrt(float(input("Ingrese el valor para calcular la raiz cuadrada: "))))
print("Potenciacion:", power(float(input("Ingrese la base: ")), float(input("Ingrese el exponente: "))))
print("Logaritmo:", log(float(input("Ingrese el valor para calcular el logaritmo: "))))