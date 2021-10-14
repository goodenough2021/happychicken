import pygame,sys

from pygame.display import set_caption



if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('HappyChicken')

    image1 = pygame.image.load(r'files/chicken.png')
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill('blue')
        screen.blit(image1,(0,0))
        pygame.display.update()
