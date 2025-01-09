# pieces/empty.py
from pieces.Unit import Unit


class Empty(Unit):
    def __init__(self):
        super().__init__("empty", False, False, 7)

    def move(self, move_from, move_to, board):
        print("Empty")
        return False
