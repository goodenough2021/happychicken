import pygame,sys,os

from pygame.display import set_caption

def load_graphics(path,accept=('.jpg','.png','.bmp','.gif')):
    graphics = {}
    for pic in os.listdir(path):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(path,pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
            graphics[name] = img
    return graphics

def get_image(sheet,x,y,width,height,colorkey,scale):
    image = pygame.Surface((width,height))
    image.blit(sheet,(0,0),(x,y,width,height))
    image.set_colorkey(colorkey)
    image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
    return image




if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('HappyChicken')

    # image1 = pygame.image.load(r'files/chicken.png')
    GRAPHICS = load_graphics(r'files')
    print(GRAPHICS)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill('blue')
        image = get_image(GRAPHICS[r'chicken'],124,269,75,75,(0,0,0),2)
        image_rect = image.get_rect()
        image_rect.center = (800/2,600/2)
        
        screen.blit(image,image_rect.center)
        pygame.display.update()

