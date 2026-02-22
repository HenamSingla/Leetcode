from typing import List
import heapq
class Twitter:
    def __init__(self):
        self.time=0
        self.follows={}
        self.tweets={}

    def postTweet(self,userId:int,tweetId:int)-> None:
        if userId not in self.tweets:
            self.tweets[userId]=[]
        self.tweets[userId].append((self.time, tweetId))
        self.time+=1

    def getNewsFeed(self,userId:int)-> List[int]:
        followees = set()
        if userId in self.follows:
            followees = set(self.follows[userId])
        followees.add(userId)

        heap = []
        for uid in followees:
            if uid in self.tweets and len(self.tweets[uid]) > 0:
                idx = len(self.tweets[uid]) - 1
                t, tid = self.tweets[uid][idx]
                heapq.heappush(heap, (-t, tid, uid, idx))

        res = []
        while heap and len(res) < 10:
            neg_t, tid, uid, idx = heapq.heappop(heap)
            res.append(tid)
            idx -= 1
            if idx >= 0:
                t, tid2 = self.tweets[uid][idx]
                heapq.heappush(heap, (-t, tid2, uid, idx))

        return res

    def follow(self,followerId:int,followeeId:int)-> None:
        if followerId==followeeId:
            return
        if followerId not in self.follows:
            self.follows[followerId]=set()
        self.follows[followerId].add(followeeId)

    def unfollow(self,followerId:int,followeeId:int)-> None:
        if followerId in self.follows:
            if followeeId in self.follows[followerId]:
                self.follows[followerId].remove(followeeId)
