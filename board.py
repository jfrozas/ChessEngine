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
        
        self.bishopList = [(1,1), (-1,-1), (1,-1), (-1,1)]
        self.rookList = [(1,0), (-1,0), (0,-1), (0,1)]
        self.KnightList = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2),]
        self.KingList = [(1,1),(-1,-1),(1,-1),(-1,1),(1,0),(-1,0),(0,-1),(0,1)]
        
        self.WhiteKingLoc = (7,4)
        self.BlackKingLoc = (0,4)
        
    def show_board(self, surface):
        colors = [(255,250,250), (43,45,47)]
        for row in range(ROWS):
            for column in range(COLUMNS):
                color = colors[((row+column)% 2)]

                rect = (row * SQUARESIZE, column * SQUARESIZE, SQUARESIZE, SQUARESIZE)

                p.draw.rect(surface, color, rect)

    def makeMove(self, move, turn):

        self.boardcoord[move.startRow][move.startColumn] = "__"
        self.boardcoord[move.endRow][move.endColumn] = move.pieceToMove

        move.turn = turn
        
        if move.pieceToMove == "wK":

            self.WhiteKingLoc = (move.endRow, move.endColumn)

        
        if move.pieceToMove == "bK":
            self.BlackKingLoc = (move.endRow, move.endColumn)

            
        self.movelog.append(move)
        self.whiteToMove = not self.whiteToMove

    def undoMove(self, turn):
        
        # ! Acceder al movelog, sacar el movimiento, poner las casillas de ese move como end y beggining, movemos la pieza, cambiamos turno
        move = self.movelog[-1]
        
        self.boardcoord[move.startRow][move.startColumn] = move.pieceToMove
        self.boardcoord[move.endRow][move.endColumn] = "__"
        print("a")
        print(move)
        
        if self.whiteToMove == True:
            move.turn = turn -1
        else:
            move.turn = turn
        
        if move.pieceToMove == "wK":

            self.WhiteKingLoc = (move.startRow, move.startColumn)

        
        if move.pieceToMove == "bK":
            self.BlackKingLoc = (move.startRow, move.startColumn)       
        
        self.movelog.pop()
        self.whiteToMove = not self.whiteToMove
        
    def getPiece(self, square):
        self.row = square[0]
        self.column = square[1] 

        return self.boardcoord[self.row][self.column][0] + self.boardcoord[self.row][self.column][1]

    def getAllOponentsMoves(self):
        
        moves = []
        
        if self.whiteToMove == True:
            letter = "b"
        else: 
            letter = "w"
            
        for row in range(len(self.boardcoord)):
            for column in range(len(self.boardcoord[row])):
                
                piece = self.boardcoord[row][column]  
                #print("Pieza = " + piece + " Letra: " + letter)
                
                if piece == letter + "p":
                    self.getPawnMoves(row, column, moves, not self.whiteToMove)

                elif piece == letter + "R":
                    self.getRookMoves(row, column, moves, not self.whiteToMove)

                elif piece == letter + "B":
                    self.getBishopMoves(row, column, moves, not self.whiteToMove)
                
                elif piece == letter + "N":
                    self.getKnightMoves(row, column, moves, self.KnightList, not self.whiteToMove)
                    
                elif piece == letter + "Q":
                    self.getQueenMoves(row, column, moves, not self.whiteToMove)
                    
                elif piece == letter + "K":
                    self.getKingMoves(row, column, moves, self.KingList, not self.whiteToMove)   
                    
        return moves 
                  
    def getPossibleMoves(self, square):
        
        moves = []

        self.row = square[0]
        self.column = square[1]
        piece = self.boardcoord[self.row][self.column][0] + self.boardcoord[self.row][self.column][1]

        if self.whiteToMove == True:
            letter = "w"
        else: 
            letter = "b"
            
        if piece == letter + "p":
            self.getPawnMoves(self.row, self.column, moves, self.whiteToMove)

        elif piece == letter + "R":
            self.getRookMoves(self.row, self.column, moves, self.whiteToMove)

        elif piece == letter + "B":
            self.getBishopMoves(self.row, self.column, moves, self.whiteToMove)
        
        elif piece == letter + "N":
            self.getKnightMoves(self.row, self.column, moves, self.KnightList, self.whiteToMove)
            
        elif piece == letter + "Q":
            self.getQueenMoves(self.row, self.column, moves, self.whiteToMove)
            
        elif piece == letter + "K":
            self.getKingMoves(self.row, self.column, moves, self.KingList, self.whiteToMove)      
                  
        return moves


    def getPawnMoves(self, row, column, moves, turn):

        if turn:                                                                         #White
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
    
    
    def Iterator(self, row, column, moves, list, turn):
        
        if turn == True:
            enemycolor = "b"
        else:
            enemycolor = "w"
            
            
        for direction in list:
            
            a = direction[0]
            b = direction[1]

            
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
                    
                    
    def Iterator2(self, row, column, moves, list, turn):
        
        if turn == True:
            enemycolor = "b"
        else:
            enemycolor = "w"
            
            
        for direction in list:
            
            a = direction[0]
            b = direction[1]

            endRow = row + a 
            endCol = column + b 

            if 0 <= endRow < 8 and 0 <= endCol < 8:
                piece = self.boardcoord[endRow][endCol]

                if piece == "__":
                    moves.append( mover( (row, column), (endRow, endCol), self.boardcoord) )

                elif piece[0] == enemycolor:
                    moves.append( mover( (row, column), (endRow, endCol), self.boardcoord) )
                            
    
    def getRookMoves(self, row, column, moves, turn):
        
        self.Iterator(row, column, moves, self.rookList, turn)
        
           
    def getBishopMoves(self, row, column, moves, turn):
        
        self.Iterator(row, column, moves, self.bishopList, turn)
    
    
    def getQueenMoves(self, row, column, moves, turn):
        self.getBishopMoves(row, column, moves, turn)
        self.getRookMoves(row, column, moves, turn)
        
        
    def getKnightMoves(self, row, column, moves, list, turn):
       self.Iterator2(row, column, moves, list, turn)
       
               
    def getKingMoves(self, row, column, moves, list, turn):
        
        self.Iterator2(row, column, moves, list, turn)
    

        

