class Solution:
    def checkDivisibility(self, n: int) -> bool:
        product, total = 1, 0
        a = n
        while a > 0:
            temp = a % 10
            total += temp
            product *= temp
            a = a // 10
        
        print(total + product)
        
        return True if n % (total + product) == 0 else False