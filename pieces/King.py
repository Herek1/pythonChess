# pieces/king.py
from pieces.Empty import Empty
from pieces.Rook import Rook
from pieces.Unit import Unit


class King(Unit):
    def __init__(self, color):
        super().__init__("king", True, color, 1)

    def move(self, move_from, move_to, board):
        valid_moves = []
        check_color = self.color

        # Check all adjacent squares
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    move_to_check = [move_from[0] + i, move_from[1] + j]
                    target_unit = board.get_unit(move_to_check)
                    if target_unit.color != check_color or not target_unit.is_alive:
                        valid_moves.append(move_to_check)
                except Exception:
                    continue

        # Castling (O-O)
        move_to_check = [move_from[0], move_from[1] + 2]
        initial_rook_position_r = [move_from[0], move_from[1] + 3]
        new_rook_position_r = [move_from[0], move_from[1] + 1]
        if move_to_check == move_to:
            if not board.get_unit([move_from[0], move_from[1] + 1]).is_alive:
                if not board.get_unit(move_to_check).is_alive:
                    if not self.moved and not board.get_unit(initial_rook_position_r).moved:
                        valid_moves.append(move_to_check)
                        board.set_unit(new_rook_position_r, Rook(check_color))
                        board.set_unit(initial_rook_position_r, Empty())

        # Castling (O-O-O)
        move_to_check = [move_from[0], move_from[1] - 2]
        initial_rook_position_l = [move_from[0], move_from[1] - 4]
        new_rook_position_l = [move_from[0], move_from[1] - 1]
        if move_to_check == move_to:
            if not board.get_unit([move_from[0], move_from[1] - 1]).is_alive:
                if not board.get_unit([move_from[0], move_from[1] - 2]).is_alive:
                    if not board.get_unit(move_to_check).is_alive:
                        if not self.moved and not board.get_unit(initial_rook_position_l).moved:
                            valid_moves.append(move_to_check)
                            board.set_unit(new_rook_position_l, Rook(check_color))
                            board.set_unit(initial_rook_position_l, Empty())

        if move_to in valid_moves:
            print("valid move")
            self.moved = True
            return True
        else:
            print("invalid move")
            return False
