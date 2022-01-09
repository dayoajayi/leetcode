class TweetCounts:

    def __init__(self):
        self.frequency_lookup = {
            "minute" : 60,
            "hour" : 3600,
            "day" : 86400
        }
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        delta = self.frequency_lookup[freq]
        result = [0] * int((endTime - startTime) / delta + 1)
        
        for time in self.tweets[tweetName]:
            if startTime <= time <= endTime:
                idx = int((time - startTime) / delta)
                result[idx] += 1
        
        return result
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)


'''
T: O(N)
S: O(N)

'''