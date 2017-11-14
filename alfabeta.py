import copy
import pygame
import sys

ANCHO = 300 
ALTO = 300
NEGRO = (0,0,0)
BLANCO = (255,255,255)
ROJO = (255,0,0)

def evaluation(nodo): # esta funcion evalua para saber si se puede ganar de alguna forma
	for i in range(3):
		#caso horizontal
		if nodo[i][0] == nodo[i][1] and nodo[i][0] == nodo[i][2] and nodo[i][0] != ' ':
			if nodo[i][0] == 'x':
				return 1
			else:
				return -1
		# caso vertical
		if nodo[0][i] == nodo[1][i] and nodo[0][i] == nodo[2][i] and nodo[0][i] != ' ':
			if nodo[0][i] == 'x':
				return 1
			else:
				return -1
	#caso diagonal
	if nodo[0][0] == nodo[1][1] and nodo[1][1] == nodo[2][2] and nodo[0][0] != ' ':
		if nodo[0][0] == 'x':
			return 1
		else:
			return -1

	if nodo[0][2] == nodo[1][1] and nodo[1][1] == nodo[2][0] and nodo[0][2] != ' ':
		if nodo[0][2] == 'x':
			return 1
		else:
			return -1

	return 0 # hay un empate

def nodo_terminal(nodo,jugador): # verifico si es un nodo termial
	if evaluation(nodo) != 0 or len(sons(nodo,jugador)) == 0:
		return True
	else:
		return False

def sons(nodo,jugador): #se crean los hijos
	posibles = []
	for i in range(3):
		for j in range(3):
			if nodo[i][j] == ' ':
				newnode = copy.deepcopy(nodo)
				if jugador == 1:
					newnode[i][j] = 'x'
				else:
					newnode[i][j] = 'o'
				posibles.append(newnode)
	return posibles

def alfabeta(nodo,alfa,beta,jugador): # se le puede agregar un limite de profundidad
	jugada = nodo
	if nodo_terminal(nodo,jugador): # si el nodo es terminal o la profundidad es igual a cero
		return evaluation(nodo), nodo

	if jugador == 1:
		for hijo in sons(nodo,1):
			#show(hijo)
			alfaaux = alfabeta(hijo,alfa,beta,2)[0] # profundidad-1
			if alfaaux > alfa:
				alfa = alfaaux
				jugada = hijo
			if beta <= alfa:
				break
		return alfa, jugada
	else:
		for hijo in sons(nodo,2):
			betaaux = alfabeta(hijo,alfa,beta,1)[0] # profundidad-1
			if betaaux < beta:
				beta = betaaux
				jugada = hijo
			if beta <= alfa:
				break
		return beta, jugada

def show(nodo):
	for i in nodo:
		print(i)

if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode([ANCHO,ALTO])
	fuente = pygame.font.Font(None,150)
	inicial = []
	for i in range(3): # se llena el triki de ' '
		fila = []
		for j in range(3):
			fila.append(' ')
		inicial.append(fila) 
	jugador = 2
	pantalla.fill(BLANCO)
	for i in range(2):
		pygame.draw.line(pantalla,NEGRO,((i+1)*100,0),((i+1)*100,300))
		pygame.draw.line(pantalla,NEGRO,(0,(i+1)*100),(300,(i+1)*100))		
	pygame.display.flip()

	while True: #ciclo del juego

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		if not nodo_terminal(inicial,jugador): #se evalua si ya no hay jugadas
			if jugador == 1:
				inicial = alfabeta(inicial,-float('inf'),float('inf'),jugador)[1]
				for i in range(3):
					for j in range(3):
						if inicial[i][j] != ' ':
							simbolo = fuente.render(inicial[i][j],True,ROJO)
							pantalla.blit(simbolo,[(i*100)+20,(j*100)])
				jugador = 2
			else: # turno del jugador min, es decir nosotros
				aux = False
				pos = []
				while not aux:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							sys.exit()
						if event.type == pygame.MOUSEBUTTONDOWN:
							pos = event.pos
							aux = True
				#print(pos[0],pos[1])
				'''print("posicion i:")
				x = int(input())
				print("posicion j:")
				y = int(input()) '''
				if inicial[int(pos[0]/100)][int(pos[1]/100)] == ' ':
					inicial[int(pos[0]/100)][int(pos[1]/100)] = 'o'
					simbolo = fuente.render('o',True,ROJO)
					pantalla.blit(simbolo,[(int(pos[0]/100)*100)+20,(int(pos[1]/100)*100)])
					jugador = 1
		else:
			
		'''
		pantalla.fill(BLANCO)
		for i in range(2):
			pygame.draw.line(pantalla,NEGRO,((i+1)*100,0),((i+1)*100,300))
			pygame.draw.line(pantalla,NEGRO,(0,(i+1)*100),(300,(i+1)*100)) '''
			
		pygame.display.flip()