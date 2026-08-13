from typing import List

class Node:
    def __init__(self, size=1, char=''):
        self.size = size
        self.pref_len = 1
        self.pref_char = char
        self.suff_len = 1
        self.suff_char = char
        self.max_len = 1

class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.tree = [Node() for _ in range(4 * self.n)]
        self.s = list(s)
        self.build(0, 0, self.n - 1)

    def merge(self, left: Node, right: Node) -> Node:
        res = Node(left.size + right.size)
        res.pref_char = left.pref_char
        res.suff_char = right.suff_char

        res.pref_len = left.pref_len
        if left.pref_len == left.size and left.pref_char == right.pref_char:
            res.pref_len += right.pref_len

        res.suff_len = right.suff_len
        if right.suff_len == right.size and right.suff_char == left.suff_char:
            res.suff_len += left.suff_len
            
        res.max_len = max(left.max_len, right.max_len)
        if left.suff_char == right.pref_char:
            res.max_len = max(res.max_len, left.suff_len + right.pref_len)
            
        return res

    def build(self, node: int, start: int, end: int):
        if start == end:
            self.tree[node] = Node(1, self.s[start])
            return
        mid = (start + end) // 2
        self.build(2 * node + 1, start, mid)
        self.build(2 * node + 2, mid + 1, end)
        self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def update(self, node: int, start: int, end: int, idx: int, char: str):
        if start == end:
            self.tree[node] = Node(1, char)
            self.s[idx] = char
            return
        
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node + 1, start, mid, idx, char)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, char)
            
        self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def get_max(self) -> int:
        return self.tree[0].max_len


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        tree = SegmentTree(s)
        ans = []
        
        for char, idx in zip(queryCharacters, queryIndices):
            tree.update(0, 0, len(s) - 1, idx, char)
            ans.append(tree.get_max())
            
        return ans