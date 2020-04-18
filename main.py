import pygame, classGame

game = classGame.Game()

while not game.over:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game.over = True
    game.update()