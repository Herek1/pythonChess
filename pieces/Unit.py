# pieces/unit.py

class Unit:
    def __init__(self, unit_type, is_alive, color, look_code):
        self.type = unit_type
        self.is_alive = is_alive
        self.color = color
        self.look = self.get_look(look_code, color)
        self.moved = False

    @staticmethod
    def get_look(look_code, color):
        pieces = {
            0: "♙" if color else "♟",
            1: "♔" if color else "♚",
            2: "♕" if color else "♛",
            4: "♗" if color else "♝",
            5: "♖" if color else "♜",
            6: "♘" if color else "♞",
        }
        return pieces.get(look_code, " ")

    def move(self, move_from, move_to, board):
        raise NotImplementedError("Subclasses must implement this method.")

    def __str__(self):
        return self.look
