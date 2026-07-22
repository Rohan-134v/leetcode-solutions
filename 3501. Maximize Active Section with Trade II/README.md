# 3501. Maximize Active Section with Trade II

### Difficulty: Hard

## Description
You are given a binary string s of length n, where:


	'1' represents an active section.
	'0' represents an inactive section.


You can perform at most one trade to maximize the number of active sections in s. In a trade, you:


	Convert a contiguous block of '1's that is surrounded by '0's to all '0's.
	Afterward, convert a contiguous block of '0's that is surrounded by '1's to all '1's.


Additionally, you are given a 2D array queries, where queries[i] = [li, ri] represents a substring s[li...ri].

For each query, determine the maximum possible number of active sections in s after making the optimal trade on the substring s[li...ri].

Return an array answer, where answer[i] is the result for queries[i].

Note


	For each query, treat s[li...ri] as if it is augmented with a '1' at both ends, forming t = '1' + s[li...ri] + '1'. The augmented '1's do not contribute to the final count.
	The queries are independent of each other.


 
Example 1:


Input: s = "01", queries = [[0,1]]

Output: [1]

Explanation:

Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.


Example 2:


Input: s = "0100", queries = [[0,3],[0,2],[1,3],[2,3]]

Output: [4,3,1,1]

Explanation:


	
	Query [0, 3] → Substring "0100" → Augmented to "101001"
	Choose "0100", convert "0100" → "0000" → "1111".
	The final string without augmentation is "1111". The maximum number of active sections is 4.
	
	
	Query [0, 2] → Substring "010" → Augmented to "10101"
	Choose "010", convert "010" → "000" → "111".
	The final string without augmentation is "1110". The maximum number of active sections is 3.
	
	
	Query [1, 3] → Substring "100" → Augmented to "11001"
	Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.
	
	
	Query [2, 3] → Substring "00" → Augmented to "1001"
	Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.
	



Example 3:


Input: s = "1000100", queries = [[1,5],[0,6],[0,4]]

Output: [6,7,2]

Explanation:


	
	Query [1, 5] → Substring "00010" → Augmented to "1000101"
	Choose "00010", convert "00010" → "00000" → "11111".
	The final string without augmentation is "1111110". The maximum number of active sections is 6.
	
	
	Query [0, 6] → Substring "1000100" → Augmented to "110001001"
	Choose "000100", convert "000100" → "000000" → "111111".
	The final string without augmentation is "1111111". The maximum number of active sections is 7.
	
	
	Query [0, 4] → Substring "10001" → Augmented to "1100011"
	Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 2.
	



Example 4:


Input: s = "01010", queries = [[0,3],[1,4],[1,3]]

Output: [4,4,2]

Explanation:


	
	Query [0, 3] → Substring "0101" → Augmented to "101011"
	Choose "010", convert "010" → "000" → "111".
	The final string without augmentation is "11110". The maximum number of active sections is 4.
	
	
	Query [1, 4] → Substring "1010" → Augmented to "110101"
	Choose "010", convert "010" → "000" → "111".
	The final string without augmentation is "01111". The maximum number of active sections is 4.
	
	
	Query [1, 3] → Substring "101" → Augmented to "11011"
	Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 2.
	



 
Constraints:


	1 <= n == s.length <= 105
	1 <= queries.length <= 105
	s[i] is either '0' or '1'.
	queries[i] = [li, ri]
	0 <= li <= ri < n

## Submission Details
- **Status**: Accepted
- **Runtime**: 717
- **Memory**: 67428000
- **Language**: python3

## Code
```python3
from typing import List

class SparseTable:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        if self.n == 0:
            return
        self.K = self.n.bit_length()
        self.st = [[0] * self.n for _ in range(self.K)]
        
        for i in range(self.n):
            self.st[0][i] = arr[i]
            
        for j in range(1, self.K):
            length = 1 << (j - 1)
            for i in range(self.n - (1 << j) + 1):
                self.st[j][i] = max(self.st[j - 1][i], self.st[j - 1][i + length])

    def query(self, L: int, R: int) -> int:
        if L > R or self.n == 0:
            return 0
        j = (R - L + 1).bit_length() - 1
        return max(self.st[j][L], self.st[j][R - (1 << j) + 1])


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')
        
        # 1. Identify all zero-groups and map each index in s to its zero-group index
        zero_groups = []  # [(start_idx, length)]
        zero_group_map = [-1] * n
        
        i = 0
        while i < n:
            if s[i] == '0':
                start = i
                while i < n and s[i] == '0':
                    i += 1
                group_idx = len(zero_groups)
                zero_groups.append((start, i - start))
                for j in range(start, i):
                    zero_group_map[j] = group_idx
            else:
                i += 1

        num_zero_groups = len(zero_groups)
        
        # 2. Build adjacent merge lengths array: merge_lens[i] = len(g_i) + len(g_{i+1})
        merge_lens = []
        for i in range(num_zero_groups - 1):
            merge_lens.append(zero_groups[i][1] + zero_groups[i + 1][1])
            
        st = SparseTable(merge_lens)
        
        ans = []
        
        # 3. Answer each query in O(1) time
        for l, r in queries:
            g_l = zero_group_map[l]
            g_r = zero_group_map[r]
            
            # Identify first fully internal / query-bounded zero-group indices
            start_g = g_l if (g_l != -1 and s[l] == '0') else (g_l + 1 if g_l != -1 else 0)
            if s[l] == '1':
                # find next zero-group at or after l
                # binary search or scanning from next index
                pass
            
            # Easier zero-group index boundaries for [l, r]:
            # Find the index of the first zero-group that intersects [l, r]
            first_z = -1
            if g_l != -1:
                first_z = g_l
            else:
                # search forward to next zero group
                idx = l
                while idx <= r and s[idx] == '1':
                    idx += 1
                if idx <= r:
                    first_z = zero_group_map[idx]

            last_z = -1
            if g_r != -1:
                last_z = g_r
            else:
                # search backward to previous zero group
                idx = r
                while idx >= l and s[idx] == '1':
                    idx -= 1
                if idx >= l:
                    last_z = zero_group_map[idx]

            if first_z == -1 or last_z == -1 or first_z >= last_z:
                ans.append(total_ones)
                continue

            # Effective trimmed lengths of the boundary zero-groups
            g_first_start, g_first_len = zero_groups[first_z]
            left_len = g_first_start + g_first_len - l if first_z == g_l else g_first_len

            g_last_start, g_last_len = zero_groups[last_z]
            right_len = r - g_last_start + 1 if last_z == g_r else g_last_len

            max_gain = 0

            # Case A: Exactly two adjacent zero-groups
            if first_z + 1 == last_z:
                max_gain = left_len + right_len
            else:
                # Case B: Boundaries paired with adjacent inner groups
                max_gain = max(max_gain, left_len + zero_groups[first_z + 1][1])
                max_gain = max(max_gain, right_len + zero_groups[last_z - 1][1])
                
                # Case C: Fully internal adjacent pairs between (first_z + 1) and (last_z - 1)
                if first_z + 1 <= last_z - 2:
                    max_gain = max(max_gain, st.query(first_z + 1, last_z - 2))

            ans.append(total_ones + max_gain)

        return ans
```
