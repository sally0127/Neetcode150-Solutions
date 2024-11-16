**Design Twitter Feed**
-

🔗 Link: Design Twitter Feed

💡 Difficulty: Medium

🛠️ Topics: 資料結構設計(Data Structure Design)、最大堆應用(Max-Heap Application)、多功能需求設計(Multi-Function Requirement Design)'
效率優化(Efficiency Optimization)、邊界條件處理(Edge Case Handling)、模擬真實場景(Simulating Real-World Scenarios)

=========================================

Implement a simplified version of Twitter which allows users to post tweets, follow/unfollow each other, and view the 10 most recent tweets within their own news feed.

Users and tweets are uniquely identified by their IDs (integers).

Implement the following methods:

    ．Twitter() Initializes the twitter object.
    
    ．void postTweet(int userId, int tweetId) Publish a new tweet with ID tweetId by the user userId. You may assume that each tweetId is unique.
    
    ．List<Integer> getNewsFeed(int userId) Fetches at most the 10 most recent tweet IDs in the user's news feed. Each item must be posted by users who the user is following or by the user themself. Tweets IDs should be ordered from most recent to least recent.
    
    ．void follow(int followerId, int followeeId) The user with ID followerId follows the user with ID followeeId.
    
    ．void unfollow(int followerId, int followeeId) The user with ID followerId unfollows the user with ID followeeId.

Example 1:

Input:
["Twitter", "postTweet", [1, 10], "postTweet", [2, 20], "getNewsFeed", [1], "getNewsFeed", [2], "follow", [1, 2], "getNewsFeed", [1], "getNewsFeed", [2], "unfollow", [1, 2], "getNewsFeed", [1]]

Output:
[null, null, null, [10], [20], null, [20, 10], [20], null, [10]]

Explanation:
Twitter twitter = new Twitter();
twitter.postTweet(1, 10); // User 1 posts a new tweet with id = 10.
twitter.postTweet(2, 20); // User 2 posts a new tweet with id = 20.
twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].
twitter.getNewsFeed(2);   // User 2's news feed should only contain their own tweets -> [20].
twitter.follow(1, 2);     // User 1 follows user 2.
twitter.getNewsFeed(1);   // User 1's news feed should contain both tweets from user 1 and user 2 -> [20, 10].
twitter.getNewsFeed(2);   // User 2's news feed should still only contain their own tweets -> [20].
twitter.unfollow(1, 2);   // User 1 follows user 2.
twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].

Constraints:

．1 <= userId, followerId, followeeId <= 100

．0 <= tweetId <= 1000

=======================================================

**UMPIRE Method:**

**Understand**

問題需求：

1.推文 (Post Tweet)
    
    ．用戶可以發送推文，推文用 tweetId 唯一標識。
    
    ．推文應保存到某種數據結構中以便檢索。

2.新聞推送 (Get News Feed)
    
    ．對於某個 userId，返回該用戶及其所關注的用戶所發布的最新 10 條推文。
    
    ．推文需要按時間順序排序（從最新到最舊）。

3.關注與取消關注 (Follow/Unfollow)
    
    ．一個用戶可以關注其他用戶。
    
    ．用戶也可以取消對其他用戶的關注。

關鍵點：

．每條推文和用戶有唯一 ID。

．推文排序需要按時間順序，可能需要設計某種結構來支持排序。

．關注關係影響新聞推送的內容。

初步需求理解：

要設計以下幾個方法：

    ．postTweet(userId, tweetId)：發送推文。
    
    ．getNewsFeed(userId)：獲取最新 10 條推文。
    
    ．follow(followerId, followeeId)：關注某個用戶。
    
    ．unfollow(followerId, followeeId)：取消關注某個用戶。

**Match**

關聯概念：

1.圖 (Graph)

    ．關注/取消關注可以被看作是用戶之間的有向圖，其中節點是用戶，邊是關注關係。

2.優先隊列/堆 (Priority Queue/Heap)

    ．提取最新的 10 條推文可以用優先隊列來實現，確保推文按時間順序排列。

3.哈希表 (Hash Table)

    ．保存用戶的推文和關注關係需要用到哈希表來高效檢索。

**Plan**

