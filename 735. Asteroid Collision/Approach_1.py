class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for a in asteroids: 
            while result and result[-1] > 0 and a < 0:
                diff = a + result[-1]
                if diff > 0:
                    a = 0
                elif diff < 0:
                    result.pop()
                else:
                    result.pop()
                    a = 0
            if a:
                result.append(a)
        
        return result

                
            
        
            