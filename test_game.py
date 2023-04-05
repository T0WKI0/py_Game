import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Snail Run')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# BG
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# Title
text_surf = test_font.render('Snail Run', False, ('#ea00ff'))
text_rect = text_surf.get_rect(midbottom = (400,50))

# Snail
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomleft = (800, 300))

# Player
player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Space-jump
        if event.type == pygame.KEYDOWN and player_rect.bottom >= 300:
            if event.key == pygame.K_SPACE:
                player_gravity = -20
        # Mouse-jump
        if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
            if player_rect.collidepoint(event.pos):
                player_gravity = -20

    # BG
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    pygame.draw.rect(screen, (100,100,100), text_rect)
    pygame.draw.rect(screen, (100,100,100), text_rect, 10, 10)
    screen.blit(text_surf,text_rect)

    # Snail
    screen.blit(snail_surf,snail_rect)
    snail_rect.left -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    
    # Player
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom > 300:
        player_rect.bottom = 300
    screen.blit(player_surf,player_rect)


    if player_rect.colliderect(snail_rect):
        print('collision')
    
    pygame.display.update()
    clock.tick(60)