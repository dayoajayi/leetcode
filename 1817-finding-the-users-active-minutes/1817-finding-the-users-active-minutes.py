class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        UAMS = defaultdict(set)
        ans = [0] * k
        
        for ID, time in logs:
            UAMS[ID].add(time)
        for UAM in UAMS.values():
            ans[len(UAM)-1] += 1
        return ans
        
'''
T: O(N)
S: O(N+K)
'''