# 🤖 AI Tic-Tac-Toe (Python Console Game)

A beginner-friendly Tic-Tac-Toe game where you play as `X` against an unbeatable AI `O` powered by the **Minimax algorithm**. The game runs in the Python console and teaches core concepts of AI and game theory.

---

## 📌 Features

- Play against an unbeatable AI
- Simple and intuitive console interface
- Implements the **Minimax algorithm** from scratch
- Learn about zero-sum games and recursion

---

## 🧠 Concepts Used

- **Game Theory**
- **Minimax Algorithm**
- **Recursive Search**
- **Zero-Sum Decision Making**
- Python Fundamentals (functions, loops, conditionals)

---

## 🛠 Tools & Technologies

- Language: Python (3.x)
- No external libraries required
- Runs entirely in the terminal

---

## ▶️ How to Run

1. **Clone this repository** or copy the code into a `.py` file:
    ```bash
    git clone https://github.com/your-username/ai-tic-tac-toe
    cd ai-tic-tac-toe
    ```

2. **Run the script:**
    ```bash
    python ai_tic_tac_toe.py
    ```

3. **Start playing:**
    - You are `X` and AI is `O`.
    - Enter a number between 0-8 as your move:

      ```
      0 | 1 | 2
      ---------
      3 | 4 | 5
      ---------
      6 | 7 | 8
      ```

---

# 📘 Function Descriptions – AI Tic-Tac-Toe

This document provides detailed explanations of all the functions used in the AI-powered Tic-Tac-Toe game built with Python. Each function plays a specific role in game management, user interaction, or AI decision-making.

---

### `print_board()`

**Purpose:**  
Prints the current game board in a 3x3 grid format using rows and columns.

**How it works:**  
- Slices the 1D `board` list into three rows.
- Prints each row with vertical separators (`|`) to mimic a Tic-Tac-Toe grid.

---

### `available_moves()`

**Purpose:**  
Returns a list of indices representing unoccupied positions on the board.

**How it works:**  
- Loops through the `board` using `enumerate`.
- Collects indices where the value is a blank space (`' '`).

---

### `make_move(position, player)`

**Purpose:**  
Places the player’s symbol ('X' or 'O') on the board at the specified index.

**How it works:**  
- Directly assigns the symbol to the corresponding index in the `board` list.

---

### `winner(player)`

**Purpose:**  
Checks if the given player has a winning combination on the board.

**How it works:**  
- Defines all 8 possible winning combinations (rows, columns, diagonals).
- Uses `all()` to verify if all positions in any combination contain the player's symbol.

---

### `is_full()`

**Purpose:**  
Checks if the board is full (i.e., a tie situation).

**How it works:**  
- Returns `True` if there are no spaces (`' '`) left on the board.

---

### `minimax(is_maximizing)`

**Purpose:**  
Core AI algorithm that simulates all possible future game states and calculates the best possible move for the AI.

**Parameters:**  
- `is_maximizing`: Boolean flag. If `True`, AI's turn. If `False`, player's turn.

**How it works:**  
- Returns a score:
  - `+1` if AI wins.
  - `-1` if human wins.
  - `0` for a tie.
- For maximizing:
  - Tries every available move, recursively calls `minimax(False)`, and selects the highest score.
- For minimizing:
  - Tries every available move, recursively calls `minimax(True)`, and selects the lowest score.

**Concepts Used:**  
- Recursion  
- Backtracking  
- Game Tree Simulation

---

### `best_ai_move()`

**Purpose:**  
Finds the best possible move for the AI using the `minimax` function.

**How it works:**  
- Iterates through each available move.
- Simulates the move, gets its score via `minimax(False)`, then undoes the move.
- Tracks the move with the highest score and returns it.

---

### `play()`

**Purpose:**  
Main game loop that drives the interaction between the user and the AI.

**How it works:**  
- Greets the player and prints the initial board.
- Repeatedly:
  - Takes user input for move.
  - Updates board, checks for win/tie.
  - Lets AI choose its move using `best_ai_move()`.
  - Updates board, checks for win/tie.
- Ends when someone wins or the board is full.

---

## ✅ Summary

This modular function-based design ensures the code is clean, maintainable, and scalable. Each function has a single, clear responsibility, which aligns well with best practices in software development.



---

## 🏁 Future Enhancements (Optional Ideas)

- GUI using **Tkinter**
- Add **difficulty levels** (easy/medium/hard)
- Add **score tracking**
- Integrate **voice input** using SpeechRecognition
- Multiplayer (2 human players)

---

## 📚 Learning Resources

- [Minimax Algorithm Explained](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/)
- [Python Tic Tac Toe Minimax Tutorial](https://www.youtube.com/watch?v=trKjYdBASyQ)
- [MIT Intro to AI Lectures (OpenCourseWare)](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-fall-2010/)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Safal Bhattarai**  
📧 bhattarairobert@gmail.com  
🌐 [GitHub](https://github.com/RobertBhattrai)



