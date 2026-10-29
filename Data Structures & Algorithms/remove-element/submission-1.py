class Solution:    
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        s = len(nums) - 1
        while i <= s:
            if nums[i] == val:
                nums[i] = nums[s]
                s -= 1
            else:
                i += 1
        return i