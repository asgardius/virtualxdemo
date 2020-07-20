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
FPS = 6000
BLACK = (0, 0, 0)
#WHITE = (255, 255, 255)
pygame.mixer.music.load('space.ogg')
csfx = pygame.mixer.Sound('crash.ogg')
lcfx = pygame.mixer.Sound('complete.ogg')
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
class Supernova(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('supernova.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.velocity = [0, 0]
class Antenna(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('antenna.png')
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
supernova = Supernova()
antenna = Antenna()
running = True
live = True
complete = False
#rect = pygame.Rect((0, 0), (32, 32))
#image = pygame.Surface((32, 32))
#image.fill(WHITE)
while running:
    dt = clock.tick(FPS) / 1000
    #screen.fill(BLACK)
    datetime.datetime.now()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    joystick = pygame.joystick.Joystick(0)
    #tested with ds4 controller on rpi, please use joysticktest script to test your controller
    joystick.init()
    #ax and ay are for left stick
    ax = joystick.get_axis(0)
    ay = joystick.get_axis(1)
    #bx and by are for right stick
    bx = joystick.get_axis(3)
    by = joystick.get_axis(4)
    #b0 is for cross button on ds4
    b0 = joystick.get_button(0)
    #b1 is for circle button on ds4
    b1 = joystick.get_button(1)
    #b2 is for triangle button on ds4
    b2 = joystick.get_button(2)
    #b3 is for square button on ds4
    b3 = joystick.get_button(3)
    if live:
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
    
    if live:
        if pygame.sprite.collide_rect(player, css1):
            live = False
            pygame.mixer.music.stop()
            csfx.play()
            player = Player()
        elif pygame.sprite.collide_rect(player, css2):
            live = False
            pygame.mixer.music.stop()
            csfx.play()
        elif pygame.sprite.collide_rect(player, sat1):
            live = False
            pygame.mixer.music.stop()
            csfx.play()
        elif pygame.sprite.collide_rect(player, goal):
            live = False
            complete = True
            pygame.mixer.music.stop()
            lcfx.play()
    if b0:
        #this stop music playback
        pygame.mixer.music.stop()
    elif b1:
        #this start music playback
        pygame.mixer.music.play(-1)
    elif b2:
        #this trigger spaceship crash event
        live = False
        pygame.mixer.music.stop()
        csfx.play()
    elif b3:
        #this restart the game
        player = Player()
        css1 = Css1()
        css2 = Css2()
        sat1 = Sat1()
        goal = Goal()
        ast1 = Ast1()
        ast2 = Ast2()
        ast3 = Ast3()
        live = True
        complete = False
        pygame.mixer.music.play(-1)
    player.update()
    css1.update()
    css2.update()
    sat1.update()
    goal.update()
    ast1.update()
    ast2.update()
    ast3.update()

    if live:
        screen.blit(background.image, background.rect)
        screen.blit(ast3.image, ast3.rect)
        screen.blit(ast1.image, ast2.rect)
        screen.blit(ast1.image, ast1.rect)
        screen.blit(player.image, player.rect)
        screen.blit(css1.image, css1.rect)
        screen.blit(css2.image, css2.rect)
        screen.blit(sat1.image, sat1.rect)
        screen.blit(goal.image, goal.rect)
    elif complete:
        screen.blit(antenna.image, antenna.rect)
    else:
        screen.blit(supernova.image, supernova.rect)
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