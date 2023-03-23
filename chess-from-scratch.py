import numpy as np

class Piece:
    none =   np.uint8(0)
    king =   np.uint8(1)
    pawn =   np.uint8(2)
    knight = np.uint8(3) 
    bishop = np.uint8(4)
    rook =   np.uint8(5)
    queen =  np.uint8(6)
    white = np.uint8(8)
    black = np.uint8(16)

class Board: 
    casillas = np.zeros(shape=64, dtype=np.uint8)
    def loadPositionFromFen (self, fen):
        dict = {
            'k': Piece.king,
            'p': Piece.pawn,
            'n': Piece.knight,
            'b': Piece.bishop,
            'r': Piece.rook,
            'q': Piece.queen
        }
        fenBoard = fen.split(' ')[0]
        rank = 7
        file = 0
        for e in fenBoard:
            if (e == '/'):
                file = 0
                rank = rank - 1
            else:
                if (e.isdigit()):
                    file = file + int(e)
                else:
                    if e.isupper():
                        pieceColour = Piece.white
                    else:
                        pieceColour = Piece.black
                    pieceType = dict[str(e.lower())]
                    self.casillas[rank * 8 + file] = pieceType + pieceColour

    