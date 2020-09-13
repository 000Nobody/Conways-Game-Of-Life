import sys
import pygame
from pygame.locals import *

run = __name__ == '__main__'
clock = pygame.time.Clock()

#-----Options------
WINDOW_SIZE = (1920, 1080) # (width, height) in pixels
CELL_SIZE = 10 # in pixels
FPS = 15 # number of generations per second
#------------------

screen = pygame.display.set_mode(WINDOW_SIZE)
display = pygame.Surface(WINDOW_SIZE)

cells = []
setting_up = True
lmousedown = False
rmousedown = False
show_grid = False
columns = WINDOW_SIZE[0] // CELL_SIZE
rows = WINDOW_SIZE[1] // CELL_SIZE

play_button_img = pygame.image.load('images/play_button.png').convert_alpha()
pause_button_img = pygame.image.load('images/pause_button.png').convert_alpha()

class Cell():
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.living = False
        self.x_coord = self.x // size
        self.y_coord = self.y // size
        self.rect = pygame.Rect(x, y, size, size)

    def getNeighbors(self, cells):
        # Translates the cells position in the 2d array in
        # 8 directions to find the neighboring cells
        neighbors = []
        translate_directions = [
            [0, 1],
            [1, 0],
            [0,-1],
            [-1,0],
            [1,-1],
            [-1,1],
            [1, 1],
            [-1,-1],
        ]
        for translation in translate_directions:
            x = self.x_coord + translation[0]
            y = self.y_coord + translation[1]
            # check if neighbor exists
            if x < 0 or y < 0 or x >= len(cells[0]) or y >= len(cells):
                continue
            neighbors.append(cells[y][x])
        return neighbors

    def update(self):
        living_neigbhors = 0
        for neighbor in self.neighbors:
            if neighbor.living:
                living_neigbhors += 1

        if self.living:
            if living_neigbhors < 2:
                self.lives_next_round = False
            elif living_neigbhors > 3:
                self.lives_next_round = False
            else:
                self.lives_next_round = True
        else:
            if living_neigbhors == 3:
                self.lives_next_round = True
            else:
                self.lives_next_round = False
        # Setting self.lives_next_round instead of self.living so that all cells can update their state at the same time

    def draw(self, display):
        if self.living:
            pygame.draw.rect(display, (255, 255, 255), self.rect)
        else:
            if show_grid:
                pygame.draw.rect(display, (150, 150, 150), self.rect, 1)

# Creating cells and storing them in a 2d array
for i in range(rows):
    cells.append([Cell(j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE) for j in range(columns)])

# Once all cells are created, find all of their neighbors
for row in cells:
    for cell in row:
        cell.neighbors = cell.getNeighbors(cells)

def draw():
    display.fill((50, 50, 50))

    for row in cells:
        for cell in row:
            cell.draw(display)

    if setting_up:
        display.blit(pause_button_img, (0, WINDOW_SIZE[1]-70))
    else:
        display.blit(play_button_img, (0, WINDOW_SIZE[1]-70))

    screen.blit(display, (0, 0))

    pygame.display.update()

while run:
    if not setting_up:
        clock.tick(FPS)

    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_g:
                show_grid = not show_grid

        if setting_up:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    lmousedown = True
                if event.button == 3:
                    rmousedown = True

            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    lmousedown = False
                if event.button == 3:
                    rmousedown = False                    

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    setting_up = False
                if event.key == K_c:
                    for row in cells:
                        for cell in row:
                            cell.living = False

            if lmousedown:
                try:
                    cells[my//CELL_SIZE][mx//CELL_SIZE].living = True
                except IndexError:
                    pass
            if rmousedown:
                try:
                    cells[my//CELL_SIZE][mx//CELL_SIZE].living = False
                except IndexError:
                    pass
        else:
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    setting_up = True

    if not setting_up:
        for row in cells:
            for cell in row:
                cell.update()

        for row in cells:
            for cell in row:
                cell.living = cell.lives_next_round

    draw()