1.數據結構設計：

    ．tweets：一個哈希表，key 是 userId，value 是該用戶的推文列表（按照發送順序保存 tweetId 和時間戳）。
    
    ．follows：一個哈希表，key 是 userId，value 是該用戶關注的用戶集合。
    
    ．timestamp：全局變量，用於記錄推文的時間戳，確保可以按時間排序。

2.主要方法實現：

．postTweet(userId, tweetId)：

    ．將該推文添加到 tweets[userId] 中，記錄時間戳。

．getNewsFeed(userId)：

    ．找到該用戶和其關注用戶的所有推文。

    ．使用最大堆提取最新的 10 條推文。

．follow(followerId, followeeId)：

    ．在 follows[followerId] 中添加 followeeId。

．unfollow(followerId, followeeId)：

    ．從 follows[followerId] 中移除 followeeId。

**Implement**

see solution.py

**Review**

．檢查代碼是否符合要求：

  ．確保正確實現了所有方法：

    ．postTweet 能正確地將推文插入使用者的推文列表中。
    
    ．getNewsFeed 能按要求返回最多 10 條最新推文。
    
    ．follow 和 unfollow 能正確管理用戶之間的關注關係。

  ．邏輯是否正確處理了關鍵邊界條件：

    ．如果用戶沒有推文或沒有關注任何人，getNewsFeed 是否返回空列表。
    
    ．確保用戶不能關注自己。
    
    ．如果取消關注的人從未被關注，程式是否會崩潰。

  ．驗證程式是否滿足所有測試用例。

**Evaluate**

．時間複雜度：

    ．postTweet：O(1)，因為插入推文到 deque 是常數時間操作。
    
    ．getNewsFeed：最多需要處理用戶和他關注者的推文，複雜度為 O(n⋅k+mlogm)，其中 n 是關注者數量，k 是每人推文數量，m 是總推文數。
    
    ．follow 和 unfollow：O(1)，因為集合的操作是常數時間。

．空間複雜度：

    ．推文儲存在 deque 中，總共需要 O(u⋅k) 空間，u 是用戶數，k 是每用戶推文數量。
    
    ．關注關係儲存在 set 中，總共需要 O(f) 空間，f 是所有關注關係的數量。

**Topic**

1.資料結構設計：

    ．使用 deque 存儲用戶的推文。
    
    ．使用 set 管理用戶之間的關注關係。

2.最大堆應用：

    ．用 heapq 管理推文的時間戳，實現高效提取最新推文。

3.多功能需求設計：

    ．涉及多種操作的整合設計，例如發推、查看動態、關注/取消關注。

4.效率優化：

    ．對方法進行時間與空間複雜度的優化，確保系統能處理大量數據。

5.邊界條件處理：

    ．例如自己關注自己、無推文時的情況。

6.模擬真實場景：

    ．設計模擬像 Twitter 這類真實應用的場景，測試對需求分析和實現的能力。

**簡化邏輯說明**

1.初始化三個條件：

    ．用戶推文（tweets）： 使用 defaultdict(deque) 來存儲每個用戶的推文。
        
    ．用戶關注關係（follows）： 使用 defaultdict(set) 來管理每個用戶的關注對象。
        
    ．全局時間戳（timestamp）： 用來追踪每篇推文的發佈時間，確保推文可以按時間排序。

2.發推文：

    ．將新推文附帶當前時間戳存入用戶的推文列表（tweets[userId]）。
        
    ．使用 deque.appendleft()，確保最新的推文總是位於最前面。

3.獲取動態（news feed）：

    ．包括自己的推文，以及所有已追蹤用戶的推文。
    
    ．使用最大堆（heapq）將所有推文按照時間戳排序。
    
    ．最後提取最新的 10 條推文。

4.追蹤用戶（follow）：

    ．將被追蹤的用戶 followeeId 加入當前用戶 followerId 的關注集合中。
    
    ．確保用戶無法追蹤自己（用 if followerId != followeeId 避免）。

5.取消追蹤（unfollow）：

    ．從用戶的關注集合中移除指定的用戶 followeeId。
    
    ．使用 discard()，避免當目標用戶不存在時觸發錯誤。

這幾點總結得很好，就是這樣的邏輯！整體設計的核心在於用資料結構（deque 和 set）來高效管理推文和關注關係，並利用 heapq 快速獲取最新動態。


