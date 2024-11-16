import heapq
from collections import defaultdict,deque
from typing import List

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(deque) # 用戶推文 {userId: deque([tweet1, tweet2, ...])}
        self.follows = defaultdict(set)  # 用戶關注關係 {userId: {followeeId1, followeeId2, ...}}
        self.timestamp = 0 # 全局時間戳
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendleft((self.timestamp,tweetId)) # 最新推文放到前面
        self.timestamp += 1  # 更新時間戳

        
    def getNewsFeed(self, userId: int) -> List[int]:
        # 初始化最大堆
        max_heap = []
        # 添加自己的推文
        for tweet in self.tweets[userId]:
            heapq.heappush(max_heap,(-tweet[0],tweet[1])) # 時間戳取負數以實現最大堆
        # 添加關注者的推文
        for followeeId in self.follows[userId]:
            for tweet in self.tweets[followeeId]:
                heapq.heappush(max_heap,(-tweet[0],tweet[1]))

        # 提取最新的 10 條推文
        news_feed = []
        while max_heap and len(news_feed) < 10:
            news_feed.append(heapq.heappop(max_heap)[1])

        return news_feed
       
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId: # 防止用戶關注自己
            self.follows[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)  # 使用 discard 防止 KeyError
