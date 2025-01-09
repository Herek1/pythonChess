# pieces/knight.py

from pieces.Unit import Unit

class Knight(Unit):
    def __init__(self, color):
        super().__init__("knight", True, color, 6)

    def move(self, move_from, move_to, board):
        valid_moves = []
        check_color = self.color
        move_to_check = None

        for i in [-1, 1]:
            for j in [-1, 1]:
                try:
                    move_to_check = [move_from[0] + 2 * i, move_from[1] + j]
                    target_unit = board.get_unit(move_to_check)
                    if target_unit.color != check_color or not target_unit.is_alive:
                        valid_moves.append(move_to_check)
                except Exception:
                    pass

        for i in [-1, 1]:
            for j in [-1, 1]:
                try:
                    move_to_check = [move_from[0] + i, move_from[1] + 2 * j]
                    target_unit = board.get_unit(move_to_check)
                    if target_unit.color != check_color or not target_unit.is_alive:
                        valid_moves.append(move_to_check)
                except Exception:
                    pass

        if move_to in valid_moves:
            print("valid move")
            return True
        else:
            print("invalid move")
            return False
