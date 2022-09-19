class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dup_map = collections.defaultdict(list)
        
        
        for path in paths:
            sub_paths = path.split(" ")
            root = sub_paths[0]
            for i in range(1, len(sub_paths)):
                sb = sub_paths[i]
                content = sb.split("(")
                if len(content) > 1: dup_map[content[1]].append(root+"/"+content[0])
        
        ans = []
        for content, path in dup_map.items():
            if len(path) > 1: ans.append(path)
        
        return ans
            