class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k, i, j = m + n - 1, m - 1, n - 1
        while k >= 0:
            if i >= 0 and n > 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            elif j >= 0:
                nums1[k] = nums2[j]
                j -= 1
            k = k - 1
