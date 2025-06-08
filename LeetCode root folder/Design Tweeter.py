# so boring ass I just quit

class User:
    id_ = -1
    followers = {}
    followees = {}
    newsFeed = []
    posts = []

    def __init__(self, id_):
        self.id_ = id_

    def addFollower(self, follower):
        self.followers[follower.id_] = follower

    def removeFollower(self, follower):
        del self.followers[follower.id_]

    def addFollowee(self, followee):
        self.followees[followee.id_] = followee

    def removeFollowee(self, followee):
        del self.followees[followee.id_]

    def addNewsFeed(self, news):
        self.newsFeed.append(news)

    def addPost(self, post):
        self.post.append(post)

    def updateNewsFeed1(self, newsFeed, posts):
        # add all the news from posts to the news feed
        for time, post in posts:
            heapq.heappush([time, post])

    def updateNewsFeed2(self, newsFeed, posts):
        # delete all the news from newsFeed that exists in posts
        for time, post in newsFeed:
            if


class Twitter:
    users = {}

    def __init__(self):
        self.users = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:  # init the new user if doesn't exist
            self.users[userId] = User(userId)

        user = self.users[userId]

        for follower in user.followers.values():  # update news feed for all followers
            follower.addNewsFeed(tweetId)

        user.addNewsFeed(tweetId)  # update news feed for user themself
        user.addPost(tweetId)  # update post for user themself

    def getNewsFeed(self, userId: int) -> List[int]:
        user = self.users[userId]
        return list(user.newsFeed)

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)

        follower = self.users[followerId]
        followee = self.users[followeeId]

        followee.addFollower(follower)
        follower.addFollowee(followee)

        followee.updateNewsFeed1(followee.newFeed,
                                 follower.posts)  # refresh the top ten most recently posted news feed for the followee

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)

        follower = self.users[followerId]
        followee = self.users[followeeId]

        followee.removeFollower(follower)
        follower.removeFollowee(followee)

        followee.updateNewsFeed2(followee.newFeed,
                                 follower.posts)  # refresh the top ten most recently posted news feed for the followee

