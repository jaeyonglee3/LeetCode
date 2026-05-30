class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = collections.defaultdict(list)  # userId : tweets list
        self.following = collections.defaultdict(set)  # userId : following userIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        # tweets are tuples: (timestamp, tweetId)
        new_tweet = (-self.timestamp, tweetId)
        self.timestamp += 1
        self.tweets[userId].append(new_tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        # pull the latest tweet from each user userId follows (incl themself)
        # into a max heap and heappop the latest 10
        result = []
        tweet_heap = []
        curr_tweet_index = -1
        
        users_set = self.following[userId].copy()
        users_set.add(userId)

        for user in users_set:
            user_tweets = self.tweets[user]
            if not user_tweets:
                continue
            
            index = len(user_tweets) - 1  # grab latest tweet
            latest_tweet = user_tweets[index]
            timestamp, tweetId = latest_tweet[0], latest_tweet[1]
            
            heapq.heappush(tweet_heap, [timestamp, tweetId, user, index - 1])
        
        while tweet_heap and len(result) < 10:
            timestamp, tweetId, userId, index = heapq.heappop(tweet_heap)
            result.append(tweetId)

            if index >= 0:
                timestamp, tweetId = self.tweets[userId][index]
                heapq.heappush(tweet_heap, [timestamp, tweetId, userId, index - 1])
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)