# pieces/pawn.py

from pieces.Unit import Unit

class Pawn(Unit):
    def __init__(self, color):
        super().__init__("pawn", True, color, 0)

    def move(self, move_from, move_to, board):
        valid_moves = []
        check_color = self.color
        move_to_check = None

        # Move forward
        try:
            move_to_check = [move_from[0] - 1 if check_color else move_from[0] + 1, move_from[1]]
            if board.get_unit(move_to_check).type == "empty":
                valid_moves.append(move_to_check)
        except Exception:
            pass

        # Move forward two spaces
        try:
            move_to_check = [move_from[0] - 2 if check_color else move_from[0] + 2, move_from[1]]
            move_to_check2 = [move_from[0] - 1 if check_color else move_from[0] + 1, move_from[1]]
            if (
                board.get_unit(move_to_check).type == "empty"
                and board.get_unit(move_to_check2).type == "empty"
                and move_from[0] == (6 if check_color else 1)
            ):
                valid_moves.append(move_to_check)
        except Exception:
            pass

        # Diagonal capture
        for i in [-1, 1]:
            try:
                move_to_check = [
                    move_from[0] - 1 if check_color else move_from[0] + 1,
                    move_from[1] + i if check_color else move_from[1] - i,
                ]
                target_unit = board.get_unit(move_to_check)
                if target_unit.color != self.color and target_unit.is_alive:
                    valid_moves.append(move_to_check)
            except Exception:
                pass

        # Check if the move is valid
        if move_to in valid_moves:
            print("valid move")
            return True
        else:
            print("invalid move")
            return False
