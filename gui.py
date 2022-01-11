import pygame
import solver
import time

pygame.display.init()
pygame.font.init()

screen = pygame.display.set_mode((675, 575))

icon = pygame.image.load('brain.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Sudoku")
font = pygame.font.Font('font.ttf', 28)
cross = pygame.image.load('cross.png')

sudoku = [
    [0, 0, 4, 0, 9, 0, 8, 0, 5],
    [0, 5, 0, 0, 0, 7, 2, 0, 0],
    [0, 3, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 4, 0, 0, 0, 2, 9],
    [0, 0, 0, 0, 7, 0, 0, 0, 8],
    [5, 0, 0, 0, 8, 1, 3, 7, 4],
    [0, 2, 1, 0, 0, 0, 5, 0, 0],
    [6, 0, 0, 3, 0, 0, 0, 1, 0],
    [0, 0, 0, 6, 1, 0, 4, 3, 0]
]


def button(x, y, width, height, txt):
    pressed = False
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # Pressed
    if x < mouse_pos[0] < x + width and y < mouse_pos[1] < y + height and click[0] == 1:
        pygame.draw.rect(screen, (98, 146, 158), (x, y, width, height), 2)
        display_txt = font.render(txt, True, (98, 146, 158))
        pressed = True
    # Not pressed
    else:
        pygame.draw.rect(screen, (57, 61, 63), (x, y, width, height), 2)
        display_txt = font.render(txt, True, (57, 61, 63))

    screen.blit(display_txt, (x + 20, y + 10))
    return pressed


def add_zero(time):
    if len(str(time)) == 1:
        time = "0" + str(time)
    return time


def format_time(time):
    sec = time % 60
    sec = add_zero(sec)
    mins = time // 60
    mins = add_zero(mins)
    formatted = str(mins) + " : " + str(sec)
    return formatted


def draw(faults, time):
    # Mistakes
    for fault in range(faults):
        screen.blit(cross, (25 + 40 * fault, 525))
    # Time
    time_txt = font.render(format_time(time), True, (57, 61, 63))
    screen.blit(time_txt, (310, 17))


running = True
key = None
mistakes = 2

start_time = time.time()
while running:
    screen.fill((222, 226, 230))
    pygame.draw.rect(screen, (253, 253, 255), (112, 62, 450, 450))
    play_time = round(time.time() - start_time)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                key = 1
            if event.key == pygame.K_2:
                key = 2
            if event.key == pygame.K_3:
                key = 3
            if event.key == pygame.K_4:
                key = 4
            if event.key == pygame.K_5:
                key = 5
            if event.key == pygame.K_6:
                key = 6
            if event.key == pygame.K_7:
                key = 7
            if event.key == pygame.K_8:
                key = 8
            if event.key == pygame.K_9:
                key = 9

    if button(291, 520, 92, 50, "Solve"):
        solver.solver(sudoku)

    draw(mistakes, play_time)

    for i, line in enumerate(sudoku):

        for j, digit in enumerate(line):
            num = None
            if digit != 0:
                num = str(digit)
            if button(112 + j * 50, 62 + i * 50, 50, 50, num) and str(key).isalnum():
                if solver.legit(sudoku, key, (i, j)):
                    pass

    pygame.display.update()
