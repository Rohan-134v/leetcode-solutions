import math

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        n = len(coins)
        subsets = []
        for i in range(1, 1 << n):
            current_lcm = 1
            set_bits = 0
            for j in range(n):
                if i & (1 << j):
                    current_lcm = math.lcm(current_lcm, coins[j])
                    set_bits += 1
            sign = 1 if set_bits % 2 == 1 else -1
            subsets.append((current_lcm, sign))
        def count_valid_amounts(x: int) -> int:
            count = 0
            for lcm_val, sign in subsets:
                count += sign * (x // lcm_val)
            return count

        left = 1
        right = min(coins) * k
        result = right
        
        while left <= right:
            mid = (left + right) // 2
            if count_valid_amounts(mid) >= k:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return result