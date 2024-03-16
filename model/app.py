import pygame
from model import player, maze, ai

pygame.init()
class App:
    def __init__(self,size):
        cell_size = 15
        self.width = (2 * size + 1) * cell_size
        self.size = size
        self.window = pygame.display.set_mode((self.width + 250, self.width))
        self.player = player.Player(cell_size)
        self.maze = maze.Maze(size)
        self.maze_arr = self.maze.maze
        self.span = self.maze.span
        self.image_player = pygame.image.load("D:\\projects\\MazeGame\\player-right.gif")
        self.image_block = pygame.image.load("D:\\projects\\MazeGame\\jungle.gif")
        self.image_block = pygame.transform.scale(self.image_block, (cell_size, cell_size))
        self.image_player = pygame.transform.scale(self.image_player, (cell_size, cell_size))

    def render(self):
        self.window.fill((0, 0, 0))
        self.draw_maze()
        self.window.blit(self.image_player, (self.player.x, self.player.y))

    def draw_button(self,  surface, color, x, y, width, height, str):
        f = pygame.font.SysFont(None, 27)
        text = f.render(str, True, (255, 255, 255))
        pygame.draw.rect(surface, color,(x, y, width, height), 0, 8)
        shape = text.get_rect()
        surface.blit(text, (x + width/2 - shape.width/2, y + height/2 - shape.height/2))

    def draw_toolbar(self, pos_x, pos_y):
        surface = pygame.surface.Surface((200, self.width))
        surface.fill((0,0,0))

        self.draw_button(surface, (255, 172, 108), 60, 100, 80,40, "HOME")

        self.draw_button(surface, (255, 172, 108), 60, 170, 80, 40, "PAUSE")

        self.draw_button(surface, (255, 172, 108), 60, 240, 80,40, "RESTART")
        shape_width = self.width

        if shape_width + 60 <= pos_x <= shape_width + 140:
            if 100 <= pos_y <= 140:
                self.draw_button(surface, (224, 224, 224), 60, 100, 80, 40, "HOME")
            elif 170 <= pos_y <= 210:
                self.draw_button(surface, (224, 224, 224), 60, 170, 80, 40, "PAUSE")
            elif 240 <= pos_y <= 280:
                self.draw_button(surface, (224, 224, 224), 60, 240, 80, 40, "RESTART")

        self.window.blit(surface,(self.width, 0))

    def draw_menu(self, pos_x, pos_y):
        surface = pygame.surface.Surface((100, 200))
        surface.fill((0, 0, 0))

        self.draw_button(surface, (255, 172, 108), 0, 0, 100,60, "AI")
        self.draw_button(surface, (255, 172, 108), 0, 100, 100,60, "PLAYER")
        shape = self.window.get_rect()
        if shape.width/2 - 50 <= pos_x <= shape.width/2 + 50:
            if shape.height/2 - 100 <= pos_y <= shape.height/2 - 40:
                self.draw_button(surface, (224, 224, 224), 0, 0, 100, 60, "AI")
            elif shape.height/2 <= pos_y <= shape.height/2 + 60:
                self.draw_button(surface, (224, 224, 224),0, 100, 100, 60, "PLAYER")

        self.window.blit(surface, (shape.width/2 - 50, shape.height/2 - 100))

    def draw_maze(self):
        shape = self.image_block.get_rect()
        for i in range(self.size * 2 + 1):
            for j in range(self.size * 2 + 1):
                if self.maze_arr[i][j] == 1:
                    self.window.blit(self.image_block, (j * shape.width, i * shape.height))

    def can_move(self, pos1, pos2):
        c = pos2[0] - pos1[0]
        if c == 0:
            if self.maze_arr[pos1[0] * 2 + 1][2 * pos1[1] + 2] == 0 or self.maze_arr[2 * pos1[0] + 1][2 * pos1[1]] == 0:
                return True
        if c == 1:
            if self.maze_arr[2 * pos1[0] + 2][2 * pos1[1] + 1] == 0 or self.maze_arr[2 * pos1[0]][2 * pos1[1] + 1] == 0:
                return True
        return False

    def get_path(self, solve1, solve2):
        if [solve1, solve2] in self.span or [solve2, solve1] in self.span:
            if solve2 - solve1 == 1:
                return "R"
            if solve2 - solve1 == -1:
                return "L"
            if solve2 - solve1 == -self.size:
                return "U"
            if solve2 - solve1 == self.size:
                return "D"
        return None

    def get_path_ai(self):
        path = []
        a = ai.AI(self.span, self.size, 0, self.size * self.size - 1)
        solve = a.solve()
        i = 0
        while i < len(solve) - 1:
            if self.get_path(solve[i], solve[i + 1]) is not None:
                path.append(self.get_path(solve[i], solve[i + 1]))
            i += 1
        return path
    def restart(self):
        self.maze = maze.Maze(self.size)
        self.span = self.maze.span
        self.maze_arr = self.maze.maze
        self.player.x = 15
        self.player.y = 15

    def draw_path(self, i):
        path = self.get_path_ai()
        j = 0
        pos = [15, 15]
        while j <= i:
            if path[j] == "R":
                pygame.draw.rect(self.window, (0, 255, 0), (pos[0], pos[1], 30, 15))
                pos[0] += 30
            elif path[j] == "L":
                pygame.draw.rect(self.window, (0, 255, 0), (pos[0] - 15, pos[1], 30, 15))
                pos[0] -= 30
            elif path[j] == "D":
                pygame.draw.rect(self.window, (0, 255, 0), (pos[0], pos[1], 15, 30))
                pos[1] += 30
            elif path[j] == "U":
                pygame.draw.rect(self.window, (0, 255, 0), (pos[0], pos[1] - 15, 15, 30))
                pos[1] -= 30
            j += 1

    def draw_ai(self):
        path = self.get_path_ai()
        run = True
        i = 0
        x = 0
        speed = 1
        con = True
        run_home = restart = False

        while run:
            self.window.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if self.width + 60 <= x <= self.width + 140:
                        if 100 <= y <= 140:
                            run_home = True
                            run = False
                        elif 170 <= y <= 210:
                            if con:
                                con = False
                            else:
                                con = True
                                i -= 1
                        elif 240 <= y <= 280:
                            restart = True
                            run = False
            while x <= 30 and i < len(path) and con:
                x += speed
                pos_x, pos_y = pygame.mouse.get_pos()
                self.draw_maze()
                self.draw_toolbar(pos_x, pos_y)
                self.draw_path(i - 1)
                pygame.display.flip()

            x = 0
            pos_x, pos_y = pygame.mouse.get_pos()
            self.draw_maze()
            self.draw_toolbar(pos_x, pos_y)

            if i < len(path) and con:
                i += 1
            self.draw_path(i - 1)
            pygame.display.flip()
        if restart:
            self.restart()
            self.draw_ai()
        elif run_home:
            self.restart()
            self.draw_play()

    def draw_player(self):

        for a in self.maze_arr:
            print(a)

        running = True
        run_home = False
        restart = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.player.move_on_key_down(event.key, self.maze_arr)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if self.width + 60 <= x <= self.width + 140:
                        if 100 <= y <= 140:
                            run_home = True
                            running = False
                        elif 170 <= y <= 210:
                            pass
                        elif 240 <= y <= 280:
                            restart = True
                            running = False
            pos_x, pos_y = pygame.mouse.get_pos()
            self.render()
            self.draw_toolbar(pos_x, pos_y)
            pygame.display.flip()

        if restart:
            self.restart()
            self.draw_player()
        elif run_home:
            self.restart()
            self.draw_play()

    def draw_play(self):
        menu = True
        player = False
        a = False
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos_x, pos_y = pygame.mouse.get_pos()
                    shape = self.window.get_rect()
                    if shape.width / 2 - 50 <= pos_x <= shape.width / 2 + 50:
                        if shape.height / 2 - 100 <= pos_y <= shape.height / 2 - 40:
                            a = True
                            menu = False
                            player = False
                        elif shape.height / 2 <= pos_y <= shape.height / 2 + 60:
                            player = True
                            a = False
                            menu = False
            pos_x, pos_y = pygame.mouse.get_pos()
            self.draw_menu(pos_x, pos_y)
            pygame.display.flip()
        if a:
            self.draw_ai()
        elif player:
            self.draw_player()