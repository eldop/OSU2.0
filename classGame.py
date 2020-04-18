import pygame, classLVL
pygame.init()


class Game():
    def __init__(self):
        self.font = pygame.font.SysFont('DOCKER THREE', 40)

        self.background = pygame.image.load('background.jpg')

        self.FPS = 30
        self.clock = pygame.time.Clock()


        self.over = False
        self.display = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)


    def update(self):
        self.clock.tick(self.FPS)
        self.display.blit(self.background, (0, 0))

        pygame.display.update()