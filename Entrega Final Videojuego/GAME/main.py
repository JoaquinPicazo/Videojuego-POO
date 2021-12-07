##################################################################
#																 #
# Estudiantes: Tomas Andrade - Jerson Dominguez - Joaquín Picazo #
#																 #
##################################################################

# Iniciamos pygame y creamos la pantalla del juego
import pygame
from pygame.locals import *

pygame.init()
print("Has abierto el juego")
width = 900
height= 600
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Apocalypse")
clock = pygame.time.Clock()

# Funcion para poner un icono en la pestaña del juego
def icon(dir):
	icon = pygame.image.load(dir)
	pygame.display.set_icon(icon)

# Verifica si cumple los requisitos para subir de nivel, y en caso de cumplirlos sube de nivel
def up():
	global n
	global max_n
	global window
	global play
	global level
	global conditional_win
	n+=1	
	if enemy[n] == enemy[0]:
		level+=1	
	if enemy[n] == enemy[1]:
		print("Sistema: Subiste al nivel 2!")
		level+=1		
	pygame.display.update()
	pygame.time.delay(100)
	if n == max_n:
		play = False
		level=1
		conditional_win=True
		print("Sistema: Has acabado con el apocalipsis!")
		print("Sistema: Has finalizado con " + str(score) + " puntos")

# Clase policía con sus atributos y métodos
class Police():
	# Atributos
	def __init__(self, x, y, speed, health, damage, max):
		self.x = x
		self.y = y
		self.health = health
		self.speed = speed
		self.damage = damage
		self.left = False
		self.right = False
		self.stp = 0
		self.r_walk = [pygame.image.load("img/rn_police.png")]	
		self.l_walk = [pygame.image.load("img/ln_police.png")]
		self.afk = pygame.image.load("img/rn_police.png")
		self.width = self.afk.get_width()
		self.height = self.afk.get_height()
		self.s = [-10, max]		
		self.hb = (self.x + 20, self.y + 100, 130, 250)
	
	# Muestra los elementos que contiene
	def show(self, box):
		printwindow=pygame.font.SysFont("arial", 50)      
		health=printwindow.render("Vida: " + str(self.health) + "/100", True, (255,255,255))		
		if self.stp + 1 > 0:
			self.stp = 0
		if self.left:
			box.blit(self.l_walk[self.stp], (self.x,self.y))
			self.stp += 1
		elif self.right:
			box.blit(self.r_walk[self.stp], (self.x,self.y))
			self.stp += 1
		else:
			box.blit(self.afk, (self.x,self.y))
		self.hb = (self.x + 20, self.y + 100, 130, 250)		
		window.blit(health, (55, 19))
	
	# Teclas
	def keys(self, k, l, r):
		if k[l] and self.x > self.speed:
			self.x -= self.speed
			self.left = True
			self.right = False
			print("Sistema: Te has movido a la izquierda")
		elif k[r] and self.x < width - self.width - self.speed:
			self.x += self.speed
			self.right = True
			self.left = False
			print("Sistema: Te has movido a la derecha")
		else:			
			self.left = False
			self.right = False
			self.stp = 0     

	# Hitbox
	def hit(self, character):
		a1 = self.hb[1] + self.hb[3]
		b1 = self.hb[1]
		c1 = self.hb[0]
		d1 = self.hb[0] + self.hb[2]
		a2 = character.hb[1] + character.hb[3]
		b2 = character.hb[1]
		c2 = character.hb[0]
		d2 = character.hb[0] + character.hb[2]
		return d1 > c2 and c1 < d2 and b1 < a2 and a1 > b2
		

	# Reposiciona al policía al ser impactado
	def boom(self):
		print("Sistema: TE HEMOS REPOSICIONADO")
		self.x = 0
		self.y = 300
		self.stp = 0
		pygame.time.delay(1000)

