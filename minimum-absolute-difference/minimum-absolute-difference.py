class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minDiff = float("inf")
        arr.sort()
        output = []
        
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            minDiff = min(minDiff, diff)
        
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == minDiff:
                output.append([arr[i-1],arr[i]])
        return output