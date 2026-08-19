import collections
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved_map = collections.defaultdict(int)
        for row, seat in reservedSeats:
            reserved_map[row] |= (1 << seat)
        
        max_groups = n * 2
        LEFT_MASK = 60
        MIDDLE_MASK = 240
        RIGHT_MASK = 960
        
        for row, bitmask in reserved_map.items():
            max_groups -= 2
            
            left_free = (bitmask & LEFT_MASK) == 0
            right_free = (bitmask & RIGHT_MASK) == 0
            middle_free = (bitmask & MIDDLE_MASK) == 0
            
            if left_free and right_free:
                max_groups += 2
            elif left_free or right_free or middle_free:
                max_groups += 1
                
        return max_groups