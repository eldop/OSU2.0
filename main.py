import pygame, classGame

game = classGame.Game()
pygame.time.set_timer(pygame.USEREVENT, 1000)
pygame.mixer.music.load('liqwyd-with-you.mp3')
pygame.mixer.music.play()

while not game.over:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game.over = True
        if e.type == pygame.USEREVENT:
            game.spawn()
        if e.type == pygame.MOUSEBUTTONDOWN:
            game.checkclick(e.pos)



    game.update()