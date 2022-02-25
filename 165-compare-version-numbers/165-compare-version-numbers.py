class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(lambda x: int(x), version1.split(".")))
        version2 = list(map(lambda x: int(x), version2.split(".")))
        if len(version1) > len(version2): version2 += [0]*(len(version1)-len(version2))
        if len(version1) < len(version2): version1 += [0]*(len(version2)-len(version1))
        for v1, v2 in zip(version1, version2):
            if v1 > v2: return 1
            if v1 < v2: return -1
            if v1 == v2: continue
        return 0