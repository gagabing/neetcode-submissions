class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #return nums + nums
        n = len(nums)
        ans = (2 * n) * [0]
        for i in range(n):
            ans[i] = nums[i]
            ans[n+i] = nums[i]
        return ans