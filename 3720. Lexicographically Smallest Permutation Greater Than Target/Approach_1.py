from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = Counter(s)
        
        best_branch_idx = -1
        best_branch_char = None
        
        n, m = len(s), len(target)
        
        for i in range(min(n, m) + 1):
            if i == m:
                if n > m: 
                    best_branch_idx = i
                    best_branch_char = None
                break
            
            t_char = target[i]
            
            branch_char = None
            for char in sorted(count.keys()):
                if char > t_char and count[char] > 0:
                    branch_char = char
                    break
            
            if branch_char:
                best_branch_idx = i
                best_branch_char = branch_char
            
            if count[t_char] > 0:
                count[t_char] -= 1
            else:
                break
                
        if best_branch_idx == -1:
            return ""  
            
        result = []
        for i in range(best_branch_idx):
            result.append(target[i])
        rem_count = Counter(s)
        for i in range(best_branch_idx):
            rem_count[target[i]] -= 1
        if best_branch_char is not None:
            result.append(best_branch_char)
            rem_count[best_branch_char] -= 1

        for char in sorted(rem_count.keys()):
            result.extend([char] * rem_count[char])
            
        return "".join(result)