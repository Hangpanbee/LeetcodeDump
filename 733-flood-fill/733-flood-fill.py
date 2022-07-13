class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = collections.deque()
        FILLED_COLOR = image[sr][sc]
        if FILLED_COLOR == color: return image
        
        q.append((sr,sc))
        image[sr][sc] = color
        r, c = len(image), len(image[0])
        while q:
            currR, currC = q.popleft()
            
            for nxtR, nxtC in ((currR+1, currC),(currR-1, currC),(currR,currC-1),(currR, currC+1)):
                if 0 <= nxtR < r and 0 <= nxtC < c and image[nxtR][nxtC] == FILLED_COLOR:
                    q.append((nxtR, nxtC))
                    image[nxtR][nxtC] = color
                    
        return image