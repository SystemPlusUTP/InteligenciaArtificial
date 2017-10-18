from PQ import *
import copy

salida = []
class Celda:

	def __init__(self,i,j,costo):
		self.i = i 
		self.j = j
		self.costo = costo #g(n)
		self.padres = []

	def get_padres(self):
		return self.padres

def is_solution(posx,posy):
	if posx == salida[0] and posy == salida[1]:
		return True
	else:
		return False

def manhatan(x,y):
	return abs(x-salida[0])+abs(y-salida[1])

def expandir(mapa,nodo):
	hijos = []
	if nodo.j - 1 >= 0:
		if mapa[nodo.j-1][nodo.i] != 1:
			c = Celda(nodo.i,nodo.j-1,nodo.costo+1)
			c.padres = copy.deepcopy(nodo.get_padres())
			c.padres.append([nodo.i,nodo.j])
			hijos.append([c,c.costo+manhatan(c.i,c.j)])

	if nodo.i + 1 <= len(mapa)-1:
		if mapa[nodo.j][nodo.i+1] != 1:
			c = Celda(nodo.i+1,nodo.j,nodo.costo+1)
			c.padres = copy.deepcopy(nodo.get_padres())
			c.padres.append([nodo.i,nodo.j])
			hijos.append([c,c.costo+manhatan(c.i,c.j)])
	
	if nodo.j + 1 <= len(mapa[nodo.i])-1:
		if mapa[nodo.j+1][nodo.i] != 1:
			c = Celda(nodo.i,nodo.j+1,nodo.costo+1)
			c.padres = copy.deepcopy(nodo.get_padres())
			c.padres.append([nodo.i,nodo.j])
			hijos.append([c,c.costo+manhatan(c.i,c.j)])

	if nodo.i - 1 >= 0:
		if mapa[nodo.j][nodo.i-1] != 1:
			c = Celda(nodo.i-1,nodo.j,nodo.costo+1)
			c.padres = copy.deepcopy(nodo.get_padres())
			c.padres.append([nodo.i,nodo.j])
			hijos.append([c,c.costo+manhatan(c.i,c.j)])

	return hijos 


def Aestrella(mapa,x,y, s):
	global salida
	salida = s
	front = PriorityQueue()
	exp = []
	c = Celda(x,y,0)
	front.insert(c,manhatan(x,y))
	while front.size() != 0:
		ps = front.pop()
		if is_solution(ps[0].i,ps[0].j):
			return ps[0].get_padres()
		else: 
			#print(ps[0].i,ps[0].j)
			hijos = expandir(mapa,ps[0])
			exp.append([ps[0].i,ps[0].j])
			for elem in hijos:
				if not [elem[0].i,elem[0].j] in exp:
					front.insert(elem[0],elem[1])

	return 'no encontre solucion'

if __name__ == '__main__':
			#	0 1 2 3 4 5 6 7 8 9
	matriz = [ [0,1,1,1,1,1,1,1,1,1], # 0
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

	print(Aestrella(matriz,empieza[0],empieza[1]))