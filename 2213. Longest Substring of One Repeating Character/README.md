# 2213. Longest Substring of One Repeating Character

### Difficulty: Hard

## Description
You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.

The ith query updates the character in s at index queryIndices[i] to the character queryCharacters[i].

Return an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.

 
Example 1:


Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
Output: [3,3,4]
Explanation: 
- 1st query updates s = "bbbacc". The longest substring consisting of one repeating character is "bbb" with length 3.
- 2nd query updates s = "bbbccc". 
  The longest substring consisting of one repeating character can be "bbb" or "ccc" with length 3.
- 3rd query updates s = "bbbbcc". The longest substring consisting of one repeating character is "bbbb" with length 4.
Thus, we return [3,3,4].


Example 2:


Input: s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
Output: [2,3]
Explanation:
- 1st query updates s = "abazz". The longest substring consisting of one repeating character is "zz" with length 2.
- 2nd query updates s = "aaazz". The longest substring consisting of one repeating character is "aaa" with length 3.
Thus, we return [2,3].


 
Constraints:


	1 <= s.length <= 105
	s consists of lowercase English letters.
	k == queryCharacters.length == queryIndices.length
	1 <= k <= 105
	queryCharacters consists of lowercase English letters.
	0 <= queryIndices[i] < s.length

## Submission Details
- **Status**: Accepted
- **Runtime**: 4197
- **Memory**: 86200000
- **Language**: python3

## Code
```python3
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
```
