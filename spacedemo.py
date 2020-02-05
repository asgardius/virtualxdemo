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
screen = pygame.display.set_mode((512, 448))
pygame.display.set_caption('Space - Virtualx Game Engine')
font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()
FPS = 60
BLACK = (0, 0, 0)
#WHITE = (255, 255, 255)
pygame.mixer.music.load('space.ogg')
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
        super().__init__()
        self.image = pygame.image.load('ss.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect = pygame.Rect((12, 190), (108, 68))
        self.velocity = [0, 0]

    def update(self):
        self.rect.move_ip(*self.velocity)
class P2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('ss.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect = pygame.Rect((400, 190), (108, 68))
        self.velocity = [0, 0]

    def update(self):
        self.rect.move_ip(*self.velocity)
player = Player()
p2 = P2()
background = Background()
running = True
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
    player.velocity[0] = 600 * dt * ax
    player.velocity[1] = 600 * dt * ay
    p2.velocity[0] = 600 * dt * bx
    p2.velocity[1] = 600 * dt * by
    if b0:
        pygame.mixer.music.stop()
    elif b1:
        pygame.mixer.music.play(-1)
    player.update()
    p2.update()

    screen.blit(background.image, background.rect)
    screen.blit(player.image, player.rect)
    screen.blit(p2.image, p2.rect)
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