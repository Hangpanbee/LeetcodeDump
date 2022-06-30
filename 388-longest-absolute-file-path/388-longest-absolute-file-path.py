class Solution:
    def lengthLongestPath(self, input: str) -> int:
        #input = input.replace(" ", "_")
      
        splittedInput = input.split("\n")
        #print(len(splittedInput[-1]))
        # [dir, \tsubdir, \t\tfile1.ext, \t\tsubsubdir1, \tsubdir2, \t\tsubsubdir2, \t\t\tfile2.ext]
        
        st = []
        maxLenPath = 0
        for i, file in enumerate(splittedInput):
            fileSplitted = file.split("\t")
            fileName, fileLevel = fileSplitted[-1], len(fileSplitted)
            isTextFile = "." in fileName
            pathLen = len(fileName)
            while st and st[-1][1] >= fileLevel:
                st.pop()
            if st: pathLen += st[-1][2] + 1
                
            if isTextFile:    
                maxLenPath = max(maxLenPath, pathLen)
            else:
                st.append((fileName, fileLevel, pathLen))
        return maxLenPath
        