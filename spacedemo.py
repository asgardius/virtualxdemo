import sys
import pygame
import threading
import time
import datetime
import platform
import subprocess
#introplay = "ffplay -autoexit -window_title Intro intro.ogv"
#process = subprocess.Popen(introplay.split(), stdout=subprocess.PIPE)
#output, error = process.communicate()
pygame.init()
pygame.joystick.init()
screen = pygame.display.set_mode((1024, 600))
pygame.display.set_caption('Space - Virtualx Game Engine')
font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()
FPS = 60
BLACK = (0, 0, 0)
#WHITE = (255, 255, 255)
pygame.mixer.music.load('space.ogg')
csfx = pygame.mixer.Sound('crash.ogg')
pygame.mixer.music.play(-1)
#sound = pygame.mixer.Sound(file='bmx.ogg')
#raw_array = sound.get_raw()
#raw_array = raw_array[100000:92557920]
#cut_sound = pygame.mixer.Sound(buffer=raw_array)
#cut_sound.play(-1)
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('galaxy.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.velocity = [0, 0]
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 12
        self.y = 190
        self.image = pygame.image.load('ss.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect = pygame.Rect(self.x,self.y,108, 68)
        self.velocity = [0, 0]

    def update(self):
        self.rect.move_ip(*self.velocity)
class Css1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 400
        self.y = 190
        self.image = pygame.image.load('css.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect = pygame.Rect(self.x,self.y,108, 68)
        self.velocity = [0, 0]

    def update(self):
        self.rect.move_ip(*self.velocity)
class Css2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 500
        self.y = 400
        self.image = pygame.image.load('css.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect = pygame.Rect(self.x,self.y,108, 68)
        self.velocity = [0, 0]

    def update(self):
        self.rect.move_ip(*self.velocity)
class Sat1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 550
        self.y = -100
        self.image = pygame.image.load('sat.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect = pygame.Rect(self.x,self.y,30, 22)
        self.velocity = [0, 0]

    def update(self):
        self.rect.move_ip(*self.velocity)
class Goal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 3000
        self.y = -200
        self.image = pygame.image.load('radio.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect = pygame.Rect(self.x,self.y,69, 120)
        self.velocity = [0, 0]

    def update(self):
        self.rect.move_ip(*self.velocity)
class Ast1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 120
        self.y = 200
        self.image = pygame.image.load('asteroid.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect = pygame.Rect(self.x,self.y,108, 78)
        self.velocity = [0, 0]

    def update(self):
        self.rect.move_ip(*self.velocity)
class Ast2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 300
        self.y = 100
        self.image = pygame.image.load('asteroid.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect = pygame.Rect(self.x,self.y,108, 78)
        self.velocity = [0, 0]

    def update(self):
        self.rect.move_ip(*self.velocity)
class Ast3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 500
        self.y = 150
        self.image = pygame.image.load('asteroid.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect = pygame.Rect(self.x,self.y,108, 78)
        self.velocity = [0, 0]

    def update(self):
        self.rect.move_ip(*self.velocity)
player = Player()
css1 = Css1()
css2 = Css2()
sat1 = Sat1()
goal = Goal()
ast1 = Ast1()
ast2 = Ast2()
ast3 = Ast3()
background = Background()
running = True
live = True
#rect = pygame.Rect((0, 0), (32, 32))
#image = pygame.Surface((32, 32))
#image.fill(WHITE)
while running:
    dt = clock.tick(FPS) / 1000
    screen.fill(BLACK)
    datetime.datetime.now()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    ax = joystick.get_axis(0)
    ay = joystick.get_axis(1)
    bx = joystick.get_axis(3)
    by = joystick.get_axis(4)
    b0 = joystick.get_button(0)
    b1 = joystick.get_button(1)
    b2 = joystick.get_button(2)
    b3 = joystick.get_button(3)
    player.velocity[0] = 600 * dt * (ax - bx)
    player.velocity[1] = 600 * dt * (ay - by)
    css1.velocity[0] = -600 * dt * bx
    css1.velocity[1] = -600 * dt * by
    css2.velocity = css1.velocity
    sat1.velocity = css1.velocity
    goal.velocity = css1.velocity
    ast1.velocity[0] = -200 * dt * bx
    ast1.velocity[1] = -200 * dt * by
    ast2.velocity[0] = -150 * dt * bx
    ast2.velocity[1] = -150 * dt * by
    ast3.velocity[0] = -120 * dt * bx
    ast3.velocity[1] = -120 * dt * by
    
    if pygame.sprite.collide_rect(player, css1):
        live = False
        pygame.mixer.music.stop()
        csfx.play()
        player = Player()
        css1 = Css1()
        css2 = Css2()
        sat1 = Sat1()
        goal = Goal()
        ast1 = Ast1()
        ast2 = Ast2()
        ast3 = Ast3()
    elif pygame.sprite.collide_rect(player, css2):
        live = False
        pygame.mixer.music.stop()
        csfx.play()
        player = Player()
        css1 = Css1()
        css2 = Css2()
        sat1 = Sat1()
        goal = Goal()
        ast1 = Ast1()
        ast2 = Ast2()
        ast3 = Ast3()
    elif pygame.sprite.collide_rect(player, sat1):
        live = False
        pygame.mixer.music.stop()
        csfx.play()
        player = Player()
        css1 = Css1()
        css2 = Css2()
        sat1 = Sat1()
        goal = Goal()
        ast1 = Ast1()
        ast2 = Ast2()
        ast3 = Ast3()
    if b0:
        pygame.mixer.music.stop()
    elif b1:
        pygame.mixer.music.play(-1)
    elif b2:
        live = False
        pygame.mixer.music.stop()
        csfx.play()
        player = Player()
        css1 = Css1()
        css2 = Css2()
        sat1 = Sat1()
        goal = Goal()
        ast1 = Ast1()
        ast2 = Ast2()
        ast3 = Ast3()
    elif b3:
        live = True
        pygame.mixer.music.play(-1)
    player.update()
    css1.update()
    css2.update()
    sat1.update()
    goal.update()
    ast1.update()
    ast2.update()
    ast3.update()

    screen.blit(background.image, background.rect)
    if live:
        screen.blit(ast3.image, ast3.rect)
        screen.blit(ast1.image, ast2.rect)
        screen.blit(ast1.image, ast1.rect)
        screen.blit(player.image, player.rect)
        screen.blit(css1.image, css1.rect)
        screen.blit(css2.image, css2.rect)
        screen.blit(sat1.image, sat1.rect)
        screen.blit(goal.image, goal.rect)
    rfps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
    sysclock = font.render(str(datetime.datetime.utcnow()), True, pygame.Color('white'))
    cpuarch = font.render(str(platform.machine()), True, pygame.Color('white'))
    #infox = font.render(str(bx), True, pygame.Color('white'))
    #infoy = font.render(str(by), True, pygame.Color('white'))
    screen.blit(rfps, (50, 50))
    screen.blit(sysclock, (120, 50))
    screen.blit(cpuarch, (50, 80))
    #screen.blit(infox, (50, 110))
    #screen.blit(infoy, (50, 140))
    pygame.display.update()