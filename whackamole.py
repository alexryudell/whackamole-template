import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        moleloc = (0, 0)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if abs(event.pos[0] - moleloc[0]) < 32 and abs(event.pos[1] - moleloc[1]) < 32:
                        moleloc = (random.randrange(0, 608, 32), random.randrange(0, 480, 32))
                        screen.blit(mole_image, mole_image.get_rect())
            screen.fill("light green")
            for i in range(1,16):
                pygame.draw.line(screen, 'black', (0, i*32), (640, i*32))
            for i in range(1,20):
                pygame.draw.line(screen, 'black', (i*32, 0), (i*32, 512))

            screen.blit(mole_image, mole_image.get_rect(topleft=moleloc))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
