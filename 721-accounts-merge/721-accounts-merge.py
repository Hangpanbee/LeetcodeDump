class DisjointSet:
    def __init__(self, accounts):
        self.root = list(range(len(accounts)))
        self.rank = [0] * len(accounts)
     
    
    def find(self, acc):
        while acc != self.root[acc]:
            acc = self.root[acc]
        return acc

    def union(self, acc1, acc2):
        acc1Parent = self.find(acc1)
        acc2Parent = self.find(acc2)
        if acc1Parent == acc2Parent: return acc1Parent
        
        acc1Rank = self.rank[acc1Parent]
        acc2Rank = self.rank[acc2Parent]
        if acc1Rank >= acc2Rank:
            self.root[acc2] = self.root[acc1]
            self.rank[acc1Parent] += self.rank[acc2Parent]
            return self.root[acc2]
        else:
            self.root[acc1] = self.root[acc2]
            self.rank[acc2Parent] += self.rank[acc1Parent]
            return self.root[acc1]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        DS = DisjointSet(accounts)
        seen = {}
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                if accounts[i][j] in seen:
                    seen[accounts[i][j]] = DS.union(seen[accounts[i][j]], DS.find(i))
                else: seen[accounts[i][j]] = i
        
        
        ans = collections.defaultdict(list)
        for email, owner in seen.items():
            ans[DS.find(owner)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]