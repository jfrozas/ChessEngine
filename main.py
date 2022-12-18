import pygame as p
import sys
import numpy as np

from const import *
from board import *
from mover import *


IMAGES = {}
MAX_FPS = 15


class Main():
    def __init__(self):
        p.init()
        self.screen = p.display.set_mode( (WIDTH, HEIGHT) )
        self.board = Board()
        loadPieces()


    def mainLoop(self):
        print(np.matrix(self.board.boardcoord))

        print("White to Move")

        sqSelected = ()   #Coordinates of one square selected (x,y)
        auxMover = []      #Store player clicks, max = 2  [ (x,y) , (x,y) ]
        validMoves = []
        clock = p.time.Clock()

        while True:
            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
                elif event.type == p.MOUSEBUTTONDOWN:

                    loc = p.mouse.get_pos()  #(x,y)
                    column = loc[0]//SQUARESIZE
                    row = loc[1]//SQUARESIZE
                
                    if sqSelected == (row,column):
                        sqSelected = ()
                        auxMover = []
                    else:
                        sqSelected = (row, column)
                        auxMover.append(sqSelected)

                    if len(auxMover) == 1:

                        if self.board.getPiece(sqSelected) == "__":   #Deseleccion si clicas en casilla en blanco
                            sqSelected = ()
                            auxMover = []

                        if self.board.getPiece(sqSelected)[0] == "w" and  self.board.whiteToMove == False:
                            sqSelected = ()
                            auxMover = []

                        if self.board.getPiece(sqSelected)[0] == "b" and  self.board.whiteToMove == True:
                            sqSelected = ()
                            auxMover = []

                    if len(auxMover) == 1:
                        print("Moving: " + self.board.getPiece(sqSelected))
                        validMoves = self.board.getPossibleMoves(sqSelected)     #Consigue todos los posibles movimientos

                        for move in validMoves:
                            print("Possible moves dsps: " + move.MoveNotation())

                    if len(auxMover) == 2:   #Two valid clicks -> move
                        move = mover(auxMover[0], auxMover[1], self.board.boardcoord)

                        if move in validMoves:
                            self.board.makeMove(move)
                        

                        if move.blankselected != True:
                            print(move.MoveNotation())


                        sqSelected = ()
                        auxMover = []

                        print(np.matrix(self.board.boardcoord))

                        if self.board.whiteToMove == True:
                            print("White to move")
                        else:
                            print("Black to move")

            self.board.show_board(self.screen) 
            highlighter(self.screen, sqSelected, validMoves)
            drawPieces(self.screen, self.board)

            clock.tick(MAX_FPS)
            p.display.flip()


def loadPieces():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.image.load("assets/images/imgs-80px/" + piece + ".png")


def drawPieces(screen, board): 
    for row in range(ROWS):
        for column in range(COLUMNS):
            piece = board.boardcoord[row][column]
            if piece != "__":
                im_center = column * SQUARESIZE + SQUARESIZE // 2, row * SQUARESIZE + SQUARESIZE // 2
                rect  = IMAGES[piece].get_rect(center = im_center)
                screen.blit(IMAGES[piece], rect)
                #screen.blit(IMAGES[piece], p.Rect(column*SQUARESIZE,row*SQUARESIZE,SQUARESIZE,SQUARESIZE))

def highlighter(screen, sqSelected,validMoves):
    if sqSelected != ():
        row, column = sqSelected
        s = p.Surface( (SQUARESIZE, SQUARESIZE) )
        s.set_alpha(100)
        s.fill(p.Color('blue'))
        screen.blit(s, (column * SQUARESIZE, row*SQUARESIZE))

        s.fill(p.Color('red'))
        for move in validMoves:
            screen.blit(s, (move.endColumn * SQUARESIZE, move.endRow*SQUARESIZE))

main = Main()
main.mainLoop()
