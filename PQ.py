class PriorityQueue:

	def __init__(self):
		self.cola = [] #elemntos
		self.indice = []

	def insert(self,k,v):
		if not k in self.indice:
			self.cola.append([k,v])
			self.indice.append(k)
			self.move(len(self.cola)-1)
		else:
			i = self.indice.index(k)
			if v < self.cola[i][1]:
				self.cola[i][1] = v
				self.move(i)

	def move(self,n):
		if n == 0:
			return
		else:
			if self.cola[n][1] <= self.cola[n-1][1]:
				self.cola[n-1],self.cola[n] = self.cola[n],self.cola[n-1]
				self.indice[n],self.indice[n-1] = self.indice[n-1],self.indice[n]
				self.move(n-1)

	def pop(self):
		self.indice.pop(0)
		return self.cola.pop(0)

	def show(self):
		print(self.cola)
		#print(self.indice)

	def size(self):
		return len(self.cola)

'''
c = PriorityQueue()
c.insert('R',6)
c.insert('l',4)
c.insert('x',1)
c.insert('y',4)
c.show()
c.insert('y',1)
c.show()
print(c.pop())
c.show()
print(c.size()) '''