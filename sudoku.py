from typing import Any


class Grid:
    def ____init__(self, items, id):
        self._items = items
        self._self._completed = False
        self._number_tracker = {}
        for i in items:
            if i == -1:
                continue
            elif (i in self._number_tracker):
                raise Exception("Format invalid for grid {self._id}")
    def _check_valid(self):
        number_tracker