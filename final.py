import pygame
import sys

# Constants
WIDTH = 540
HEIGHT = 540
LINE_WIDTH = 6
LINE_WIDTH_INNER = 2
BOARD_SIZE = 9
SQUARE_SIZE = WIDTH // BOARD_SIZE
BG_COLOR = (12, 10, 50)
LINE_COLOR = (44, 40, 197)
TEXT_COLOR = (255, 255, 255)
CHIP_FONT = 100
GAME_OVER_FONT = 40

# Global variables
selected_cell = None
game_over = False

def draw_numbers():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            value = board[row * BOARD_SIZE + col]
            if value != "-":
                num_surf = main_font.render(str(value), True, TEXT_COLOR)
                x = col * SQUARE_SIZE + SQUARE_SIZE // 2
                y = row * SQUARE_SIZE + SQUARE_SIZE // 2
                num_rect = num_surf.get_rect(center=(x, y))
                screen.blit(num_surf, num_rect)

def draw_game_over():
    screen.fill(BG_COLOR)
    end_text = "You won the game"
    end_surf = game_over_font.render(end_text, 0, LINE_COLOR)
    end_rect = end_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(end_surf, end_rect)

    restart_text = "Press r to play the game again..."
    restart_surf = game_over_font.render(restart_text, 0, LINE_COLOR)
    restart_rect = restart_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(restart_surf, restart_rect)

class Cell:
    def __init__(self, value, row, col, font, screen):
        self.value = value
        self.row = row
        self.col = col
        self.font = font
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    def draw(self):
        if self.value != "-":
            x = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
            y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2
            num_surf = self.font.render(str(self.value), True, TEXT_COLOR)
            num_rect = num_surf.get_rect(center=(x, y))
            self.screen.blit(num_surf, num_rect)

class Board:
    def __init__(self, width, height, screen, difficulty=30):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.size = BOARD_SIZE
        self.board = self.initialize_board()
        self.update_cells()

    def draw(self):
        for i in range(1, BOARD_SIZE):
            if i % 3 == 0:
                pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
            else:
                pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH_INNER)

        for i in range(1, BOARD_SIZE):
            if i % 3 == 0:
                pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
            else:
                pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH_INNER)

        for i in range(self.size):
            for j in range(self.size):
                self.cells[i][j].draw()

    def initialize_board(self):
        return ["-" for _ in range(BOARD_SIZE * BOARD_SIZE)]  # Flat list for the board

    def available_square(self, row, col):
        return self.board[row * BOARD_SIZE + col] == "-"

    def find_empty(self):
        for i in range(self.size):  # size = 9 for standard Sudoku
            for j in range(self.size):
                if self.board[i][j] == "-":
                    return (i, j)
        return None

    def mark_square(self, row, col, value):
        self.board[row * BOARD_SIZE + col] = value
        self.update_cells()

    def is_full(self):
        for row in self.board:
            if "-" in row:
                return False
        return True

    def update_cells(self):
        self.cells = [
            [Cell(self.board[i * BOARD_SIZE + j], i, j, main_font, self.screen)
             for j in range(self.size)] for i in range(self.size)
        ]

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    screen.fill(BG_COLOR)

    main_font = pygame.font.Font(None, CHIP_FONT)
    game_over_font = pygame.font.Font(None, GAME_OVER_FONT)

    board_obj = Board(WIDTH, HEIGHT, screen)
    board = board_obj.board
    board_obj.draw()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                row = y // SQUARE_SIZE
                col = x // SQUARE_SIZE
                selected_cell = (row, col)

            if event.type == pygame.KEYDOWN:
                if selected_cell and pygame.K_1 <= event.key <= pygame.K_9:
                    num_pressed = event.key - pygame.K_1 + 1
                    row, col = selected_cell
                    if board_obj.available_square(row, col):
                        board_obj.mark_square(row, col, num_pressed)
                        draw_numbers()

                if event.key == pygame.K_r and game_over:
                    screen.fill(BG_COLOR)
                    board_obj = Board(WIDTH, HEIGHT, screen)
                    board = board_obj.board
                    game_over = False

        if game_over:
            pygame.display.update()
            pygame.time.delay(1000)
            draw_game_over()

        pygame.display.update()
