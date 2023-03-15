import pygame


def init():
    pygame.init()
    pygame.display.set_mode((256, 256))


def get_key(key_name):
    # final result, True for pressed, False for not pressed
    res = False

    for event in pygame.event.get():
        pass

    key_input = pygame.key.get_pressed()
    my_key = getattr(pygame, 'K_{}'.format(key_name))

    if key_input[my_key]:
        res = True

    pygame.display.update()

    return res


# for test
def main():
    # if get_key("LEFT"):
    #     print("Left key pressed")
    #
    # if get_key("RIGHT"):
    #     print("Right key Pressed")
    print(get_key("a"))


if __name__ == "__main__":
    init()
    while True:
        main()
