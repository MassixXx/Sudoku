from sudoku import Grid

def test_initialization():
    
    """Test if the grid, rows, columns, and squares are initialized properly."""
    grid = Grid()
    assert len(grid.rows) == 9, "Grid should have 9 rows"
    assert len(grid.columns) == 9, "Grid should have 9 columns"
    assert len(grid.squares) == 9, "Grid should have 9 squares"

    for row in grid.rows:
        assert len(row.cells) == 9, f"Each row should have 9 cells, found {len(row.cells)}"
        
    for col in grid.columns:
        assert len(col.cells) == 9, f"Each column should have 9 cells, found {len(col.cells)}"
        
    for square in grid.squares:
        assert len(square.cells) == 9, f"Each square should have 9 cells, found {len(square.cells)}"

    print("Initialization test passed.")


def test_set_value():
    """Test setting values in cells and their effect on zones."""
    grid = Grid()
    grid.set_value(1, 1, 5)  # Set the top-left cell to 5

    cell = grid.rows[0].cells[0]
    assert cell.val == 5, "Cell value should be 5"
    assert grid.rows[0].val_is_in_zone(5), "Row should track value 5"
    assert grid.columns[0].val_is_in_zone(5), "Column should track value 5"
    assert grid.squares[0].val_is_in_zone(5), "Square should track value 5"

    try:
        grid.set_value(1, 2, 5) # Attempt to set duplicate value in the same row
    except Exception as e:
        assert "already in" in str(e), "Should raise an error for duplicate value in a zone"

    print("Set value test passed.")


def test_get_remaining_numbers():
    """Test if the remaining numbers in zones are calculated correctly."""
    grid = Grid()
    grid.set_value(1, 1, 1)  # Set the top-left cell to 1

    remaining_in_row = grid.rows[0].get_remaining_numbers()
    remaining_in_col = grid.columns[0].get_remaining_numbers()
    remaining_in_square = grid.squares[0].get_remaining_numbers()

    assert 1 not in remaining_in_row, "1 should not be in the remaining numbers for the row"
    assert 1 not in remaining_in_col, "1 should not be in the remaining numbers for the column"
    assert 1 not in remaining_in_square, "1 should not be in the remaining numbers for the square"

    print("Get remaining numbers test passed.")


def test_notes_functionality():
    """Test the note-taking functionality of cells."""
    grid = Grid()
    grid.set_value(1, 1, 1)
    cell = grid.rows[0].cells[1]  # Get the second cell in the first row

    cell.set_notes()  # Should calculate notes based on the current state of the grid

    notes = cell.get_notes()
    assert 1 not in notes, "Notes should not contain 1"
    assert 2 in notes and 3 in notes, "Notes should contain 2 and 3 (and others)"

    cell.add_note(4)
    assert 4 in cell.get_notes(), "Note should include 4 after adding it"

    cell.remove_note(4)
    assert 4 not in cell.get_notes(), "Note should not include 4 after removing it"

    print("Notes functionality test passed.")


def test_zone_completion():
    """Test the completion status of a zone when fully populated."""
    grid = Grid()
    for i in range(1, 10):
        grid.set_value(1, i, i) 

    assert grid.rows[0].is_completed(), "Row should be marked as completed"
    assert not grid.columns[0].is_completed(), "Column should not be marked as completed if not full"
    assert not grid.squares[0].is_completed(), "Square should not be marked as completed if not full"

    print("Zone completion test passed.")


if __name__ == "__main__":
    test_initialization()
    test_set_value()
    test_get_remaining_numbers()
    test_notes_functionality()
    test_zone_completion()
