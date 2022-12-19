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

        if piece == "wR" or piece == "bR":
            self.getRookMoves(self.row, self.column, moves)

        if piece == "wB" or piece == "bB":
            self.getBishopMoves(self.row, self.column, moves)
        
        if piece == "wN" or piece == "bN":
            self.getKnightMoves(self.row, self.column, moves)
            
        if piece == "wQ" or piece == "bQ":
            self.getQueenMoves(self.row, self.column, moves)
            
        if piece == "wK" or piece == "bK":
            self.getKingMoves(self.row, self.column, moves)      
                  
        return moves
        #print(self.boardcoord[self.row][self.column][0] + self.boardcoord[self.row][self.column][1]) 



    def getPawnMoves(self, row, column, moves):

        if self.whiteToMove:                                                                         #White
            if self.boardcoord[row-1][column] == "__":
                moves.append( mover( (row, column), (row-1, column), self.boardcoord) )             #Move 1
                if row == 6 and self.boardcoord[row-2][column] == "__":
                    moves.append( mover( (row, column), (row-2, column), self.boardcoord) )          #Move 2 

            if column-1 >= 0:                                                                       #Captures  
                if self.boardcoord[row-1][column-1][0] == "b":          
                    moves.append( mover( (row, column), (row-1, column-1), self.boardcoord) )       #Captures left
            if column+1 <= 7:
                if self.boardcoord[row-1][column+1][0] == "b":                              
                    moves.append( mover( (row, column), (row-1, column+1), self.boardcoord) )       #Captures right

        else:
            if self.boardcoord[row+1][column] == "__":
                moves.append( mover( (row, column), (row+1, column), self.boardcoord) )
                if row == 1 and self.boardcoord[row+2][column] == "__":
                    moves.append( mover( (row, column), (row+2, column), self.boardcoord) )

            if column-1 >= 0:                                                                       #Captures  
                if self.boardcoord[row+1][column-1][0] == "w":          
                    moves.append( mover( (row, column), (row+1, column-1), self.boardcoord) )       #Captures left
            if column+1 <= 7:
                if self.boardcoord[row+1][column+1][0] == "w":                              
                    moves.append( mover( (row, column), (row+1, column+1), self.boardcoord) )       #Captures right
    

    def getRookMoves(self, row, column, moves):
        
        if self.whiteToMove == True:
            enemycolor = "b"
        else:
            enemycolor = "w"

        #Up
        a = -1
        b = 0

        for i in range(1,8):

            endRow = row + a * i
            endCol = column + b * i

            if 0 <= endRow < 8 and 0 <= endCol < 8:
                piece = self.boardcoord[endRow][endCol]

                if piece == "__":
                    moves.append( mover( (row, column), (endRow, endCol), self.boardcoord) )

                elif piece[0] == enemycolor:
                    moves.append( mover( (row, column), (endRow, endCol), self.boardcoord) )
                    break

                else:
                    break

            else:
                break
        #Down
        a = 1
        b = 0

        for i in range(1,8):
            
            endRow = row + a * i
            endCol = column + b * i

            if 0 <= endRow < 8 and 0 <= endCol < 8:
                piece = self.boardcoord[endRow][endCol]

                if piece == "__":
                    moves.append( mover( (row, column), (endRow, endCol), self.boardcoord) )

                elif piece[0] == enemycolor:
                    moves.append( mover( (row, column), (endRow, endCol), self.boardcoord) )
                    break

                else:
                    break

            else:
                break
        #Left
        a = 0
        b = -1

        for i in range(1,8):
            
            endRow = row + a * i
            endCol = column + b * i

            if 0 <= endRow < 8 and 0 <= endCol < 8:
                piece = self.boardcoord[endRow][endCol]

                if piece == "__":
                    moves.append( mover( (row, column), (endRow, endCol), self.boardcoord) )

                elif piece[0] == enemycolor:
                    moves.append( mover( (row, column), (endRow, endCol), self.boardcoord) )
                    break

                else:
                    break

            else:
                break
        #Right
        a = 0
        b = 1

        for i in range(1,8):
            
            endRow = row + a * i
            endCol = column + b * i

            if 0 <= endRow < 8 and 0 <= endCol < 8:
                piece = self.boardcoord[endRow][endCol]

                if piece == "__":
                    moves.append( mover( (row, column), (endRow, endCol), self.boardcoord) )

                elif piece[0] == enemycolor:
                    moves.append( mover( (row, column), (endRow, endCol), self.boardcoord) )
                    break

                else:
                    break

            else:
                break
        
        
    def getBishopMoves(self, row, column, moves):
        if self.whiteToMove == True:
            enemycolor = "b"
        else:
            enemycolor = "w"

        
        a = 1
        b = 1

        for i in range(1,8):

            endRow = row + a * i
            endCol = column + b * i

            if 0 <= endRow < 8 and 0 <= endCol < 8:
                piece = self.boardcoord[endRow][endCol]

                if piece == "__":
                    moves.append( mover( (row, column), (endRow, endCol), self.boardcoord) )

                elif piece[0] == enemycolor:
                    moves.append( mover( (row, column), (endRow, endCol), self.boardcoord) )
                    break

                else:
                    break

            else:
                break
        #Down
        a = -1
        b = -1

        for i in range(1,8):
            
            endRow = row + a * i
            endCol = column + b * i

            if 0 <= endRow < 8 and 0 <= endCol < 8:
                piece = self.boardcoord[endRow][endCol]

                if piece == "__":
                    moves.append( mover( (row, column), (endRow, endCol), self.boardcoord) )

                elif piece[0] == enemycolor:
                    moves.append( mover( (row, column), (endRow, endCol), self.boardcoord) )
                    break

                else:
                    break

            else:
                break
        #Left
        a = 1
        b = -1

        for i in range(1,8):
            
            endRow = row + a * i
            endCol = column + b * i

            if 0 <= endRow < 8 and 0 <= endCol < 8:
                piece = self.boardcoord[endRow][endCol]

                if piece == "__":
                    moves.append( mover( (row, column), (endRow, endCol), self.boardcoord) )

                elif piece[0] == enemycolor:
                    moves.append( mover( (row, column), (endRow, endCol), self.boardcoord) )
                    break

                else:
                    break

            else:
                break
        #Right
        a = -1
        b = 1

        for i in range(1,8):
            
            endRow = row + a * i
            endCol = column + b * i

            if 0 <= endRow < 8 and 0 <= endCol < 8:
                piece = self.boardcoord[endRow][endCol]

                if piece == "__":
                    moves.append( mover( (row, column), (endRow, endCol), self.boardcoord) )

                elif piece[0] == enemycolor:
                    moves.append( mover( (row, column), (endRow, endCol), self.boardcoord) )
                    break

                else:
                    break

            else:
                break
    
    
    def getQueenMoves(self, row, column, moves):
        self.getBishopMoves(row, column, moves)
        self.getRookMoves(row, column, moves)
        
        
    def getKnightMoves(self, row, column, moves):
        #Two forward, one left, one right, two backwards, one left one right, two left, one up one down, two right, one up one down
        pass    
    
    def getKingMoves(self, row, column, moves):
        #One in each possible direction
        pass
    

        

