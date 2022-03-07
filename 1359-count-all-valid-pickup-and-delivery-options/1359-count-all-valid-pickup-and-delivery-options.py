import functools

class Solution:
    def countOrders(self, n: int) -> int:
        total = functools.reduce(lambda x, y: x*(y), [*range(1,n*2+1)] )
        
        return total // 2**n % (10**9+7)