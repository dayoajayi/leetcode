class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff, currentDiff = float("inf"), float("inf")
        result = []
    
        for i in range(1, len(arr)):
            currentDiff = arr[i] - arr[i -1]
            minDiff = min(minDiff, currentDiff)
            
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == minDiff:
                result.append([arr[i-1], arr[i]])
                
        return result
