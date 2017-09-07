#!python2
from random import randint # Libreria para generar numeros enteros aleatorios en python
import time # Libreria para usar la funcion sleep()

# Matriz que indica cuales son los carriles que pueden estar en verde al mismo tiempo.
# Los carriles A, C, E y G son vueltas a la izquierda; los carriles restantes (B, D, F y H),
# son carriles que van derecho.
carriles_en_verde = [
		# A, B, C, D, E, F, G, H
		[ 1, 1, 0, 0, 0, 0, 0, 0 ], # A y B estan prendidos
		[ 0, 1, 0, 0, 0, 1, 0, 0 ], # B y F estan prendidos
		[ 0, 0, 0, 0, 1, 1, 0, 0 ], # E y F estan prendidos
		[ 0, 0, 1, 1, 0, 0, 0, 0 ], # C y D estan prendidos
		[ 0, 0, 0, 1, 0, 0, 0, 1 ], # D y H estan prendidos
		[ 0, 0, 0, 0, 0, 0, 1, 1 ]  # G y H estan prendidos
	]

# Arreglo que guarda la cantidad de carros en cada carril, todos los carriles empiezan con 0 carros
				   # A, B, C, D, E, F, G, H
carros_en_carril = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
nombre_de_carril = [ "A", "B", "C", "D", "E", "F", "G", "H"]

# Arreglo que guarda el tiempo que estara en verde cada carril, todos los carriles empiezan con 5 seg
					# A, B, C, D, E, F, G, H
tiempo_por_carril = [ 5, 5, 5, 5, 5, 5, 5, 5 ]


def agregar_trafico_carriles():
	"""
	Funcion que genera el trafico en cada uno de los carriles.
	El trafico que se genera es un numero aleatorio.
	"""

	# Recorremos el arreglo para asignar un numero de carros a cada carril
	for carril in range(len(carros_en_carril)):
		# El trafico en cada carril es la cantidad de carros en ese carril mas un numero aleatorio entre 1 y 15
		carros_en_carril[carril] = carros_en_carril[carril] + randint(1, 15)
		print "\tCarros en el carril {} = {}".format(nombre_de_carril[carril], carros_en_carril[carril])


def simula_cruce_con_semaforo():
	"""
	Funcion que simula el funcionamiento de un cruce de calles con semaforos
	"""

	# Se recorre la matriz de carriles en verde
	for index in range(len(carriles_en_verde)):
		estado_de_los_semaforos = carriles_en_verde[index]
		imprimir_estatus_de_semaforos(estado_de_los_semaforos)
		
		# Se recorre el estado de los semaforos
		tiempo_en_verde = obtener_tiempo_en_verde(estado_de_los_semaforos)
		for semaforo in range(len(estado_de_los_semaforos)):
			# Revisar si el semaforo esta encendido y quitarle trafico
			if estado_de_los_semaforos[semaforo] == 1:
				# Por cada segundo se resta un carro del carril con semaforo en verde.
				# Si el numero de carros en un carril es menor a 0, se deja en 0 la cantidad de carros en el carril
				# No es posible tener una cantidad negativa de carros en espera
				carros_en_carril[semaforo] = carros_en_carril[semaforo] - tiempo_en_verde if (carros_en_carril[semaforo] - tiempo_en_verde) >= 0 else 0
			else:
				# Si el semaforo esta en rojo, agregarle trafico
				carros_en_carril[semaforo] = carros_en_carril[semaforo] + randint(1, 5)

		# Esperar el numero de segundos que los carriles van a estar en verde
		time.sleep(tiempo_en_verde)
		# Imprimir numero de carros por carril
		imprimir_carros_por_carril()


def imprimir_estatus_de_semaforos(estado_de_los_semaforos):
	"""
	Funcion que imprime el status de cada semaforo, es decir,
	cuales semaforos estan prendidos y cuales estan apagados
	"""
	semaforos_en_verde = ""
	semaforos_en_rojo = ""

	# Se recorre el arreglo de semaforos
	for index in range(len(estado_de_los_semaforos)):
		# Si el semaforo esta encendido, se agrega el semaforo a semaforos_en_verde
		if estado_de_los_semaforos[index] == 1:
			semaforos_en_verde = semaforos_en_verde + " " + nombre_de_carril[index]
		else: # Si el semaforo esta apagado, se agrega a los semaforos en rojo
			semaforos_en_rojo = semaforos_en_rojo + " " + nombre_de_carril[index]

	print "Semaforos en verde: {}\tSemaforos en rojo: {}".format(semaforos_en_verde, semaforos_en_rojo)


def imprimir_carros_por_carril():
	"""
	Funcion que imprime el trafico en cada uno de los carriles.
	"""
	for carril in range(len(carros_en_carril)):
		print "\tCarros en el carril {} = {}".format(nombre_de_carril[carril], carros_en_carril[carril])
	print "\n"


def obtener_tiempo_en_verde(estado_de_los_semaforos):
	"""
	Funcion que regresa la cantidad de segundos que los semaforos van a estar en verde, 
	como se tienen 2 semaforos encendidos a la vez, el tiempo en verde lo decide el semaforo
	que tiene el mayor numero de segundos
	"""
	tiempo_en_verde = 5 # Es el minimo de segundos por semaforo

	for index in range(len(estado_de_los_semaforos)):
		# Si el semaforo esta encendido se revisa el tiempo en verde de ese semaforo
		if estado_de_los_semaforos[index] == 1:
			# Si el tiempo en ese semaforo es mayor que el tiempo en verde actual, se actualiza la variable con el tiempo mayor
			tiempo_en_verde = tiempo_por_carril[index] if tiempo_por_carril[index] > tiempo_en_verde else tiempo_en_verde

	return tiempo_en_verde



# Comienza mpieza la ejecucion del programa
print "Simulacion de cruce de calles con semaforos"
print "Inicializar el trafico:"
agregar_trafico_carriles()
print "\n\n"
simula_cruce_con_semaforo()
