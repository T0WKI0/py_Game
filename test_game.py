import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Snail Run')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('Snail Run', False, 'Blue')

snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_x_pos = 850

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))

    snail_x_pos -= 4
    screen.blit(snail_surface,(snail_x_pos,265))
    if snail_x_pos < -50:
        snail_x_pos = 850
        


    pygame.display.update()
    clock.tick(60)