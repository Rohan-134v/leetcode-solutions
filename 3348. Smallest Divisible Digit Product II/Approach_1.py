import math
from functools import lru_cache

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp_t = t
        for p in [2, 3, 5, 7]:
            while temp_t % p == 0:
                temp_t //= p
        if temp_t > 1:
            return "-1"

        @lru_cache(None)
        def get_shortest(r):
            if r == 1: 
                return ""
            best = None
            for d in range(2, 10):
                nr = r // math.gcd(r, d)
                if nr != r: 
                    cand = get_shortest(nr)
                    if cand is not None:
                        cand = "".join(sorted(str(d) + cand))
                        if best is None:
                            best = cand
                        else:
                            if len(cand) < len(best):
                                best = cand
                            elif len(cand) == len(best) and cand < best:
                                best = cand
            return best
        
        shortest_t = get_shortest(t)
        zero_idx = num.find('0')
        if zero_idx == -1:
            zero_idx = len(num)
        reqs = [t]
        for i in range(min(len(num), zero_idx)):
            reqs.append(reqs[-1] // math.gcd(reqs[-1], int(num[i])))
            
        if zero_idx == len(num) and reqs[-1] == 1:
            return num
            
        for i in range(min(len(num) - 1, zero_idx), -1, -1):
            current_req = reqs[i]
            start_d = int(num[i]) + 1
            
            for d in range(start_d, 10):
                nr = current_req // math.gcd(current_req, d)
                short_s = get_shortest(nr)
                
                rem_len = len(num) - 1 - i
                if short_s is not None and len(short_s) <= rem_len:
                    return num[:i] + str(d) + "1" * (rem_len - len(short_s)) + short_s
                    
        req_len = max(len(num) + 1, len(shortest_t))
        return "1" * (req_len - len(shortest_t)) + shortest_t