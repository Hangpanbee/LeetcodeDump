class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        
        for i in path:
            if i == '' or i == '.':
                continue
            elif i == '..':
                if len(stack):
                    stack.pop()
            else:
                stack.append(i)
         
        return "/" + "/".join(stack)