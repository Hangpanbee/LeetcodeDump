class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        seen = {}
        ans = []
        for name in names:
            modified = name
            suffix = 0 if name not in seen else seen[name]
            while modified in seen:
                suffix += 1
                modified = f'{name}({suffix})'
            seen[name] = suffix
            seen[modified] = 0
            ans.append(modified)
            
        return ans