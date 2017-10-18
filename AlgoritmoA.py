import pygame 
from lab import *

ANCHO = 500
BLANCO = (255,255,255)
ROJO = (255, 0, 0)
AZUL = (0,0,255)
VERDE = (0,255,0)
LOCO = (100,100,100)


class InterfasInicio(pygame.sprite.Sprite):
	pygame.font.init()
	Fuente1 = pygame.font.Font(None, 46)
	Fuente2 = pygame.font.Font(None, 36)
	Texto1 = Fuente1.render("BIENVENIDO", 0, (0, 0, 0))
	Texto2 = Fuente2.render("Definido",0, (0, 0, 0))
	Texto3 = Fuente2.render("Sin Definir", 0, (0, 0, 0))
	y = 200
	Selector = pygame.Surface((20, 20))
	Selector.fill(ROJO)
	def __init__(self, p):
		self.p = p
		p.fill(BLANCO)
		p.blit(self.Texto1, (210, 100))
		p.blit(self.Texto2, (250, 200))
		p.blit(self.Texto3, (250, 250))
		p.blit(self.Selector, (219,self.y))
		pygame.display.flip()

	def mov(self, y):
		self.y += y
		if(self.y < 200):
			self.y = 250;
		if(self.y > 250):
			self.y = 200;
		self.update()

	def update(self):
		self.p.fill(BLANCO)
		self.p.blit(self.Texto1, (210, 100))
		self.p.blit(self.Texto2, (250, 200))
		self.p.blit(self.Texto3, (250, 250))
		self.p.blit(self.Selector, (219,self.y))
		pygame.display.flip()


if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode((ANCHO,ANCHO))
	reloj = pygame.time.Clock()
	niveles = 0
	an_cua = ANCHO/10
	validacion = True
	while validacion:
		if niveles == 0:
			inicio = InterfasInicio(pantalla)
			val = True
			while val:
				reloj.tick(60)
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_UP:
							inicio.mov(-50)
						if event.key == pygame.K_DOWN:
							inicio.mov(50)
						if (event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN):
							if inicio.y == 200:
								mapa = [[0,1,1,1,1,1,1,1,1,1], # 0
										   [0,0,1,0,0,0,0,1,1,1], # 1
										   [0,0,1,0,1,1,0,1,1,1], # 2
										   [1,0,1,0,1,1,0,0,0,1], # 3
										   [1,0,1,0,1,1,1,0,0,1], # 4
										   [1,0,1,0,0,0,0,1,0,1], # 5
										   [1,0,0,1,1,1,0,1,0,0], # 6
										   [1,0,0,0,0,0,0,1,0,1], # 7
										   [1,0,0,0,1,1,1,1,0,1], # 8
										   [1,1,1,0,0,0,0,0,0,1]  # 9
										]  

							if inicio.y == 250:
								mapa = []
								for i in range(10):
									s = []
									for j in range(10):
										s.append(0)
									mapa.append(s)
							x = -100
							y = -100
							niveles = 1
							val = False
						if event.key == pygame.K_ESCAPE:
							validacion = False
							val = False
					if event.type == pygame.QUIT:
						validacion = False
						val = False

		if niveles == 1:
			salida = [-100, -100]
			empieza = [-100, -100]	
			val = True	
			while val:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						validacion = False
						val = False
					if event.type == pygame.MOUSEBUTTONDOWN:
						if event.button == 1:
							x,y = event.pos
					if event.type == pygame.KEYDOWN:
						if x>=0 and y >= 0:
							if event.key == pygame.K_b:
								mapa[int(y/an_cua)][int(x/an_cua)] = 1
							if event.key == pygame.K_e:
								empieza = [int(x/an_cua),int(y/an_cua)]
							if event.key == pygame.K_s:
								salida = [int(x/an_cua),int(y/an_cua)]
						if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
							val = False
							niveles = 2

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
			if niveles == 2:
				if(camino != 'no encontre solucion'):
					for elem in camino:
						pygame.draw.rect(pantalla, LOCO, [elem[0]*an_cua, elem[1]*an_cua, an_cua, an_cua])
					pygame.display.flip()
				else:
					pantalla.fill(BLANCO)
					Fuente1 = pygame.font.Font(None, 46)
					Texto1 = Fuente1.render("NO ENCONTRE LA SOLUCION", 0, (0, 0, 0))
					pantalla.blit(Texto1, (15, 200))
					pygame.display.flip()
				val = True
				while val:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							validacion = False
							val = False
						if event.type == pygame.KEYDOWN:
							niveles = 0
							val = False