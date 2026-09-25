import pygame 
import random
pygame.init()
SPRITE_COLOUR_CHANGE_EVENT=pygame.USEREVENT +1
BACKGROUND_COLOUR_CHANGE_EVENT=pygame.USEREVENT +2
BLUE=pygame.Colour('blue')
LIGHTBLUE=pygame.Colour('lightblue')
DARKBLUE=pygame.Colour('darkblue')
YELLOW=pygame.Colour('yellow')
MAGENTA=pygame.Colour('Magenta')
ORANGE=pygame.Colour('orange')
WHITE=pygame.Colour('White')
class Sprite(pygame.sprite.Sprite) :
    def init_(self,colour,widthight):
super()._init_()
 self.image=pygame.Surface(([width,height])
self.image.fill(colour)
self.rect=self.image.get_rect()
self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
def update(self) :
    self.rect.move_ip(self.velocity)
    boundary_hit=False
    if self.rect.left<=0 or self.rect.right>=500:
        self.velocity[0] = -self.velocity[0]
        boundary_hit=True
    if self.rect.top<=0 or self.rect.bottom >=400:
        self.velocity[1]=-self.velocity[1]
        boundary_hit=True
    if boundary_hit :
pygame.event.post(pygame.event.Event(SPRITE_COLOUR_CHANGE_EVENT))
pygame.event.post(pygame.event.Event(BACKGROUND_COLOUR_CHANGE_EVENTT))
    def change_colour(self):
        self.image.fill(random.choice([YELLOW,MAGENTA,ORANGE,WHITE]))
    def change_background_colour():
        global bg_colour
        bg_colour=random.choice([BLUE,LIGHT,DARKBLUE])
        
    all_spites_list=pygame.sprite.Group()
    sp1=Sprite(WHITE,20,30)
    sp1.rect.x=random.randint(0,480)
    sp1.rect.y=random.randint(0,370)
    all_sprites_list.add(sp1)
    
    screen=pygame.display.set_mode((500,400))
    pygame.display.set_caption("Boundary Sprite")
    bg_colour=BLUE
    screen.fill(bg_colour)
    exit=False
    clock=pygame.time.Clock()
    while not exit :
        for event in pygame.event.get() :
            if event.type==pygame.QUIT:
                exit=True
            elif event.type==SPRITE_COLOUR_CHANGE_EVENT:
                sp1.change_colour()
            elif event.type==BACKGROUND_COLOUR_CHANGE_EVENT:
                change_background-colour()
            all_sprites_list.update()
            screen.fill(bg_colour)
            all_sprites_list.draw(screen)
            pygame.display.flip()
            clock.tick(240)
            pygame.quit()