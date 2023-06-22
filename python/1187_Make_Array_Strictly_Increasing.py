class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(arr2)
        dp = {}

        def binary_search(arr, value):
            left = 0
            right = len(arr)
            while left < right:
                mid = (left + right) // 2
                if value < arr[mid]:
                    right = mid
                else:
                    left = mid + 1
            return left

        def recursive(i, previous):
            if i == len(arr1):
                return 0
            if dp.get((i, previous)) is not None:
                return dp[(i, previous)]
            counter = float('inf')
            if arr1[i] > previous:
                counter = recursive(i + 1, arr1[i])
            idx = binary_search(arr2, previous)
            if idx < len(arr2):
                counter = min(counter, 1 + recursive(i + 1, arr2[idx]))
            dp[(i, previous)] = counter
            return counter
        result = recursive(0, -1)
        return result if result < float('inf') else -1
