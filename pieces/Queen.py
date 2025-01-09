# pieces/queen.py
from pieces.Unit import Unit


class Queen(Unit):
    def __init__(self, color):
        super().__init__("queen", True, color, 2)

    def move(self, move_from, move_to, board):
        valid_moves = []
        move_to_check = None

        for i in [-1, 1]:
            j = 1
            # Rook-like moves: up and down
            while True:
                try:
                    move_to_check = [move_from[0] + i * j, move_from[1]]
                    target_unit = board.get_unit(move_to_check)
                    if target_unit.color != self.color or not target_unit.is_alive:
                        valid_moves.append(move_to_check)
                        j += 1
                        if target_unit.color != self.color and target_unit.is_alive:
                            break
                    else:
                        break
                except Exception:
                    break

            j = 1
            # Rook-like moves: left and right
            while True:
                try:
                    move_to_check = [move_from[0], move_from[1] + i * j]
                    target_unit = board.get_unit(move_to_check)
                    if target_unit.color != self.color or not target_unit.is_alive:
                        valid_moves.append(move_to_check)
                        j += 1
                        if target_unit.color != self.color and target_unit.is_alive:
                            break
                    else:
                        break
                except Exception:
                    break

        for i in [-1, 1]:
            j = 1
            # Bishop-like moves: \ (diagonal)
            while True:
                try:
                    move_to_check = [move_from[0] + i * j, move_from[1] + i * j]
                    target_unit = board.get_unit(move_to_check)
                    if target_unit.color != self.color or not target_unit.is_alive:
                        valid_moves.append(move_to_check)
                        j += 1
                        if target_unit.color != self.color and target_unit.is_alive:
                            break
                    else:
                        break
                except Exception:
                    break

            j = 1
            # Bishop-like moves: / (diagonal)
            while True:
                try:
                    move_to_check = [move_from[0] - i * j, move_from[1] + i * j]
                    target_unit = board.get_unit(move_to_check)
                    if target_unit.color != self.color or not target_unit.is_alive:
                        valid_moves.append(move_to_check)
                        j += 1
                        if target_unit.color != self.color and target_unit.is_alive:
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
