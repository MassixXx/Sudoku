
# Sudoku Game Instructions

This program allows you to interactively manage and solve Sudoku puzzles through a command-line interface. You can load a puzzle from a file, view and modify the grid, check notes on each cell, and keep track of the puzzle's history as you work toward a solution.

## Table of Contents
- [Getting Started](#getting-started)
- [Commands](#commands)
  - [load](#load-grid_file_path)
  - [print or display](#print-or-display)
  - [show_history](#show_history)
  - [solve](#solve)
  - [set](#set-rrow_numberccolumn_number-value)
  - [reset](#reset-i)
  - [show_notes](#show_notes)
  - [help](#help)
  - [exit or quit](#exit-or-quit)

## Getting Started

1. **Run the Program**: Execute the `game.py` file to start the program.
   ```bash
   python game.py
   ```
2. **Command Prompt**: You will see a prompt that reads `Enter command:`, where you can input any of the following commands.
3. **Run the tests**: Execute the `test.py` file to execute the testing script.
   ```bash
   python test.py
   ```
## Commands

### `load <grid_file_path>`
- **Purpose**: Load a Sudoku grid from a specified text file.
- **Usage**: `load sudoku.txt`
- **File Format**:
  - The file should contain 9 lines, each representing a row in the grid.
  - Each line should have 9 numbers separated by commas, with values between `1` and `9` for filled cells, and `-1` or `0` for empty cells.
- **Example File**:
    ```plaintext
    5,3,-1,-1,7,-1,-1,-1,-1
    6,-1,-1,1,9,5,-1,-1,-1
    -1,9,8,-1,-1,-1,-1,6,-1
    8,-1,-1,-1,6,-1,-1,-1,3
    4,-1,-1,8,-1,3,-1,-1,1
    7,-1,-1,-1,2,-1,-1,-1,6
    -1,6,-1,-1,-1,-1,2,8,-1
    -1,-1,-1,4,1,9,-1,-1,5
    -1,-1,-1,-1,8,-1,-1,7,9
    ```

### `print` or `display`
- **Purpose**: Display the current state of the grid on the console.
- **Usage**: `print` or `display`

### `show_history`
- **Purpose**: Display all previous states of the grid since it was loaded or reset, allowing you to review past versions.
- **Usage**: `show_history`

### `solve`
- **Purpose**: Solve (or try) the current Sudoku puzzle.
- **Usage**: `solve`

### `set R<row_number>C<column_number> <value>`
- **Purpose**: Set a specific cell in the grid to a given value.
- **Usage**: `set R2C3 7` sets the cell at row 2, column 3 to `7`.
- **Constraints**: 
  - `<row_number>` and `<column_number>` must be between 1 and 9.
  - `<value>` must be between `1` and `9`.

### `reset <i>`
- **Purpose**: Reset the grid to a previous state saved in the history.
- **Usage**: `reset 2` restores the grid to the version saved at index `2` in the history.
- **Constraints**: 
  - `<i>` should be a valid index in the history list (between 0 and the last state index).
- **Note**: Resetting to an earlier state clears subsequent states from the history.

### `show_notes`
- **Purpose**: Display potential notes on each empty cell in the grid.
- **Usage**: `show_notes`

### `help`
- **Purpose**: Display a list of all available commands with descriptions.
- **Usage**: `help`

### `exit` or `quit`
- **Purpose**: Exit the program.
- **Usage**: `exit` or `quit`

## Example Usage

```plaintext
Enter command: load sudoku.txt
Grid loaded successfully.
Enter command: display
+---+---+---+---+---+---+---+---+---+
| 5 | 3 |   |   | 7 |   |   |   |   |
+---+---+---+---+---+---+---+---+---+
| 6 |   |   | 1 | 9 | 5 |   |   |   |
+---+---+---+---+---+---+---+---+---+
|   | 9 | 8 |   |   |   |   | 6 |   |
+---+---+---+---+---+---+---+---+---+
...
Enter command: set R1C3 4
Set cell at row 1, column 3 to 4.
Enter command: display
+---+---+---+---+---+---+---+---+---+
| 5 | 3 | 4 |   | 7 |   |   |   |   |
+---+---+---+---+---+---+---+---+---+
...
Enter command: reset 0
Grid reset to state 0.
Enter command: show_notes
notes in R1C1: {2, 5, 7}
...
Enter command: quit
Exiting game.
```
