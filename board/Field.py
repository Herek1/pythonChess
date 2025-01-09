# board/field.py

class Field:
    def __init__(self, position_x, position_y, unit=None):
        self.position_x = position_x
        self.position_y = position_y
        self.unit = unit

    @staticmethod
    def get_position(position):
        return None

    @staticmethod
    def set_position(position, unit):
        pass
