# Design a simplified version of Twitter where users can post tweets, follow/unf
# ollow another user and is able to see the 10 most recent tweets in the user's ne
# ws feed. Your design should support the following methods: 
# 
#  
#  
#  postTweet(userId, tweetId): Compose a new tweet. 
#  getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news
#  feed. Each item in the news feed must be posted by users who the user followed 
# or by the user herself. Tweets must be ordered from most recent to least recent.
#  
#  follow(followerId, followeeId): Follower follows a followee. 
#  unfollow(followerId, followeeId): Follower unfollows a followee. 
#  
#  
# 
#  Example:
#  
# Twitter twitter = new Twitter();
# 
# // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5);
# 
# // User 1's news feed should return a list with 1 tweet id -> [5].
# twitter.getNewsFeed(1);
# 
# // User 1 follows user 2.
# twitter.follow(1, 2);
# 
# // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6);
# 
# // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# // Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# 
# twitter.getNewsFeed(1);
# 
# // User 1 unfollows user 2.
# twitter.unfollow(1, 2);
# 
# // User 1's news feed should return a list with 1 tweet id -> [5],
# // since user 1 is no longer following user 2.
# twitter.getNewsFeed(1);
#  
#  Related Topics 堆 设计 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
import collections
import datetime
import time
from typing import List
import heapq

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followers = collections.defaultdict(set)
        self.twitters = collections.defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if len(self.twitters[userId]) == 10:
            self.twitters[userId].remove(0)
        self.twitters[userId].append((tweetId, datetime.datetime.now()))

    def cmp(self, a, b):


    def getNewsFeed(self, userId: int) -> List[int]:

        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        heap = []
        return None
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followers[followerId].remove(followeeId)



a = collections.defaultdict(list)
a[1].append(3)
a[1].append(3)
print(a[1])
a = datetime.datetime.now()
time.sleep(1)
b = datetime.datetime.now()
print(a < b)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# leetcode submit region end(Prohibit modification and deletion)
