import pygame
import time

"""Made By: Khaled Ras Guerriche"""

from pygame.locals import*
from time import sleep

class Sprite():
	def __init__(self, xm, ym,height, width,img):
		self.x = xm
		self.y = ym
		self.h = height
		self.w = width
		self.image_image = pygame.image.load(img)

	def isTube(self): return False
	def isMario(self): return False
	def isGoomba(self): return False
	def isFireball(self): return False
	def update(self):
		pass#this is just because my update is an empty function, so instead of using print something I just used pass

class Mario(Sprite):
	def __init__(self, x, y):
		super(Mario, self).__init__(x,y,95,60,"mario1.png")
		self.dest_x=x
		self.dest_y=y
		self.image_image = pygame.image.load("mario1.png")
		self.index = 0
		self.pre_x=0; #cordination for previews mario cordinations x,y 
		self.pre_y=0;
		self.images=[]
		self.images.append("mario1.png")
		self.images.append("mario2.png")
		self.images.append("mario3.png")
		self.images.append("mario4.png")
		self.images.append("mario5.png")
		self.image_image = pygame.image.load(self.images[self.index])
		self.x = x
		self.y = y
		self.h = 95
		self.w = 60
		self.imageCount=0
		self.vert_vel=-2.0 
		self.frameCount =120
		self.marioViewLocation=120
	def isMario(self): return True
	#save Mario's previews cordinations
	def marioWasHere(self):
		self.pre_x =self.x
		self.pre_y =self.y



		#to get mario bounce from the tube
	def bounceFromTube(self,t):
		#to detect if there is a tube where Mario is
		
		if(self.x+self.w >= t.x and self.pre_x < t.x):
			self.x =t.x - self.w

		if(self.x < t.x+ t.w):
			self.x = self.pre_x

		if(self.y+self.h >t.y and self.x+self.w > t.x and self.x < t.x+ t.w ): 
			self.y =t.y-self.h-1
			self.vert_vel =0.0
			self.frameCount=0
		if(self.pre_y>t.y+t.h and self.y>t.y ):
			self.y = t.y-t.h


	def update(self):
		self.vert_vel += 0.7
		self.y +=self.vert_vel
		self.frameCount=self.frameCount+1 #incrreamenting the frame counter

		# to keep mario on the ground level

		if self.y > (500-self.h):
			self.vert_vel = 0.0
			self.y=500-self.h
		if self.y<0:
			self.y=0
			self.vert_vel = 7# will push mario back down, right after he touch y=0


		if self.index > 4:
			self.index = 0

		self.image_image = pygame.image.load(self.images[self.index])

	def draw(self):
		# start preloading
		for i in range(5): 
				self.image_image = pygame.image.load(self.images[i])

	#Jumping method
	def jump(self):
		if self.frameCount<10:
			self.vert_vel += -10


class Tube(Sprite):
	def __init__(self, x, y):
		super(Tube, self).__init__(x,y,400,55,"tube.png")
		self.w=55
		self.h=400
		self.x=x
		self.y=y
		self.image_image = pygame.image.load("tube.png")
	def isTube(self): return True

class Goombas(Sprite):
	def __init__(self, x, y):
		super(Goombas, self).__init__(x,y,118,99,"goomba.png")

		self.x=x
		self.y=y
		self.w = 99;
		self.h = 118;
		self.speed =5;
		self.vert_vel =1.2;
		self.direction =1;
		self.curr_direction=self.direction
		self.isOnFire =False
		self.CountinFire=0
		self.image_image = pygame.image.load("goomba.png")

	def isGoomba(self): return True
		#to get mario bounce from the tube
	def goombaBounceFromTube(self,t):
		self.curr_direction = self.direction
		#to detect if there is a tube where goomba is
		if(self.curr_direction==1):
			self.direction = -1

		if(self.curr_direction==-1):
			self.direction =1

	def update(self):
		self.vert_vel += 0.7;
		self.y += self.vert_vel;
		if(self.isOnFire==True):self.CountinFire+=1##if on fir incr onfircount
		# to keep goombas on the ground level
		if self.y>(500-self.h):
			self.vert_vel = 0.0
			self.y=500-self.h

		self.x+=self.speed*self.direction
	def ONfire(self,g):
		self.image_image = pygame.image.load("goomba_fire.png")
		self.isOnFire = True




class Fireball (Sprite):
	def __init__(self, x, y):
		super(Fireball, self).__init__(x,y,47,47,"fireball.png")
		self.direction=1;
		self.marioToEdge=650 #I used it to remove the firball from screen so I did it right by the edge in purpose
		self.x = x
		self.y = y
		self.w = 47
		self.h = 47
		self.vert_vel =2
		self.speed =10


		self.image_image = pygame.image.load("fireball.png")
	def isFireball(self):
		return True




	def update(self):
		self.vert_vel += 2
		self.y += self.vert_vel
		
		# the ground level
		if(self.y>(500-self.h)):
			self.vert_vel = -20.0
			self.y=400-self.h

		if(self.y<0):
			self.y=0
			self.vert_vel = 7
		self.x+=self.speed*self.direction

