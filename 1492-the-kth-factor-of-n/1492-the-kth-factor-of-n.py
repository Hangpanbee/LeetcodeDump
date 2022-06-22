class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # sieve
        # [1,2,3,4,5,6]
        sieve = []
        opsieve = []

        for i in range(1, int(n**0.5)+1):
            if n%i==0:
                sieve.append(i)
                if (i != n//i): opsieve.append(n//i)
        
        # sieve = [1,2,3]
        # opsieve = [12,6,4]
        # k = 5
        #print(sieve, opsieve)
        if k <= len(sieve):
            return sieve[k-1]
        elif k <= (len(sieve) + len(opsieve)):
            return opsieve[(len(sieve)+len(opsieve)-k)]
        else:
            return -1