import tkinter as tk
from tkinter import simpledialog

from board.Board import Board
from pieces.Empty import Empty


class ChessBoard:
    TILE_SIZE = 80
    BOARD_SIZE = 8

    def __init__(self):
        self.board = Board()
        self.turn = True
        self.move_from = []
        self.move_to = []

        self.root = tk.Tk()
        self.root.title("Chess")
        self.canvas = tk.Canvas(self.root, width=self.TILE_SIZE * self.BOARD_SIZE,
                                 height=self.TILE_SIZE * self.BOARD_SIZE)
        self.canvas.pack()
        self.draw_board()
        self.root.mainloop()

    def draw_board(self):
        self.canvas.delete("all")

        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                x1 = col * self.TILE_SIZE
                y1 = row * self.TILE_SIZE
                x2 = x1 + self.TILE_SIZE
                y2 = y1 + self.TILE_SIZE

                fill_color = "grey" if (row + col) % 2 == 0 else "darkgrey"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="black")

                unit = self.board.get_unit([row, col])
                if unit:
                    self.canvas.create_text(
                        (x1 + x2) // 2, (y1 + y2) // 2,
                        text=unit.look, font=("Arial", 24),
                        fill="white" if unit.color else "black"
                    )

        self.canvas.bind("<Button-1>", self.handle_click)

    def handle_click(self, event):
        col = event.x // self.TILE_SIZE
        row = event.y // self.TILE_SIZE

        if not self.move_from:
            self.move_from = [row, col]
            print(f"Selected piece at: ({row}, {col})")
        else:
            self.move_to = [row, col]
            print(f"Move piece to: ({row}, {col})")

            current_move = self.board.get_unit(self.move_from)
            if current_move.color == self.turn:
                if current_move.move(self.move_from, self.move_to, self.board):
                    temp = self.board.get_unit(self.move_from)
                    self.board.set_unit(self.move_to, temp)
                    self.board.set_unit(self.move_from, Empty())

                    if temp.type == "pawn" and self.move_to[0] in [0, 7]:
                        piece_type = self.show_promotion_dialog()
                        self.board.promote_pawn(self.move_to, piece_type)

                    self.turn = not self.turn
                else:
                    print("Invalid move")
            else:
                print("Wrong color")

            self.move_from.clear()
            self.move_to.clear()
            self.draw_board()

    def show_promotion_dialog(self):
        piece_types = ["Queen", "Rook", "Bishop", "Knight", "Pawn"]
        dialog = simpledialog.askstring("Pawn Promotion", "Promote to (Queen, Rook, Bishop, Knight, Pawn):")
        if dialog in piece_types:
            return dialog
        return "Pawn"

if __name__ == "__main__":
    ChessBoard()

