class Twitter:

    def __init__(self):
        self.count = -1
        self.tweet_map = defaultdict(list)  # userId -> list of [(count, tweetIds)]
        self.follow_map = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        self.follow_map[userId].add(userId)  # make the user follow themself
        for uid in self.follow_map[userId]:
            if uid in self.tweet_map:
                # only get uid's most recent tweet
                index = len(self.tweet_map[uid]) - 1
                count, tweetId = self.tweet_map[uid][index]

                # push 4 values, the count, tweetid, uid of person who posted it, and next index
                heapq.heappush(min_heap, [count, tweetId, uid, index - 1])
        
        while min_heap and len(res) < 10:
            # stops if min_heap is empty, or if len(res) >= 10, whichever happens first
            count, tweetId, uid, index = heapq.heappop(min_heap)
            res.append(tweetId)

            if index >= 0:
                # that index tells us the next tweet belonging to uid that we can add
                # to the feed. add it to the heap using heappush
                count, tweetId = self.tweet_map[uid][index]
                heapq.heappush(min_heap, [count, tweetId, uid, index - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getnews_feed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)