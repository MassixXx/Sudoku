from sudoku import Grid
from decision import DR1, DR2, DR3, DR4
import copy

class Game:
    def __init__(self) -> None:
        self.grid = Grid()
        self.loaded = False
        self.history = []

    def load_grid(self, filepath):
        self.grid.load_from_file(filepath)
        self.loaded = True
        self.history.clear()
        self.history.append(copy.deepcopy(self.grid))


    def check_loaded(self):
        if not self.loaded:
            raise Exception("Cannot display the grid. Please load the grid first.")

    
    def print_grid(self):
        self.check_loaded()
        self.grid.display()

    def set_value(self, row, col, val):
        self.check_loaded()
        self.grid.set_value(row, col, val)
        self.add_current_grid_to_history()

    def solve(self, steps = 20):
        decision_rules = [DR1, DR2, DR3, DR4]
        decision_level = 0
        self.check_loaded()
        cnt = 0
        while (not self.grid.is_completed()) and cnt < steps:
            dr = decision_rules[decision_level]
            dr.infer_decision(self.grid)

            if not self.grid.is_completed():
                if decision_level < 3:
                    decision_level += 1
                else:
                    decision_level -= 1

            cnt += 1
            
        if self.grid.is_completed():
            print(f"Grid solved successfully using a decision rule of level {decision_level + 1}")
        else:
            print("Couldn't solve the grid. You can see the latest versions of the notes by entring the command 'show_notes'. You can then set the value of a cell using the 'set' command.")
        self.add_current_grid_to_history()
        
    def reset(self, i):
        self.check_loaded()

        self.grid = self.history[i]
        self.history = self.history[i:]

    def print_history(self):
        self.check_loaded()
        for i, grid in enumerate(self.history):
            print(f"Grid version {i}:")
            grid.display()
            print("\n--------------------\n")
 
    def add_current_grid_to_history(self):
        self.history.append(copy.deepcopy(self.grid))


    def show_notes(self):
        for row in self.grid.rows:
            for cell in row.cells:
                if cell.is_empty():
                    print(f"notes in {cell.id}: {cell.get_notes()}")

    def help(self):
        print("""
Available commands:
- load <grid_file_path> : Load a grid from the specified file path.
- print or display : Display the current state of the grid.
- show_history : Show the history of grid states.
- solve : Solve the current grid.
- set R<row_number>C<column_number> <value> : Set the cell at specified row and column to <value>.
- reset <i> : Reset the grid to the state <i> in the history.
- show_notes : Display the notes on each empty cell.
- help : Display this help message.
        """)

    def run_command_loop(self):
        """Main loop to wait for and execute commands."""
        print("Sudoku Game - Enter 'help' for a list of commands.")
        
        while True:
            try:
                # Read and parse the user input
                user_input = input("Enter command: ").strip()
                if not user_input:
                    continue

                # Split command and arguments
                parts = user_input.split()
                command = parts[0].lower()

                if command == "load" and len(parts) == 2:
                    self.load_grid(parts[1])

                elif command in ["print", "display"] and len(parts) == 1:
                    self.print_grid()

                elif command == "show_history" and len(parts) == 1:
                    self.print_history()

                elif command == "solve" and len(parts) == 1:
                    self.solve()

                elif command == "set" and len(parts) == 3:
                    location, value = parts[1], parts[2]
                    if location.startswith("R") and "C" in location:
                        try:
                            row, col = map(int, location[1:].split("C"))
                            value = int(value)
                            if row < 1 or row > 9 or col < 1 or col > 9:
                                raise ValueError("Row and column numbers must be between 1 and 9.")
                            self.set_value(row, col, value)
                            print(f"Set cell at row {row}, column {col} to {value}.")
                        except ValueError as e:
                            print(f"Invalid input for 'set' command: {e}")
                    else:
                        print("Invalid format for 'set' command. Use format: set R<row_number>C<column_number> <value>.")

                elif command == "reset" and len(parts) == 2:
                    try:
                        state_index = int(parts[1])
                        self.reset(state_index)
                        print(f"Grid reset to state {state_index}.")
                    except ValueError:
                        print("Invalid input for 'reset' command. Please provide a valid integer index.")
                    except Exception as e:
                        print(e)

                elif command == "show_notes" and len(parts) == 1:
                    self.show_notes()

                elif command == "help" and len(parts) == 1:
                    self.help()

                elif command in ["exit", "quit"]:
                    print("Exiting game.")
                    break

                else:
                    print("Unknown command or invalid format. Type 'help' for a list of commands.")

            except Exception as e:
                print(f"Error: {e}")

    
game = Game()

game.run_command_loop()

