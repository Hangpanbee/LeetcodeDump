class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        can the dependencies has duplicate value?
        what if the target value isnt in range?
        what if there is a deadend edge?
        
        topological sort will handle case where there is a cycle, and case where there is no start
        read the question more carefully
        
        runttime: m*k = n = len(allUNiqueIngredients)
        
        """
        ingredToRecipes = collections.defaultdict(list)
        inEdge = {}
        countRecipes = len(recipes)
        supplies = {supply: True for supply in supplies}
        
        for i in range(countRecipes):
            for ii, ingre in enumerate(ingredients[i]): #O(n)
                ingredToRecipes[ingre].append(recipes[i])
                if ingre not in inEdge:
                    inEdge[ingre] = 0
            inEdge[recipes[i]] = len(ingredients[i])
            
       
        q = collections.deque()
        for recipe, lenIngre in inEdge.items(): #O(n)
            if lenIngre == 0 and recipe in supplies:
                q.append(recipe)
        
        #topological Sort: O(n)
        allRecipes = [] 
        while q:
            recipe = q.popleft()
            
            for nxtRecipe  in ingredToRecipes[recipe]:
                inEdge[nxtRecipe] -= 1
                if inEdge[nxtRecipe] == 0:
                    allRecipes.append(nxtRecipe)
                    q.append(nxtRecipe)
                
        return allRecipes