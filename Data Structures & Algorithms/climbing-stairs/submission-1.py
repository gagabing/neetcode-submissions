class Solution:
    def __init__(self):
        self.lookup = {}
        
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        if (n-1) not in self.lookup:
            self.lookup[n-1] = self.climbStairs(n-1)
        if (n-2) not in self.lookup:
            self.lookup[n-2] = self.climbStairs(n-2)
        return self.lookup[n-1] + self.lookup[n-2]

        