import pygame
import time
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

