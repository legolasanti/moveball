#tuşa basılı olduğu müddetçe  hareket etmesini sağlamak

import pygame,sys
import os
pygame.init()
width = 800
height = 600
boyut = (width,height)


pencere = pygame.display.set_mode(boyut)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img/Player")

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
class Parca(pygame.sprite.Sprite):
    def __init__(self,x=width/2,y=height/2):
        super().__init__()
        self.image=pygame.image.load(os.path.join(img_folder,"bal.png")).convert()
        self.image.set_colorkey((0,0,0))
        #self.image.fill(((0,255,0)))
        self.rect = self.image.get_rect()
        self.rect.center=(x,y)

    def update(self, *args):
        up,down,left,right = args
        if self.rect.x>width:
            self.rect.x = 0
        if self.rect.x<0:
            self.rect.x = width
        if self.rect.y>height:
            self.rect.y=0
        if self.rect.y<0:
            self.rect.y=height

        if up:
            self.rect.y-=10
        if down:
            self.rect.y+=10
        if left:
            self.rect.x-=10
        if right:
            self.rect.x+=10



parca1 = Parca()
all_sprites.add(parca1)

while True:
    keys = pygame.key.get_pressed()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()

    if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
        up,down,left,right = keys[pygame.K_UP],keys[pygame.K_DOWN],keys[pygame.K_LEFT],keys[pygame.K_RIGHT]
        all_sprites.update(up,down,left,right)



    pencere.fill((255,255,255))
    all_sprites.draw(pencere)




    pygame.display.update()

