import pygame as pg
import time as T
import sys

board = [[' ' for i in range(8)] for i in range(8)]


#class that shows what team a piece is on, and whether it can be killed by a selected piece
class Piece:
    def __init__(self, team, type, image, killable=False):
        self.team = team
        self.type = type
        self.killable = killable
        self.image = image

bp = Piece('b', 'p', 'b_pawn.png')# this is black pawn, the parameters indicate: the team, the type, and the colore
wp = Piece('w', 'p', 'w_pawn.png')# white pawn
bk = Piece('b', 'k', 'b_king.png')# Black king
wk = Piece('w', 'k', 'w_king.png')# white king
br = Piece('b', 'r', 'b_rook.png')# black rook
wr = Piece('w', 'r', 'w_rook.png')# White rook
bb = Piece('b', 'b', 'b_bishop.png')# black bishop
wb = Piece('w', 'b', 'w_bishop.png')# white bishop
bq = Piece('b', 'q', 'b_queen.png')# black queen
wq = Piece('w', 'q', 'q_queen.png')# white queen
bkn = Piece('b', 'kn', 'b_knight.png')# b_knight
wkn = Piece('w', 'kn', 'w_knight.png')# w_knight

str_order = {(0, 0): pg.image.load(br.image),
             (1, 0): pg.image.load(bkn.image),
             (2, 0): pg.image.load(bb.image),
             (3, 0): pg.image.load(bk.image),
             (4, 0): pg.image.load(bq.image),
             (5, 0): pg.image.load(bb.image),
             (6, 0): pg.image.load(bkn.image),
             (7, 0): pg.image.load(br.image),
             (0, 1): pg.image.load(bp.image),
             (1, 1): pg.image.load(bp.image),
             (2, 1): pg.image.load(bp.image),
             (3, 1): pg.image.load(bp.image),
             (4, 1): pg.image.load(bp.image),
             (5, 1): pg.image.load(bp.image),
             (6, 1): pg.image.load(bp.image),
             (7, 1): pg.image.load(bp.image),



             (0, 2): None, (1, 2): None, (2, 2): None, (3, 2): None,
             (4, 2): None, (5, 2): None, (6, 2): None, (7, 2): None,
             (0, 3): None, (1, 3): None, (2, 3): None, (3, 3): None,
             (4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None,
             (0, 4): None, (1, 4): None, (2, 4): None, (3, 4): None,
             (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None,
             (0, 5): None, (1, 5): None, (2, 5): None, (3, 5): None,
             (4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None,



             (0, 6): pg.image.load(wp.image),
             (1, 6): pg.image.load(wp.image),
             (2, 6): pg.image.load(wp.image),
             (3, 6): pg.image.load(wp.image),
             (4, 6): pg.image.load(wp.image),
             (5, 6): pg.image.load(wp.image),
             (6, 6): pg.image.load(wp.image),
             (7, 6): pg.image.load(wp.image),
             (0, 7): pg.image.load(wr.image),
             (1, 7): pg.image.load(wkn.image),
             (2, 7): pg.image.load(wb.image),
             (3, 7): pg.image.load(wk.image),
             (4, 7): pg.image.load(wq.image),
             (5, 7): pg.image.load(wb.image),
             (6, 7): pg.image.load(wkn.image),
             (7, 7): pg.image.load(wr.image)}# an extra coma was placed here what is it?


def create_board(board):
    board[0] = [Piece('b', 'r', 'b_rook.png'), Piece('b', 'kn', 'b_knight.png'),
                Piece('b', 'b', 'b_bishop.png'),\
                Piece('b', 'q', 'b_queen.png'), Piece('b', 'k', 'b_king'),
                Piece('b', 'b', 'b_bishop.png').\
                Piece('b', 'kn', 'b_knight.png'), Piece('b', 'r', 'b_rook.png')]
    board[7] = [Piece('w', 'r', 'w_rook.png'), Piece('w', 'kn', 'w_knight.png'),
                Piece('w', 'b', 'w_bishop.png'), \
                Piece('w', 'q', 'w_queen.png'), Piece('w', 'k', 'w_king'),
                Piece('w', 'b', 'w_bishop.png'), \
                Piece('w', 'kn', 'w_knight.png'), Piece('w', 'r', 'w_rook.png')]
    for i in range(8):
        board[1][i] = Piece('b', 'p', 'b_pawn.png')
        board[6][i] = Piece('w', 'p', 'w_pawn.png')

    return board

#checks if the move is within the board
def on_board(position):
    if position[0] > -1 and position[1] > -1 and position[0] < 8 and position[1] < 8:
        return True
    return False

# return a string that places the rows and columns of the board in a readable manner
def convert_to_readable(board):
    output = ''
    for i in board:
        for j in i:
            try:
                output += j.team + j.type + ', '
            except:
                output += j + ', '
        output += '\n'
    return output

def deselect():
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 'x ':
                board[row][column] = '  '
            else:
                try:
                    board[row][column].killable = False
                except:
                    pass
    return convert_to_readable(board)

