class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
    
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        start, end, pivot = -1, 0, len(nums) - 1
        kthLargest = None
        
        def quickSelect(start, end, pivot):
            nonlocal kthLargest
            
            while end < pivot:
                if end == pivot - 1:
                    nums[start+1], nums[pivot] = nums[pivot], nums[start+1]
                    if start + 1 == k:
                        kthLargest = nums[k]
                        break
                    elif start + 1 < k:
                        quickSelect(start+1, end, end+1)
                    else:
                        quickSelect(-1, 0, start)
                elif nums[end] < nums[pivot] and start < end:
                    start += 1
                    if nums[start] > nums[pivot]:
                        nums[start], nums[end] = nums[end], nums[start]
                else:
                    end += 1
                    
                
            
        quickSelect(start, end, pivot)
        return kthLargest'''