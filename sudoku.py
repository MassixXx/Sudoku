from typing import Any
from decision import DR1, DR2, DR3
import time 

class GridZone:
    def __init__(self, id, cells =None) -> None:
        self.id = id 
        self._number_tracker = set()
        self.cells = []
        if cells:
            for cell in cells:
                self.add_cell_to_zone(cell)
            
    def val_is_in_zone(self, val):
        return val in self._number_tracker
    
    def get_remaining_numbers(self):
        return set([i for i in range(1,10) if i not in self._number_tracker])
    
    def get_empty_cells(self):
        return [cell for cell in self.cells if cell.val == -1]
      
    def is_completed(self):
        return len(self._number_tracker) == 9

    def add_cell_to_zone(self, cell):
        if cell.val in self._number_tracker:
            raise Exception(f"Error in cell {cell.id} in gridZone {self.id}: cell value already in gridZone.")
        elif cell.val != -1 and (cell.val < 1 or cell.val > 9):
            raise Exception(f"Error in cell {cell.id} in gridZone {self.id}: Cell value should be between 1 and 9 or -1 if empty.")
        elif cell.val != -1:
            self._number_tracker.add(cell.val)

        cell.zones.append(self)
        self.cells.append(cell)

    def onCellUpdate(self, new_val):
        self._number_tracker.clear()
        for cell in self.cells:
            if cell.val in self._number_tracker:
                raise Exception(f"Error in cell {cell.id} in gridZone {self.id}: cell value already in gridZone.")
            elif cell.val != -1:
                self._number_tracker.add(cell.val)

        for cell in self.cells:
            if cell.is_empty():
                cell.substract_note({new_val})


class Row(GridZone):
    def __init__(self, id, row_number, cells= None) -> None:
        super().__init__(id, cells)
        self.row_number = row_number


class Column(GridZone):
    def __init__(self, id, column_number, cells= None) -> None:
        super().__init__(id, cells)
        self.column_number = column_number

class Square(GridZone):
    def __init__(self, id, grid_number, cells= None) -> None:
        super().__init__(id, cells)
        self.grid_number = grid_number



class Cell:
    def __init__(self, id, val = -1) -> None:
        self.id = id 
        self.val = val
        self.note = Note()
        self.zones = []

    def get_notes(self):
        return self.note.get()
    
    def add_note(self, v):
        self.note.add(v)
        self._on_note_update()

    def clear_note(self):
        self.note.clear()

    def remove_note(self, v):
        self.note.remove(v)
        self._on_note_update()
    
    def set_note(self, values):
        self.note.set(values)
        self._on_note_update()

    def substract_note(self, s):
        self.note.substract(s)
        self._on_note_update()

    def _on_note_update(self):
        if len(self.get_notes()) == 1:
            val = list(self.get_notes())[0]
            print(f"update cell {self.id} with {val}")
            self.set_value(val)

    def is_empty(self):
        return self.val == -1
    
    
    
    def set_value(self, v):
        if (v != -1) and (v < 1 or v > 9):
             raise Exception(f"Error in cell {self.id}: Cell value should be between 1 and 9 or -1 if empty.")
        
        for zone in self.zones:
            if zone.val_is_in_zone(v):
                raise  Exception(f"Error in cell {self.id} in gridZone {zone.id}: cell value already in {zone.id}.")
        
        self.val = v
        
        for zone in self.zones:
            zone.onCellUpdate(new_val = v)

        
        
    def set_notes(self):
        remaining_numbers = [set(zone.get_remaining_numbers()) for zone in self.zones]
        intersect = set.intersection(*remaining_numbers)
        self.note.set(intersect)



class Note:
    def __init__(self) -> None:
        self.values = set()
    
    def clear(self):
        self.values.clear()

    def get(self):
        return self.values

    def add(self, v):
        self.values.add(v) 
    
    def set(self, values):
        self.values.clear()
        self.values = values
    
    def remove(self, v):
        if v in self.values:
            self.values.remove(v)
    
    def substract(self, s):
        self.values -= s




class Grid:
    def __init__(self, values = None):
        self.rows = [Row(f"Row{i}", i) for i in range(1,10)]
        self.columns = [Column(f"Column{i}", i) for i in range(1,10)]
        self.squares = [Square(f"Square{i}", i) for i in range(1,10)]

        for i in range(81):
            val = -1 if values is None else values[i]
            row = i // 9
            col = i % 9
            square = (row // 3) * 3 + (col // 3)

            cell = Cell(f"R{row + 1}C{col + 1}", val)

            self.rows[row].add_cell_to_zone(cell)
            self.columns[col].add_cell_to_zone(cell)
            self.squares[square].add_cell_to_zone(cell)
           
    def set_value(self, row,col, val):
        cell = self.rows[row - 1].cells[col - 1]
        cell.set_value(val)

    def is_completed(self):
        zones = self.rows + self.columns + self.squares
        for zone in zones:
            if not zone.is_completed():
                return False
        
        return True
    
    def load_from_file(self, file_path):
        """Load the grid from a text file with a given path."""
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

            if len(lines) != 9:
                raise Exception("Invalid format: The file must contain exactly 9 lines.")

            values = []
            for line_number, line in enumerate(lines, start=1):
                elements = line.strip().split(',')

                if len(elements) != 9:
                    raise Exception(f"Invalid format on line {line_number}: Each line must contain exactly 9 elements.")

                for element in elements:
                    try:
                        value = int(element)
                        if value not in range(1, 10) and value not in [-1, 0]:
                            raise Exception(f"Invalid value {value} on line {line_number}: Values must be between 1 and 9, or -1/0 for empty cells.")
                        # Convert 0 to -1 for empty cells.
                        values.append(-1 if value == 0 else value)
                    except ValueError:
                        raise Exception(f"Invalid format on line {line_number}: All elements must be integers.")

            # Reinitialize the grid with the parsed values.
            self.__init__(values)
            print("Grid loaded successfully.")

        except FileNotFoundError:
            raise Exception(f"File not found: {file_path}")
        except IOError:
            raise Exception(f"An error occurred while reading the file: {file_path}")
        
    def display(self):
        """Display the grid in a formatted frame."""
        print(("+" + "---+" * 3) * 3)
        for i, row in enumerate(self.rows):
            row_string = "|"
            for j, cell in enumerate(row.cells):
                cell_value = cell.val if cell.val != -1 else " "
                row_string += f" {cell_value} |"
                if (j + 1) % 3 == 0 and j != 8:
                    row_string += "|"
            print(row_string)
            print(("+" + "---+" * 3) * 3)


grid = Grid()
grid.load_from_file("sudoku_medium.txt")

for _ in range(20):
    DR3.infer_decision(grid)
grid.display()