class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        #pay atention to // division
        ansDict = {'0': "01", '1': '10'}
        def helper(n, k):
            if k == 1: return "0"
            # set the current environement to keep track of the vairable that was sent down the tree
            LookingFor = helper(n-1, ceil(k/2))
            if k%2==0: return ansDict[LookingFor][1]
            elif k%2==1: return ansDict[LookingFor][0]
        return helper(n, k)
        