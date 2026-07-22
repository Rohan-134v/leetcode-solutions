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