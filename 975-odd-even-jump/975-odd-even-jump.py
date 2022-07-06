class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        NLaE = len(A)*[-1]
        NLE = len(A)*[-1]

        stack = []
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                NLaE[stack.pop()] = i
            stack.append(i)
        
        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                NLE[stack.pop()] = i
            stack.append(i)
        
        o = [False]*len(A)
        e = [False]*len(A)
        o[-1] = True
        e[-1] = True
        #print(o, e, NLE, NLaE)
        for i in range(len(A)-2,-1,-1):
            if NLE[i] != -1:
                e[i] = o[NLE[i]]
            if NLaE[i] != -1:           
                o[i] = e[NLaE[i]]
             
        return sum(o)
        