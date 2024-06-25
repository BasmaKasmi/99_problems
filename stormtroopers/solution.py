from typing import List
from collections import Counter

def stormtroopers(numbers: List[int]) -> List[int]:
    occurrences = Counter(numbers)
    return [num for num, count in occurrences.items() if count == 1]

