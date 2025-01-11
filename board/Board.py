# board/board.py
from pieces.Bishop import Bishop
from pieces.Empty import Empty
from pieces.King import King
from pieces.Knight import Knight
from pieces.Pawn import Pawn
from pieces.Queen import Queen
from pieces.Rook import Rook


class Board:
    def __init__(self):
        self.unit = [[Empty() for _ in range(8)] for _ in range(8)]

        for i in range(8):
            self.unit[6][i] = Pawn(True)
        for i in range(8):
            self.unit[1][i] = Pawn(False)

        self.unit[0][0] = Rook(False)
        self.unit[0][7] = Rook(False)
        self.unit[0][1] = Knight(False)
        self.unit[0][6] = Knight(False)
        self.unit[0][2] = Bishop(False)
        self.unit[0][5] = Bishop(False)
        self.unit[0][3] = Queen(False)
        self.unit[0][4] = King(False)
        self.unit[7][0] = Rook(True)
        self.unit[7][7] = Rook(True)
        self.unit[7][1] = Knight(True)
        self.unit[7][6] = Knight(True)
        self.unit[7][2] = Bishop(True)
        self.unit[7][5] = Bishop(True)
        self.unit[7][3] = Queen(True)
        self.unit[7][4] = King(True)

    def get_unit(self, position):
        return self.unit[position[0]][position[1]]

    def set_unit(self, position, unit):
        self.unit[position[0]][position[1]] = unit

    def promote_pawn(self, pawn_position, unit_type):
        unit = self.get_unit(pawn_position)
        color = unit.color
        chosen_unit = {
            "Queen": Queen(color),
            "Bishop": Bishop(color),
            "Knight": Knight(color),
            "Rook": Rook(color),
        }.get(unit_type, Pawn(color))
        self.set_unit(pawn_position, chosen_unit)