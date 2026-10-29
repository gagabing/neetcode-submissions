class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, k = 0, 0
        s = len(nums) - 1
        while i <= s:
            if nums[i] == val:
                nums[i] = nums[s]
                nums[s] = val
                s -= 1
            else:
                i += 1
                k += 1
        return k