class Leaderboard:

    def __init__(self):
        self.scores = collections.defaultdict(int)
        '''
        Time: O(1)
        Space: O(1)
        '''
        
    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score
        '''
        Time: O(1)
        Space: O(1)
        '''

    def top(self, K: int) -> int:
        return sum(heapq.nlargest(K, self.scores.values()))
        '''
        Time: O(K * Log N), where N is the total number of players
        Space: O(1)
        '''
        

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0
        

        
        

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)