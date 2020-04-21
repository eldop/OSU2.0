import pygame, random
pygame.init()

class Circle(pygame.sprite.Sprite):
    def __init__(self, n):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont('Algerian', 80)

        self.image = pygame.image.load('circle.png')
        self.image = pygame.transform.scale(self.image,(200, 200))
        self.rect = self.image.get_rect()

        self.spawnball()


        self.n = n
        self.text()

    def spawnball(self):
        self.rect.center = [random.randint(0,1700), random.randint(0,800)]

    def text(self):
        self.number = self.font.render(str(self.n), True, (255, 255, 255))
        self.nrect = self.number.get_rect()
        self.nrect.center = (99, 99)
        self.image.blit(self.number, self.nrect)
        #self.image.flip()


