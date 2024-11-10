from itertools import combinations

class DecisionRule:
    def __init__(self, level) -> None:
        self.level = level 

    def infer_decision(grid):
        pass

class DR1(DecisionRule):
    def infer_decision(grid):
        for row in grid.rows:
            for cell in row.cells:
                if cell.is_empty():
                    for zone in cell.zones:
                        remaining_numbers = zone.get_remaining_numbers()
                        cell.set_note(remaining_numbers)
                        """
                        if len(remaining_numbers) == 1:
                            val = list(remaining_numbers)[0]
                            print(f"update cell {cell.id} with {val}")
                            cell.set_value(val)
                            break
                        """
                    
class DR2(DecisionRule):
    def infer_decision(grid):
        for row in grid.rows:
            for cell in row.cells:
                if cell.is_empty():
                    remaining_numbers = [zone.get_remaining_numbers() for zone in cell.zones]
                    intersect = set.intersection(*remaining_numbers)
                    cell.set_note(intersect)
                    """
                    if len(intersect) == 1:
                        val = list(intersect)[0]
                        print(f"update cell {cell.id} with {val}")
                        cell.set_value(val)
                    """

class DR3(DecisionRule):
    def infer_decision(grid):
        grid_zones = grid.rows + grid.columns + grid.squares


        for zone in grid_zones:
            pairs = set()
            triples = {}
            to_remove = set()
            for cell in zone.cells:
                if cell.is_empty(): 

                    notes = cell.get_notes()

                    if len(notes) == 2:
                        notes_list = sorted(list(notes))
                        pair = (notes_list[0], notes_list[1])
                        if pair in pairs:
                            to_remove.add(pair)
                        else:
                            pairs.add(pair)
                    elif len(notes) == 3:
                        intersect_list = sorted(list(notes))
                        triplet = (intersect_list[0], intersect_list[1], intersect_list[2])
                        if triplet in triples:
                            if triples[triplet] == 2:
                                to_remove.add(triplet)
                            else:
                                triples[triplet] += 1
                        else:
                            triples[triplet] = 1
                        
            for cell in zone.cells:
                if cell.is_empty():
                    for tuple in to_remove:
                        substract_set = set(tuple)
                        if cell.get_notes() != substract_set:
                            cell.substract_note(substract_set)


class DR4(DecisionRule):
    def infer_decision(grid):
        grid_zones = grid.rows + grid.columns + grid.squares


        for zone in grid_zones:
            number_tracker = {i:[] for i in range(1,10)}

            for cell in zone.cells:
                if cell.is_empty(): 
                    notes = cell.get_notes()
                    for note in notes:
                        number_tracker[note].append(cell)
                    
            for i, list_i in number_tracker.items():
                if len(list_i) == 1:
                    cell = list_i[0]
                    cell.set_value(i)
