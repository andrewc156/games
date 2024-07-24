class Board():
    def __init__(self):
        self.board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
        self.turn = 0

    def clear(self):
        self.board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

    def show(self):
        for row in self.board:
            print(" ".join(row))

    def place(self, x, y):
        if 0 <= x <= 2 and 0 <= y <= 2:
            if self.board[y][x] == "_":  # Ensure the place is empty
                if self.turn % 2 == 0:
                    self.board[y][x] = "X"
                else:
                    self.board[y][x] = "O"
                self.turn += 1
            else:
                print("Place already taken!")
        else:
            print("Place out of range!")

    def check_win(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != "_":
                return True

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != "_":
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != "_":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != "_":
            return True

        return False


# main game loop
def main():
    board = Board()
    while not board.check_win():
        board.show()
        if board.turn % 2 == 0:
            x = int(input("Please enter the x-coordinate of your move: "))
            y = int(input("Please enter the y-coordinate of your move: "))
        else:
            x = int(input("Please enter the x-coordinate of your move: "))
            y = int(input("Please enter the y-coordinate of your move: "))
        board.place(x - 1, y - 1)
    if board.turn % 2 == 0:
        print("Congrats! You won! player 2")
    else:
        print("Congrats! You lost! player 1")


if __name__ == "__main__":
    print("Simple Tic Tac Toe game by Andrew Chincea")
    print("https://github.com/andrewc156")
    print("x-values are from left to right and y-values are from top to bottom.")
    print("ie (1,1) is the top left corner")
    main()
