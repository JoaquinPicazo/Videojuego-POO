import pygame
from pygame.locals import *

# Estudiantes: Tomas andrade - Alonso Carrasco - Jerson Dominguez - Joaquín Picazo
# Avance 1 - POO

pygame.init()
width = 1000
height = 600
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Apocalypse")
clock = pygame.time.Clock()
i = 0
j= 0
print("\n")
print("Se ha iniciado el juego, lets go!")
print("DATOS DE PERSONAJES")


# Clase Policia
class Police:
	def __init__(self, name, health, damage, speed, x, y, salto):
		self.x = x
		self.y = y
		self.afk = pygame.image.load("img/rn_police.png")
		self.width = self.afk.get_width()
		self.height = self.afk.get_height()
		self.speed = speed
		self.health = health
		self.damage = damage
		self.name = name
		self.salto = salto
		self.jump = False

	def show(self, plot):
		plot.blit(self.afk,(self.x,self.y))

	def keys(self, key, l, r, s, f):
		if key[l] and self.x > self.speed:
			self.x -= self.speed
			print("El policía se ha movido " + str(self.speed) + "px a la izquierda!")

		if key[r] and self.x < width - self.width - self.speed:
			self.x += self.speed
			print("El policía se ha movido " + str(self.speed) + "px a la derecha!")

		if key[s]:
			self.jump = True
				
		
		if self.jump:
				if self.salto>=-10:
					self.y -=(self.salto * abs(self.salto)) * 0.5
					self.salto -=1
				else:
					self.salto = 10
					print(str(self.name) + " ha saltado!")	
					self.jump = False
		if key[f]:
			print("El policia ha disparado!")
				


	def data(self):
		print(self.name + ":")
		print("Su vida es: " + str(self.health))
		print("Su daño es: " + str(self.damage))
		print("Su velocidad es: " + str(self.speed))
		print("\n")

class bullet:
	def __init__(self, direction, speed, x, y):
		self.bullet = [pygame.image.load("img/r_bullet.png"), pygame.image.load("img/l_bullet")]
		self.direction = direction
		self.speed = speed
		self.x = x
		self.y = y

	#def show(self):
		# Aún no habilitamos este metodo, ya que nos falta aplicar la animacion, movimiento y tecla de disparo de la bala
	
	#def fire(self):
		# Aún no habilitamos este metodo, ya que nos falta aplicar la animacion, movimiento y tecla de disparo de la bala

# Superclase enemigo
class enemy():
	def __init__(self, name, health, damage, points, speed, x, y):
		self.name = name
		self.health = health
		self.damage = damage
		self.points = points
		self.speed = speed
		self.x = x
		self.y = y		

	def show(self, cuadro):
		cuadro.blit(self.afk,(self.x,self.y))

	def data(self):
		print(self.name + (":"))
		print("Su vida es: " + str(self.health))
		print("Su daño es: " + str(self.damage))
		print("Su velocidad es: " + str(self.speed))
		print("Los puntos que da al matarlo es: " + str(self.points))
		print("\n")

# Subclase zombie
class zombies(enemy):
	def __init__(self, name, health, damage, points, speed, x, y):
		super().__init__(name, health, damage, points, speed, x, y)
		self.afk = pygame.image.load("img/l_zombie.png")
		self.ancho = self.afk.get_width()
		self.alto = self.afk.get_height()	
	
# Subclase jefe
class boss(enemy):
	def __init__(self, name, health, damage, points, speed, x, y):
		super().__init__(name, health, damage, points, speed, x, y)
		self.afk = pygame.image.load("img/l_boss.png")
		self.ancho = self.afk.get_width()
		self.alto = self.afk.get_height()

# Creando personajes usando las clases anteriores
police = Police("Robert (Police)", 100, 50, 8, 40,200,10)
zombie = zombies("Zombie normal", 100, 20, 10, 5, 750, 300)
bossmax = boss("Boss", 200, 20, 40, 5, 600, 250)

# Mostrando datos de los personajes creados
police.data()
zombie.data()
bossmax.data()
print("\n")
print("MOVIMIENTOS:")

def showgame():
	window.fill((0,0,0))
	window.blit(background,(0,0))
	police.show(window)
	zombie.show(window)
	pygame.display.update()


while True:
	background = pygame.image.load("img/bgtrain.png")	
	type1 = pygame.font.SysFont('dejavuserif', 90, True)
	type2 = pygame.font.SysFont('dejavuserif',30, True)
	front = True
	while front:
		clock.tick(35)
		
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				quit()
		

		window.fill((0,0,0)) 
		title = type1.render("APOCALYPSE", 1, (0, 152, 70))
		alert = type2.render("(En proceso de decoración)", 1, (255,255,255))
		instrucciones = type2.render("Aprete la tecla Espacio para iniciar el juego", 1, (255,255,255))
		titulo2 = type2.render("Teclas y su accion:", 1, (255,255,255))
		teclas1 = type2.render("Derecha: key right ->   Izquierda: key left <-", 1, (255,255,255))
		teclas2 = type2.render("Salto: SPACE      Disparo: x", 1, (255,255,255))
		window.blit(title, (200, 60))
		window.blit(titulo2, (200, 200))
		window.blit(teclas1, (200, 300))
		window.blit(teclas2, (200, 400))
		window.blit(instrucciones, (200, 500))
		window.blit(alert, (300, 550))

		tecla = pygame.key.get_pressed()

		if tecla[pygame.K_SPACE]:
			front=False

		pygame.display.update()

	while True:
		clock.tick(35)
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				quit()

		while int(i)==0:
			print("El " + str(zombie.name) + " ha aparecido en las coordenadas: x=" + str(zombie.x) + " y=" + str(zombie.y) + " de la pantalla")
			print("El " + str(police.name) + " ha aparecido en las coordenadas: x=" + str(police.x) + " y=" + str(police.y) + " de la pantalla")
			i=i+1		
		
		keyboard=pygame.key.get_pressed()
		police.keys(keyboard,pygame.K_LEFT, pygame.K_RIGHT, pygame.K_SPACE, pygame.K_x)
		showgame()
pygame.quit()