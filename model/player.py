import pygame


class Player:
    def __init__(self, cell_size):
        self.x = cell_size
        self.y = cell_size
        self.cell_size = cell_size

    def move_on_key_down(self, key, maze_array):
        row = int(self.y / self.cell_size)
        col = int(self.x / self.cell_size)
        if key == pygame.K_RIGHT:
            if col + 1 < len(maze_array) and 0 == maze_array[row][col + 1]:
                col += 1
        elif key == pygame.K_LEFT:
            if col - 1 >= 0 == maze_array[row][col - 1]:
                col -= 1
        elif key == pygame.K_UP:
            if row - 1 >= 0 == maze_array[row - 1][col]:
                row -= 1
        elif key == pygame.K_DOWN:
            if row + 1 < len(maze_array) and 0 == maze_array[row + 1][col]:
                row += 1
        self.x = col * self.cell_size
        self.y = row * self.cell_size

    def move_on_ai(self, dir, speed):
        if dir == "R":
            self.x += speed
        elif dir == "L":
            self.x -= speed
        elif dir == "U":
            self.y -= speed
        elif dir == "D":
            self.y += speed
        return False



