class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        i = 0
        count = 0
        min_length = float('inf')
        best_str = ""

        for j in range(len(s)):
            if s[j] == '1':
                count += 1
            
            while count == k:
                current_len = j - i + 1
                current_str = s[i:j+1]
                
                if current_len < min_length:
                    min_length = current_len
                    best_str = current_str
                elif current_len == min_length:
                    if current_str < best_str:
                        best_str = current_str
                        
                if s[i] == '1':
                    count -= 1
                i += 1
                
        return best_str