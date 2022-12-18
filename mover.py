class mover():

    ranksToRows = { "1":7, "2":6, "3":5, "4":4, 
                    "5":3, "6":2, "7":1, "8":0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}

    filesToCols = { "a":0, "b":1, "c":2, "d":3, 
                    "e":4, "f":5, "g":6, "h":7}
    colsToFiles = {v: k for k, v in filesToCols.items()}
    

    def __init__(self, startSquare, endSquare, board):
        self.startRow = startSquare[0]
        self.startColumn = startSquare[1]
        self.endRow = endSquare[0]
        self.endColumn = endSquare[1]

        self.pieceToMove = board[self.startRow][self.startColumn]
        self.squareToGo = board[self.endRow][self.endColumn]

        self.id = self.startRow*1000 + self.startColumn*100 + self.endRow*10 + self.endColumn

        self.blankselected = False
        
    def __eq__(self, other):
        if isinstance(other, mover):
            return self.id == other.id
        return False

    def MoveNotation(self):
        return self.getSquare(self.startRow, self.startColumn) + self.getSquare(self.endRow, self.endColumn)

    def getSquare(self, row, column):
        return self.colsToFiles[column] + self.rowsToRanks[row]


