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
        
        while len(result) < 10:
            users_set = self.following[userId]
            users_set.add(userId)

            for user in self.following[userId]:
                user_tweets = self.tweets[user]
                if len(user_tweets) < abs(curr_tweet_index):
                    continue
                
                curr_tweet = user_tweets[curr_tweet_index]
                heapq.heappush(tweet_heap, curr_tweet)
            
            curr_tweet_index -= 1
            if not tweet_heap:
                return result
            
            result.append(heapq.heappop(tweet_heap)[1])
        
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