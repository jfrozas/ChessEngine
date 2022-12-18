import pygame as p

from const import *
from mover import *


class Board:
    def __init__(self):
        self.boardcoord = [
            ["bR", "bN", "bB", "bQ", "bK","bB","bN","bR"],
            ["bp", "bp", "bp", "bp", "bp","bp","bp","bp"],
            ["__", "__", "__", "__", "__","__","__","__"],
            ["__", "__", "__", "__", "__","__","__","__"],
            ["__", "__", "__", "__", "__","__","__","__"],
            ["__", "__", "__", "__", "__","__","__","__"],
            ["wp", "wp", "wp", "wp", "wp","wp","wp","wp"],
            ["wR", "wN", "wB", "wQ", "wK","wB","wN","wR"]
        ]
        self.whiteToMove = True
        self.movelog = []

    def show_board(self, surface):
        colors = [(255,250,250), (43,45,47)]
        for row in range(ROWS):
            for column in range(COLUMNS):
                color = colors[((row+column)% 2)]

                rect = (row * SQUARESIZE, column * SQUARESIZE, SQUARESIZE, SQUARESIZE)

                p.draw.rect(surface, color, rect)

    def makeMove(self, move):

        self.boardcoord[move.startRow][move.startColumn] = "__"
        self.boardcoord[move.endRow][move.endColumn] = move.pieceToMove
        self.movelog.append(move)
        self.whiteToMove = not self.whiteToMove



    def getPiece(self, square):
        self.row = square[0]
        self.column = square[1] 

        return self.boardcoord[self.row][self.column][0] + self.boardcoord[self.row][self.column][1]


    def getPossibleMoves(self, square):
        
        moves = []

        self.row = square[0]
        self.column = square[1]
        piece = self.boardcoord[self.row][self.column][0] + self.boardcoord[self.row][self.column][1]


        if piece == "wp" or piece == "bp":
            self.getPawnMoves(self.row, self.column, moves)

        return moves
        #print(self.boardcoord[self.row][self.column][0] + self.boardcoord[self.row][self.column][1]) 



    def getPawnMoves(self, row, column, moves):
        if self.whiteToMove:  #White
            if self.boardcoord[row-1][column] == "__":
                moves.append( mover( (row, column), (row-1, column), self.boardcoord) )
                if row == 6 and self.boardcoord[row-2][column] == "__":
                    moves.append( mover( (row, column), (row-2, column), self.boardcoord) )
        else:
            if self.boardcoord[row+1][column] == "__":
                moves.append( mover( (row, column), (row+1, column), self.boardcoord) )
                if row == 1 and self.boardcoord[row+2][column] == "__":
                    moves.append( mover( (row, column), (row+2, column), self.boardcoord) )

    
    


        
        




