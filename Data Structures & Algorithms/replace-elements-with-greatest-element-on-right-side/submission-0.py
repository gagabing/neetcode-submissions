class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        
        right_max = len(arr) * [-1]
        for i in range(len(arr)-2, -1, -1):
            right_max[i] = max(right_max[i+1], arr[i+1])
        
        return right_max
