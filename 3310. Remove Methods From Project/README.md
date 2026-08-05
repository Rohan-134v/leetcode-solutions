# 3310. Remove Methods From Project

### Difficulty: Medium

## Description
You are maintaining a project that has n methods numbered from 0 to n - 1.

You are given two integers n and k, and a 2D integer array invocations, where invocations[i] = [ai, bi] indicates that method ai invokes method bi.

There is a known bug in method k. Method k, along with any method invoked by it, either directly or indirectly, are considered suspicious and we aim to remove them.

A group of methods can only be removed if no method outside the group invokes any methods within it.

Return an array containing all the remaining methods after removing all the suspicious methods. You may return the answer in any order. If it is not possible to remove all the suspicious methods, none should be removed.

 
Example 1:


Input: n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]]

Output: [0,1,2,3]

Explanation:



Method 2 and method 1 are suspicious, but they are directly invoked by methods 3 and 0, which are not suspicious. We return all elements without removing anything.


Example 2:


Input: n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]]

Output: [3,4]

Explanation:



Methods 0, 1, and 2 are suspicious and they are not directly invoked by any other method. We can remove them.


Example 3:


Input: n = 3, k = 2, invocations = [[1,2],[0,1],[2,0]]

Output: []

Explanation:



All methods are suspicious. We can remove them.


 
Constraints:


	1 <= n <= 105
	0 <= k <= n - 1
	0 <= invocations.length <= 2 * 105
	invocations[i] == [ai, bi]
	0 <= ai, bi <= n - 1
	ai != bi
	invocations[i] != invocations[j]

## Submission Details
- **Status**: Accepted
- **Runtime**: 310
- **Memory**: 106888000
- **Language**: python3

## Code
```python3
from typing import List
import collections

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v in invocations:
            graph[u].append(v)
            
        suspicious = set([k])
        queue = collections.deque([k])
        
        while queue:
            curr = queue.popleft()
            for neighbor in graph[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))
                
        return [i for i in range(n) if i not in suspicious]
```