# Clase zombie (Normal) con sus atributos y métodos
class normal_zombie():
	# Atributos
	def __init__(self, x, y, speed, damage, points, max, health):
		self.x = x
		self.y = y
		self.health = health
		self.speed = speed
		self.damage = damage
		self.points = points
		self.left = False
		self.right = False
		self.stp = 0
		self.r_walk = [pygame.image.load("img/r_zombie.png")]
		self.l_walk = [pygame.image.load("img/l_zombie.png")]		
		self.s = [50, max]
		self.hb = (self.x + 50, self.y , 130, 250)
	
	# Muestra los elementos que contiene 
	def show(self, box):        
		if self.stp + 1 > 1:
			self.stp = 0
		if self.left:
			box.blit(self.l_walk[self.stp], (self.x,self.y))
			self.stp += 1
		elif self.right:
			box.blit(self.r_walk[self.stp], (self.x,self.y))
			self.stp += 1
		
		self.hb = (self.x + 50, self.y , 130, 250)	
	
	# Movimiento automático del zombie
	def IA(self):
		if self.speed > 0:
			if self.x + self.speed < self.s[1]:
				self.x += self.speed 
				self.right = True
				self.left = False
			else:
				self.speed = self.speed * -1
				self.stp = 0
		else:
			if self.x - self.speed > self.s[0]:
				self.x += self.speed 
				self.left = True
				self.right = False
			else:
				self.speed = self.speed * -1
				self.stp = 0
	# Hitbox
	def hit(self, character):
		a1 = self.hb[1] + self.hb[3]
		b1 = self.hb[1]
		c1 = self.hb[0]
		d1 = self.hb[0] + self.hb[2]
		a2 = character.hb[1] + character.hb[3]
		b2 = character.hb[1]
		c2 = character.hb[0]
		d2 = character.hb[0] + character.hb[2]
		return d1 > c2 and c1 < d2 and b1 < a2 and a1 > b2
	
	def boom(self):
		print("Sistema: HEMOS REPOSICIONADO AL ZOMBIE NORMAL")
		self.x = 600
		self.y = 300
		self.stp = 0

# Clase zombie (Jefe) con sus atributos y métodos
class boss_max():
	def __init__(self, x, y, speed, points, damage, health, max):
		self.x = x
		self.y = y
		self.health = health
		self.speed = speed
		self.points = points
		self.damage = damage
		self.left = False
		self.right = False
		self.stp = 0
		self.r_walk = pygame.image.load("img/r_boss.png")
		self.l_walk = pygame.image.load("img/l_boss.png")
		self.s = [50, max]
		self.hb = (self.x + 15, self.y + 10, 30, 50)
	
	# Muestra los elementos que contiene
	def show(self, box):
		if self.stp + 1 > 16:
			self.stp = 0
		if self.left:
			box.blit(self.l_walk, (self.x,self.y))
			self.stp += 1
		elif self.right:
			box.blit(self.r_walk, (self.x,self.y))
			self.stp += 1			

		self.hb = (self.x, self.y , 280, 300)
	
	# Movimiento automático
	def IA(self):
		if self.speed > 0:
			if self.x + self.speed < self.s[1]:
				self.x += self.speed 
				self.right = True
				self.left = False
			else:
				self.speed = self.speed * -1
				self.stp = 0
		else:
			if self.x - self.speed > self.s[0]:
				self.x += self.speed 
				self.left = True
				self.right = False
			else:
				self.speed = self.speed * -1
				self.stp = 0
	
	# Hitbox
	def hit(self, character):
		a1 = self.hb[1] + self.hb[3]
		b1 = self.hb[1]
		c1 = self.hb[0]
		d1 = self.hb[0] + self.hb[2]
		a2 = character.hb[1] + character.hb[3]
		b2 = character.hb[1]
		c2 = character.hb[0]
		d2 = character.hb[0] + character.hb[2]
		return d1 > c2 and c1 < d2 and b1 < a2 and a1 > b2
	
	def boom(self):
		print("Sistema: HEMOS REPOSICIONADO AL ZOMBIE NORMAL")
		self.x = 600
		self.y = 250
		self.stp = 0

# Clase bala con sus atributos y métodos
class Bullet():
	def __init__(self, x,y,a,b, vec):
		self.x = x
		self.y = y
		self.vec = vec
		self.speed = 20 * vec
		self.hb = (self.x,self.y,30,20)
		self.shot = [pygame.image.load("img/r_bullet.png")]
	# Muestra los elementos en pantalla
	def show(self,h):
		self.hb = (self.x,self.y,50,20)
		if vec>0:
			window.blit(self.shot[0], (self.x, self.y))

	# Detecta cuando impacta un enemigo, ocasionando el daño otorgado al policía
	def pium(self, character):
		if character.health > 0:
			character.health -= police.damage
			print("Enemigo: AUCH! Me has dado!")
		else:
			del(character)

# Creamos los personajes a partir de las clases que creamos anteriormente, cada uno con sus propias características
police = Police(50, 300, 15, 100, 50, 600)
zombie = normal_zombie(600, 300, 5, 20, 10, 700, 100)
boss = boss_max(600,250,20,40,20,200, 600)

# Inicializamos el nivel y puntaje del juego
level = 1
score = 0

