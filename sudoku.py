import pygame

pygame.init()

width = 550
win = pygame.display.set_mode((width, width))
pygame.display.set_caption("SUDOKU")
bg_color = (251, 247, 245)
original_grid_element_color = (52, 31, 151)
label_font = pygame.font.SysFont("arial", 24)


def main():
    run = True
    clock = pygame.time.Clock()
    win.fill(bg_color)

    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(win, "black", (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(win, "black", (50, 50 + 50 * i), (500, 50 + 50 * i), 4)

        pygame.draw.line(win, "black", (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(win, "black", (50, 50 + 50 * i), (500, 50 + 50 * i), 2)

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
