import pygame 
from lab import *

ANCHO = 500
BLANCO = (255,255,255)
ROJO = (255, 0, 0)
AZUL = (0,0,255)
VERDE = (0,255,0)
LOCO = (100,100,100)


if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode((ANCHO,ANCHO))
	reloj = pygame.time.Clock()
	an_cua = ANCHO/10
	x = -100
	y = -100
	salida = [-100, -100]
	empieza = [-100, -100]
	mapa = []
	for i in range(10):
		s = []
		for j in range(10):
			s.append(0)
		mapa.append(s)
	validacion = True
	while validacion:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				validacion = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					x,y = event.pos
				if event.button == 3:
					x,y = -100, -100
			if event.type == pygame.KEYDOWN:
				if x>=0 and y >= 0:
					if event.key == pygame.K_b:
						mapa[int(y/an_cua)][int(x/an_cua)] = 1
					if event.key == pygame.K_e:
						empieza = [int(x/an_cua),int(y/an_cua)]
					if event.key == pygame.K_s:
						salida = [int(x/an_cua),int(y/an_cua)]
				if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
					validacion = False
				x,y = -100,-100

		pantalla.fill(BLANCO)
		for i in range(10):
			pygame.draw.line(pantalla, ROJO, [i*an_cua, 0], [i*an_cua, ANCHO])
			pygame.draw.line(pantalla, ROJO, [0, i*an_cua], [ANCHO, i*an_cua])
		for i in range(10):
			for j in range(10):
				if mapa[i][j] == 1:
					pygame.draw.rect(pantalla, AZUL, [j*an_cua, i*an_cua, an_cua, an_cua])
				pygame.draw.rect(pantalla, VERDE, [empieza[0]*an_cua, empieza[1]*an_cua, an_cua, an_cua])
				pygame.draw.rect(pantalla, ROJO, [salida[0]*an_cua, salida[1]*an_cua, an_cua, an_cua])
		pygame.display.flip()
		reloj.tick(60)

	camino = Aestrella(mapa,empieza[0],empieza[1], salida)
	for elem in camino:
		pygame.draw.rect(pantalla, LOCO, [elem[0]*an_cua, elem[1]*an_cua, an_cua, an_cua])
	pygame.display.flip()
	validacion = True
	while validacion:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				validacion = False
			if event.type == pygame.KEYDOWN:
				validacion = False