import pygame


def read_keyboard_input():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                print(pygame.key.name(event.key))
                return pygame.key.name(event.key)


if __name__ == "__main__":
    running = "a"
    while running != "q":
        running = read_keyboard_input()
    # read_keyboard_input()
