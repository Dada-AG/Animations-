import pygame
import time

pygame.init()


screen_width, screen_height = 643, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Oddball Effect: Cute Cat vs Goofy Cat")


cutecat = pygame.image.load("cutecat.jpg")
goofyasscat = pygame.image.load("goofyasscat.jpg")


cutecat = pygame.transform.scale(cutecat, (screen_width, screen_height))
goofyasscat = pygame.transform.scale(goofyasscat, (screen_width, screen_height))


def display_blank(duration):
    screen.fill((0, 0, 0))  
    pygame.display.flip()
    time.sleep(duration)


def display_image_with_gap(image, duration, gap):
    screen.blit(image, (0, 0))
    pygame.display.flip()
    time.sleep(duration)
    display_blank(gap)


def oddball_effect():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        for _ in range(5):
            display_image_with_gap(cutecat, 1, 1)

        
        display_image_with_gap(goofyasscat, 1, 1)

        
        display_image_with_gap(cutecat, 1, 1)

       
        running = False


oddball_effect()

pygame.quit()
