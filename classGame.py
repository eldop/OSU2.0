import pygame, classCircle
pygame.init()


class Game():
    def __init__(self):
        self.font = pygame.font.SysFont('Algerian', 40)

        self.background = pygame.image.load('background.jpg')

        self.FPS = 30
        self.clock = pygame.time.Clock()


        self.over = False
        self.display = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

        self.group = pygame.sprite.LayeredUpdates()

        self.n = 1
        self.num = 0
        self.score = 0
        self.scorenumber = self.font.render(str(self.score), True, (255, 255, 255))


    def update(self):
        self.clock.tick(self.FPS)
        self.display.blit(self.background, (0, 0))
        self.display.blit(self.scorenumber, (0,0))
        self.group.draw(self.display)
        pygame.display.update()

    def spawn(self):
        if len(self.group.sprites()) < 5:
            self.group.add(classCircle.Circle(self.n))
            self.n += 1
        else:
            for r in self.group.sprites():
                r.kill()
                self.n = 1
                self.num = 0


    def checkclick(self, pos):
        sprtlist = self.group.get_sprites_at(pos)
        for k in sprtlist:
            if k.n == self.num + 1:
                k.kill()
                self.num += 1
        if self.num > self.score:
            self.score = self.num
            self.scorenumber = self.font.render(str(self.score), True, (255, 255, 255))