class Model():
	def __init__(self):
		self.sprites = []
		self.mario=Mario(120,0)
		self.tube=Tube(0,0)
		self.goombas=Goombas(0,0)
		self.fireball=Fireball(0,0)
		#Tubes
		self.sprites.append(Tube(196,350))
		self.sprites.append(Tube(572,400))
		self.sprites.append(Tube(1096,360))
		self.sprites.append(Tube(1465,380))
		self.sprites.append(Tube(1791,440))

		#Goombas
		self.sprites.append(Goombas(290,100))
		self.sprites.append(Goombas(427,282))
		self.sprites.append(Goombas(731,241))
		self.sprites.append(Goombas(940,225))
		self.sprites.append(Goombas(800,220))
		self.sprites.append(Goombas(1547,192))

		#Mario
		self.sprites.append(self.mario);
	def update(self):

		for sprite in self.sprites:
			if sprite.isTube():
				#if (self.detectSpritesCollusion(sprite)):
				if (self.detectSpritesCollusion(self.mario,sprite) == True):
					self.mario.bounceFromTube(sprite)
				for st in self.sprites:
					if st.isGoomba():
						if (self.detectSpritesCollusion(st, sprite) == True):
							st.goombaBounceFromTube(sprite);
						for sf in self.sprites:
							if sf.isFireball():
								if (self.detectSpritesCollusion(sf, st) == True):
									#time.sleep(1)
									st.ONfire(st)




			sprite.update()

		#to remove the fireball after it goes off the screen
		#first looping throught the sprites
		for se in self.sprites:
		#if the sprite is fireball
			if(se.isFireball()):
             #if the fireball.x isoff screen, do: remove it
				if se.x==(self.mario.x+self.fireball.marioToEdge):
					self.sprites.remove(se)

		#for go in self.sprites:
			if(se.isGoomba()):
				if (se.CountinFire>=5):
						self.sprites.remove(se)
						se.CountinFire=0 


	#collison detection
	def detectSpritesCollusion(self, spri, s): 
		if spri.x+spri.w < s.x: 
			return False
		if spri.x > s.x + s.w:
			return False

		if spri.y + spri.h < s.y:
			return False
		elif spri.y > s.y + s.h:
			return False
		else:
			return True
	#a method to add Fireballs

	def addFireball(self):
		self.f = Fireball(self.mario.x+(self.mario.w/2),self.mario.y+(self.mario.h/2))
		self.sprites.append(self.f)





class View():
	def __init__(self, model):
		screen_size = (800,600)
		self.screen = pygame.display.set_mode(screen_size, 32)
		self.model = model

	def update(self):	 
		self.screen.fill('#82CAFF')
		surface = pygame.display.set_mode((0,500)) 

		pygame.draw.rect(surface, (50,205,50), pygame.Rect(0, 500, 800, 500))
		# Draw sprites 

		for sprite in self.model.sprites:
			self.screen.blit(sprite.image_image,(sprite.x-self.model.mario.x+self.model.mario.marioViewLocation,sprite.y))

		pygame.display.flip()

class Controller():
	def __init__(self, model):
		self.model = model
		self.keep_going = True

	def update(self):
		self.model.mario.marioWasHere()
		for event in pygame.event.get():
			if event.type == QUIT:
				self.keep_going = False
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.keep_going = False
			elif event.type == pygame.MOUSEBUTTONUP:
				pass #self.model.set_dest(pygame.mouse.get_pos()) #don't really need it
		keys = pygame.key.get_pressed()
		if keys[K_LEFT]:
			self.model.mario.x -= 6
			self.model.mario.index=self.model.mario.index+1
		if keys[K_RIGHT]:
			self.model.mario.x += 6
			self.model.mario.index=self.model.mario.index+1
		if keys[K_UP]:
			self.model.mario.y -= 5
		if keys[K_DOWN]:
			self.model.mario.y += 5
		if keys[K_SPACE]:
			self.model.mario.jump()
		if self.model.mario.vert_vel==0:
			self.model.mario.frameCount=0

		if keys[K_LCTRL] or keys[K_RCTRL]:
			self.model.addFireball()

print("Use the arrow keys to move. Press Esc to quit.")
pygame.init()
m = Model()
v = View(m)
c = Controller(m)
while c.keep_going:
	c.update()
	m.update()
	v.update()




	sleep(0.04)
print("It was a Good Class Thank you all ^^")