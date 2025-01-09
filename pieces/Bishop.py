# pieces/bishop.py

from pieces.Unit import Unit

class Bishop(Unit):
    def __init__(self, color):
        super().__init__("bishop", True, color, 4)

    def move(self, move_from, move_to, board):
        valid_moves = []
        check_color = self.color

        for i in [-1, 1]:
            j = 1
            # Diagonal \
            while True:
                try:
                    move_to_check = [move_from[0] + i * j, move_from[1] + i * j]
                    target_unit = board.get_unit(move_to_check)
                    if target_unit.color != check_color or not target_unit.is_alive:
                        valid_moves.append(move_to_check)
                        j += 1
                        if target_unit.color != check_color and target_unit.is_alive:
                            break
                    else:
                        break
                except Exception:
                    break

            j = 1
            # Diagonal /
            while True:
                try:
                    move_to_check = [move_from[0] - i * j, move_from[1] + i * j]
                    target_unit = board.get_unit(move_to_check)
                    if target_unit.color != check_color or not target_unit.is_alive:
                        valid_moves.append(move_to_check)
                        j += 1
                        if target_unit.color != check_color and target_unit.is_alive:
                            break
                    else:
                        break
                except Exception:
                    break

        if move_to in valid_moves:
            print("valid move")
            return True
        else:
            print("invalid move")
            return False
