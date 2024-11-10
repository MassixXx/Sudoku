# Sudoku Game and Solver
Welcome to the Sudoku Game and Solver project! This is a Python-based application for playing and solving Sudoku puzzles, featuring an interactive command-line interface, an intelligent solver using multiple decision rules, and organized code with key design patterns.

### Features
**Play Mode:** Load a Sudoku puzzle from a file and play by manually filling in values.
Solver Mode: Use the in-app solver to automatically solve puzzles based on logical decision rules.
**Save and Reset:** Track changes to the puzzle with an undo-like feature to reset to earlier versions.
**Command Line Interface:** Simple text-based interface with commands for loading, displaying, and solving the puzzle, as well as viewing notes and history.

### Getting Started
#### Prerequisites
Python 3

#### Installation
Clone the repository:

```
git clone https://github.com/your-username/sudoku-solver.git
cd Sudoku
```
#### Running the Application
To start the Sudoku game interface, run:
```
python game.py
```

This will launch an interactive command loop where you can load a puzzle, set values, display the grid, and apply solving rules.

#### Running Tests
To run the automated tests, use:

```
python test.py
```
### Commands and Instructions
For a full list of commands and usage examples, please refer to `instructions.md`.

### Design Patterns
This project implements several key design patterns for improved code organization:

- Factory Method: Initializes different types of grid zones (rows, columns, squares).
- Observer Pattern: Updates related zones when a cell’s value changes.
- Memento Pattern: Tracks the grid’s history for resets and undo functionality.
- Command Pattern: Handles commands in the main game loop, allowing modular addition of features.
