# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    # Implementation of QuickSort
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def sort(left, right):
            if left >= right:
                return
            pivot = pairs[right]
            k = left
            for i in range(left, right):
                if pairs[i].key < pivot.key:
                    # swap
                    pairs[i], pairs[k] = pairs[k], pairs[i]
                    k += 1
            # move pivot
            pairs[right], pairs[k] = pairs[k], pairs[right]
            sort(left, k-1)
            sort(k+1, right)
            
        sort(0, len(pairs)-1)
        return pairs


        