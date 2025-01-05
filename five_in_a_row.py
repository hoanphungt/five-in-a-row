import tkinter as tk

root = tk.Tk()
root.title("Five in a Row / Caro Game")

SIZE = 1500
COLS = 30
ROWS = 30
CELL = SIZE // COLS
TURN = "X"

# Board state
board = [[None for _ in range(COLS)] for _ in range(ROWS)]

# Winners state
winners = []

canvas = tk.Canvas(root, width=SIZE, height=SIZE)
canvas.pack()


# Draw the board
def draw_board():
    for i in range(COLS):
        canvas.create_line(CELL * i, 0, CELL * i, SIZE, fill="black")
        canvas.create_line(0, CELL * i, SIZE, CELL * i, fill="black")


# Click function
def play(event):
    global TURN, winners
    col = event.x // CELL
    row = event.y // CELL
    x_center = col * CELL + CELL // 2
    y_center = row * CELL + CELL // 2
    if board[row][col] is not None:
        return
    board[row][col] = TURN
    canvas.create_text(x_center, y_center, text=TURN, font=("Arial", 20))
    TURN = "O" if TURN == "X" else "X"

    # Check if there is a winner
    winner = detect_winner()
    if winner is not None:
        print(f"{winner} wins!")
        TURN = "X" if winner == "O" else "O"
        winners.append(winner)
        canvas.create_text(SIZE // 2, SIZE // 2, text=f"{winner} wins!", font=("Arial", 50))
        canvas.unbind("<Button-1>")
        canvas.bind("<Button-1>", restart)
        return


# Helper function to check if the winner is blocked
def is_blocked(row, col, current) -> bool:
    if row < 0 or row > ROWS - 1 or col < 0 or col > COLS - 1:
        return False
    return board[row][col] is not None and board[row][col] != current


# Detect winner
def detect_winner() -> str | None:
    for row in range(ROWS):
        for col in range(COLS):
            current = board[row][col]
            if current is None:
                continue
            # Check horizontal
            if col + 4 < COLS and all(board[row][col + i] == current for i in range(5)):
                if is_blocked(row, col - 1, current) and is_blocked(row, col + 5, current):
                    continue
                return current
            # Check vertical
            if row + 4 < ROWS and all(board[row + i][col] == current for i in range(5)):
                if is_blocked(row - 1, col, current) and is_blocked(row + 5, col, current):
                    continue
                return current
            # Check diagonal from left to right
            if (
                row + 4 < ROWS
                and col + 4 < COLS
                and all(board[row + i][col + i] == current for i in range(5))
            ):
                if is_blocked(row - 1, col - 1, current) and is_blocked(row + 5, col + 5, current):
                    continue
                return current
            # Check diagonal from right to left
            if (
                row + 4 < ROWS
                and col - 4 >= 0
                and all(board[row + i][col - i] == current for i in range(5))
            ):
                if is_blocked(row - 1, col + 1, current) and is_blocked(row + 5, col - 5, current):
                    continue
                return current
    return None


def restart(_event):
    global board, TURN
    board = [[None for _ in range(COLS)] for _ in range(ROWS)]
    canvas.delete("all")
    draw_board()
    canvas.unbind("<Button-1>")
    canvas.bind("<Button-1>", play)


def quit():
    x_wins = winners.count("X")
    o_wins = winners.count("O")
    print(f"X wins: {x_wins}")
    print(f"O wins: {o_wins}")
    if x_wins > o_wins:
        print("X wins the game!")
    elif o_wins > x_wins:
        print("O wins the game!")
    else:
        print("It's a draw!")
    root.destroy()


draw_board()
canvas.bind("<Button-1>", play)
root.protocol("WM_DELETE_WINDOW", quit)
root.mainloop()
