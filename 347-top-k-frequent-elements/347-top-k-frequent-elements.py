
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if not nums: return []
        if len(nums) == k: return nums        
        
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key= count.get)
    
'''
T:O(NlogK)
S:O(N+k)
'''