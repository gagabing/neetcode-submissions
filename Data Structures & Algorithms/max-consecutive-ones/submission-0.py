class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = 0
        niter = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                niter += 1
            else:
                niter = 0
            n = max(n, niter)
        return n