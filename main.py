# Author: Garrett Zhou
# Project: A* Pathfinding Exploration Project
# Version: Due 9/17/26
# Sources: 

# Imports
import pygame
import math
import heapq
import time

#initialize pygame
pygame.init()

# Constants
Header = 40
Rows = 25
Columns = 25
Width = 30
Win = pygame.display.set_mode((Columns * Width, Rows * Width + Header))
pygame.display.set_caption("A* Pathfinding")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

#define cell (a node)
class Cell:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.width = width
        self.g = float('inf')
        self.h = 0
        self.f = float('inf')
        self.came_from = None
        self.state = "unexplored"
    def get_neighbors(self, grid, rows, cols):
        neighbors = []
        directions = [(1, 0, 1), (1, 1, math.sqrt(2)), (0, 1, 1), (-1, 1, math.sqrt(2)), (-1, 0, 1), (-1, -1, math.sqrt(2)), (0, -1, 1), (1, -1, math.sqrt(2))]
        for dr, dc, cost in directions:
            new_row = self.row + dr
            new_col = self.col + dc
            if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                continue
            neighbor = grid[new_row][new_col]
            if neighbor.state == "wall":
                    continue
            neighbors.append((neighbor, cost))
        return neighbors
    def draw(self, win):
        colors = {"unexplored": WHITE, "open": GREY, "closed": RED, "path": GREEN, "wall": BLACK, "start": YELLOW, "goal": BLUE}
        pygame.draw.rect(win, colors[self.state], (self.col*self.width, self.row*self.width + Header, self.width, self.width))

def heuristic_diagonal(cell1, cell2):
    return max(abs(cell1.row - cell2.row), abs(cell1.col - cell2.col))

def heuristic_manhattan(cell1, cell2):
    return abs(cell1.row - cell2.row) + abs(cell1.col - cell2.col)

def heuristic_euclidean(cell1, cell2):
    return math.sqrt((cell1.row - cell2.row)**2 + (cell1.col - cell2.col)**2)

def astar(grid, start, goal, rows, cols, win, heuristic_fn, font, current_heuristic, start_time):
    counter = 0
    open_set = []
    start.g = 0
    start.h = heuristic_fn(start, goal)
    start.f = start.g + start.h
    heapq.heappush(open_set, (start.f, counter, start))
    counter += 1
    while open_set:
        current = heapq.heappop(open_set)[2]
        if current == goal:
            node = goal
            while node is not None:
                node.state = "path"
                node = node.came_from
            return True
        if current.state == "closed":
            continue
        if current != start and current != goal:
            current.state = "closed"

        #animation for A*
        for row in grid:
            for cell in row:
                cell.draw(win)
        # draw labels on top
        pygame.draw.rect(win, WHITE, (0, 0, Columns * Width, Header))
        pygame.draw.line(win, BLACK, (0, Header), (Columns * Width, Header), 2)
        heuristic_text = font.render(f"Heuristic: {current_heuristic} (H to switch)", True, BLACK)
        win.blit(heuristic_text, (10, 10))

        live_elapsed = time.time() - start_time
        time_text = font.render(f"Time: {live_elapsed:.2f}s", True, BLACK)
        win.blit(time_text, (500, 10))
        pygame.display.update()
        pygame.time.delay(50) #arbitrary choice


        for neighbor, cost in current.get_neighbors(grid, rows, cols):
            new_g = current.g + cost
            if new_g < neighbor.g:
                neighbor.came_from = current
                neighbor.g = new_g
                neighbor.h = heuristic_fn(neighbor, goal)
                neighbor.f = neighbor.g + neighbor.h
                heapq.heappush(open_set, (neighbor.f, counter, neighbor))
                counter += 1
                neighbor.state = "open"
    return False

def main():
    grid = [[Cell(row, col, Width) for col in range(Columns)] for row in range(Rows)]
    start = None
    goal = None
    running = True
    current_heuristic = "diagonal"
    elapsed = 0
    font = pygame.font.SysFont("Arial", 20)
    while running:
        pygame.draw.rect(Win, WHITE, (0, 0, Columns * Width, Header))
        pygame.draw.line(Win, BLACK, (0, Header), (Columns * Width, Header), 3)
        heuristic_text = font.render(f"Heuristic: {current_heuristic} (H to switch)", True, BLACK)
        Win.blit(heuristic_text, (10, 10))
        time_text = font.render(f"Time: {elapsed:.2f}s", True, BLACK)
        Win.blit(time_text, (500, 10))
        for row in grid:
            for cell in row:
                cell.draw(Win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[1] < Header:  # ← ignore header clicks
                    pass
                else:
                    pos = pygame.mouse.get_pos()
                    row = (pos[1]- Header) // Width
                    col = pos[0] // Width
                    cell = grid[row][col]
                    if start is None:
                        start = cell
                        start.state = "start"
                    elif goal is None:
                        if cell != start: # the user cannot select the same node as the start and goal
                            goal = cell
                            goal.state = "goal"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if start and goal:
                        if current_heuristic == "diagonal":
                            heuristic_fn = heuristic_diagonal
                        elif current_heuristic == "manhattan":
                            heuristic_fn = heuristic_manhattan
                        else:
                            heuristic_fn = heuristic_euclidean
                        start_time = time.time()
                        result = astar(grid, start, goal, Rows, Columns, Win, heuristic_fn, font, current_heuristic, start_time)
                        elapsed = time.time() - start_time
                        if not result:
                            big_font = pygame.font.SysFont("Arial", 50)
                            text = big_font.render("No Path Found!", True, BLACK)
                            Win.blit(text, (Width*3, Rows*Width//2))
                            pygame.display.update()
                            pygame.time.delay(1000)
                            grid = [[Cell(row, col, Width) for col in range(Columns)] for row in range(Rows)]
                            start = None
                            goal = None
                if event.key == pygame.K_r:
                    grid = [[Cell(row, col, Width) for col in range(Columns)] for row in range(Rows)]
                    start = None
                    goal = None
                if event.key == pygame.K_h:
                    if current_heuristic == "diagonal":
                        current_heuristic = "manhattan"
                    elif current_heuristic == "manhattan":
                        current_heuristic = "euclidean"
                    else:
                        current_heuristic = "diagonal"

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if pos[1] >= Header:
                row = (pos[1]- Header) // Width
                col = pos[0] // Width
                cell = grid[row][col]
                if cell != start and cell != goal:
                    cell.state = "wall"

        pygame.display.update()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
