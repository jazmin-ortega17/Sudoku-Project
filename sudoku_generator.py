import math,random
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


"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""

class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''
    def __init__(self, row_length, removed_cells):
        pass

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''
    def get_board(self):
        pass

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''
    def print_board(self):
        pass

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''
    def valid_in_row(self, row, num):
        pass

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''
    def valid_in_col(self, col, num):
        pass

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''
    def valid_in_box(self, row_start, col_start, num):
        pass
    
    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''
    def is_valid(self, row, col, num):
        pass

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''
    def fill_box(self, row_start, col_start):
        pass
    
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''
    def fill_diagonal(self):
        pass

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    def remove_cells(self):
        pass

'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
