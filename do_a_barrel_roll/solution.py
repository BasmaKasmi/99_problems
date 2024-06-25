from typing import List

def do_a_barrel_roll(numbers: List[int], k: int) -> List[int]:
    if not numbers:
        return numbers
    
    k %= len(numbers)
    
    return numbers[k:] + numbers[:k]