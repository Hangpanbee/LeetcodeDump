class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        """
        0, 1, 2 = -4, 4, 0
        0, 1 = -5, 10, -5
        
        0, 1, 2, 3, 4, 5, 6 = 10, -3, 20, -17, -6, -4
        -> 20, 10, -3, -4, -6, -17
        -> [25, 10, 10] , [-1,-2,-25,-7,-10]
        -> unoptimal transactions: 4. optimal transactions: 3
        """
        people = [0]*12
        for payer, debter, amount in transactions:
            people[payer] -= amount
            people[debter] += amount
        payers, debters = [], []
        debtLeft = 0
      
        for person, amount in enumerate(people):
            if amount > 0:
                payers.append(amount)
                debtLeft += amount
            elif amount < 0:
                debters.append(-amount)
            elif amount == 0: continue
        
        #print(payers, debters, debtLeft)
       
        memoize = {}
        def dp(payer, debtLeft):
            # -> 0, 4 -> 1, 2 -> 1, 1
            # -> 0, 3
            # -> 1, 2
            # -> 2, 0
            #print(payer, debtLeft)
            if debtLeft == 0: return 0
            elif payer == len(payers): return 9999999
            #elif (payer, debtLeft) in memoize:
                #return memoize[(payer, debtLeft)]
            
            transactions = 100000
            # maybe easier to use a map here
            currPayer, nxtPayer = 10000, 10000
            for p, a in enumerate(debters):
        
                if a == 0:
                    continue
                prevPayer = payers[payer]
                if (payers[payer] > a):
                    debters[p] = 0
                    payers[payer] -= a
                    currPayer = 1 + dp(payer, sum(debters))
                    debters[p] = a
                    payers[payer] = prevPayer
                elif (payers[payer] <= a):
                    debters[p] = a - payers[payer]
                    payers[payer] = 0
                    nxtPayer = 1 + dp(payer+1, sum(debters))
                    #print("NXT", payer+1, sum(debters), 1+dp(payer+1, sum(debters)))
                    #print(nxtPayer, "STATE", payer, debtLeft)
                    debters[p] = a
                    payers[payer] = prevPayer
                #print(debters, payers)
                transactions = min(currPayer, nxtPayer, transactions)
            memoize[(payer, debtLeft)] = transactions
            #print("STATE END", payer, debtLeft, transactions)
            return transactions
        return dp(0, debtLeft)