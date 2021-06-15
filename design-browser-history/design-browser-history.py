class BrowserHistory:

    def __init__(self, homepage: str):
        self.currpage = 0
        self.history = [homepage]

    def visit(self, url: str) -> None:
        while len(self.history)-1 != self.currpage:
            self.history.pop()
        self.history.append(url)
        self.currpage += 1
        

    def back(self, steps: int) -> str:

        if steps > self.currpage:
            self.currpage = 0
            return self.history[0]
        else: 
            self.currpage -= steps
            return self.history[self.currpage]

    def forward(self, steps: int) -> str:
        if len(self.history)-self.currpage-1 < steps:
            self.currpage = len(self.history)-1
            return self.history[-1]
        else:
            self.currpage += steps
            return self.history[self.currpage]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)