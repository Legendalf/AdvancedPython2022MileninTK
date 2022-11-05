from typing import List, Optional
from random import shuffle


class ShuffleIterator:
    def __init__(self, values: List[int], num_shuffles: Optional[int] = None):
        self.values = values
        self.num_shuffles = num_shuffles
        self._current_num_shuffles = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self._current_num_shuffles >= self.num_shuffles:
            raise StopIteration()
        
        self._current_num_shuffles += 1

        shuffle(self.values)
        return self.values


for permutation in ShuffleIterator([1, 2, 3], num_shuffles=5):
    print(permutation)