# Muestra y actualiza el contenido en la pantalla del juego
def display():
	if n <= max_n:
		window.blit(background[n],(0,0))
	else: 
		window.fill((0,0,0))
	police.show(window)
	enemy[n].show(window)
	for b in bs:
		b.show(window)
	printwindow=pygame.font.SysFont("arial", 50)    
	window_points=printwindow.render("Puntos: " + str(score), True, (255,255,255))
	window_level=printwindow.render("Nivel: " + str(level), True, (255,255,255))
	window.blit(window_level, (60, 80))
	window.blit(window_points, (400, 80))
	pygame.display.update()

# Elementos e interacciones de todas las pantallas del juego
playing = True 
while playing:
	n = 0
	max_n = 2
	background = [pygame.image.load('img/bgtrain.png'),pygame.image.load('img/city_bg.png'),pygame.image.load('img/bgtrain.png')]
	score = 0
	conditional_win = False    
	enemy = [zombie, boss, zombie]	
	shots = 0
	bs = []	
	i = True

	# Elementos de la pantalla de la introducción del juego
	while i:
		in_bg=pygame.image.load("img/intro_bg.png")
		arial = pygame.font.SysFont('arial',30, True)
		clock.tick(30)
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				quit()	
		icon("img/icon.jpg")	
		window.blit(in_bg,(0,0))		
		title = arial.render("APOCALYPSE", 1, (255,0,0))
		i1 = arial.render('Presiona "Espacio" para iniciar el juego', 1, (255,255,255))
		i2 = arial.render('Te mueves con las teclas:  <--    -->', 1, (255,255,255))
		i3 = arial.render('Disparas con:  X', 1, (255,255,255))
		window.blit(title, (367, 180))
		window.blit(i1, (100, 450))
		window.blit(i2, (100, 400))
		window.blit(i3, (100, 350))
		key = pygame.key.get_pressed()
		if key[pygame.K_SPACE]:
			print("Has iniciado el juego!")
			i=False
			play = True
		pygame.display.update()
	
	# Elementos e interacciones de la pantalla durante el juego 
	play = True
	while play:
		clock.tick(30)
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				quit()
		k=pygame.key.get_pressed()
		police.keys(k,pygame.K_LEFT, pygame.K_RIGHT)
		enemy[n].IA()
		if police.hit(enemy[n]):
			police.boom()
			zombie.boom()
			boss.boom()
			police.health -= enemy[n].damage
			print("Policía: Me han herido :(")
			print("Policía: Ahora tengo " + str(police.health) + " puntos de vida")	
		if shots > 0:
			shots += 1
		if shots > 2:
			shots = 0
		for b in bs:
			if enemy[n].hit(b):
				b.pium(enemy[n])
				bs.pop(bs.index(b)) 
			if b.x < width and b.x > 0:
				b.x += b.speed
			else:
				bs.pop(bs.index(b)) 		
		if k[pygame.K_x] and shots == 0:
			print("Estas apretando el botón de disparoo!")			
			if police.right:
				vec = 1
			if police.left:
				vec = -1
			else:
				vec = 1
			if len(bs) < 1: 
				bs.append(Bullet(round((police.x + police.width // 2)+50), round(police.height + 110), 6, (0,0,0), vec))
			shots = 1
		if enemy[n].health <= 0:
			score += enemy[n].points
			up()			
		if police.health < 1:
			play = False
			lvl = 1
			print("Sistema: Has muerto :(")
			print("Sistema: Te has llevado " + str(score) + " puntos en total")	
		display()
	
	# Elementos de la pantalla final del juego, en caso de victoria o derrota
	end = True
	while end:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
		end_bg=pygame.image.load("img/end_bg.png")
		win_bg = pygame.image.load("img/win_bg.png")
		window.fill((0,0,0))
		font_end= pygame.font.SysFont('console', 40, True)
		font_end2 = pygame.font.SysFont('console', 30, True)
		points = font_end2.render('Tus puntos: '+ str(score), 1, (255,255,255))
		close = font_end2.render('Presiona "Espacio" para cerrar el juego', 1, (255,255,255))		
		if conditional_win:
			window.blit(win_bg,(0,0))
			window.blit(points, (50, 250))
			window.blit(close, (100, 550))
		else:
			window.blit(end_bg,(0,0))
			message_case2 = font_end.render('You are dead  x_x', 1, (255,0,0))
			window.blit(message_case2, (250, 300))	
			window.blit(points, (320, 180))
			window.blit(close, (100, 400))
		pygame.display.update()

		# Cerrar la pantalla del juego (Tecla espacio)
		keyspressed = pygame.key.get_pressed()
		if keyspressed[pygame.K_SPACE]:
			print("Has cerrado el juego")
			playing=False
			end=False
pygame.quit()
