# Five in a Row / Caro Game (Vietnamese version)

A Python implementation of the Vietnamese game: **Five in a Row** or **Caro Game**,
built with the Tkinter library. The game is played on a 30x30 grid and allows two players
to take turns placing their marks (X and O). The first player to get an unblocked sequence
of five in a row wins the game. The first player to reach 3 wins first wins the match.


### Features

- **Interactive Gameplay**: Players alternate turns by clicking on the grid.
- **Win Detection**: Automatically checks for a winner after every move.
- **Blocked Rule**: A sequence of five that is blocked on both ends does not count as a win.
- **Restart Option**: After a win, players can restart the game by clicking on the board.
- **Score Tracking**: Displays the total wins for each player when the game is finished.
- **Winning Condition**: Player needs to win 3 games from the opponent to win the match.


### How to Play

1. **Start the Game**: Run the Python script to open the game window.

2. **Make a Move**: Click on any cell to place your mark (X or O). Players alternate turns.

3. **Win the Game**: Form a sequence of five unblocked marks in:

    - Horizontal
    - Vertical
    - Diagonal (both directions)

4. **Restart**: After a win is announced, click on the board to reset the game.

5. **Finish**: The first player to reach 3 wins will win the match and the game is finished.


### How to Run

1. Save the game script as five_in_a_row.py.

2. Open a terminal or command prompt.

3. Navigate to the directory containing the script.

4. Run the following command:

    `python five_in_a_row.py`


### Code Overview

- **Game Board**: A 30x30 grid is drawn using the Canvas.
- **Turn Management**: Alternates between "X" and "O" after each valid move.
- **Win Detection**:

    * Checks for sequences of 5 in all directions (horizontal, vertical, diagonal).
    * Ensures sequences are not blocked on both ends using the is_blocked function.

- **Restart and Quit**:
    
    * The game restarts when clicking the board after a win.
    * Total scores are displayed when the game is finished.
    * The game is closed automatically when the game is finished.


### Customization

- **Board Size**: Adjust WIDTH and HEIGHT to customize the size of the board.
- **Cell Size**: Modify the size of each cell by adjusting the CELL variable.


#### Author

This game is written by [Hoan Phung](https://github.com/hoanphungt)
