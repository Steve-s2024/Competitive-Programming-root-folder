# credit for neetcode. sorted set solution, feels like the question is designed to
# match this data structure, also I don't know how to install the
# sortedcontainers module: 30%
from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.mp = defaultdict(SortedSet)
        self.idxMp = {}
        self.ratings = ratings
        self.cuisines = cuisines
        n = len(foods)
        for i in range(n):
            self.mp[cuisines[i]].add((-ratings[i], foods[i]))
            self.idxMp[foods[i]] = i

    def changeRating(self, food: str, newRating: int) -> None:
        i = self.idxMp[food]
        cuisine = self.cuisines[i]
        prevRating = self.ratings[i]
        self.ratings[i] = newRating
        self.mp[cuisine].remove((-prevRating, food))
        self.mp[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.mp[cuisine][0][1]


# max heap solution, so boring and nerve-racking just to consider everything
# : 49%
from collections import defaultdict
import heapq

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.mp = {}
        self.idxMp = {}
        self.ratings = ratings
        self.cuisines = cuisines

        mp = self.mp
        idxMp = self.idxMp

        n = len(foods)
        for i in range(n):
            if cuisines[i] not in mp:
                maxheap = []
                heapq.heapify(maxheap)
                mp[cuisines[i]] = maxheap
            heapq.heappush(mp[cuisines[i]], (-ratings[i], foods[i]))
            idxMp[foods[i]] = i

    def changeRating(self, food: str, newRating: int) -> None:
        mp = self.mp
        idxMp = self.idxMp
        ratings = self.ratings
        cuisines = self.cuisines

        i = idxMp[food]
        ratings[i] = newRating
        cuisine = cuisines[i]

        heapq.heappush(mp[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        mp = self.mp
        idxMp = self.idxMp
        ratings = self.ratings
        while True:
            rating, food = mp[cuisine][0]
            i = idxMp[food]
            if ratings[i] != -rating:
                heapq.heappop(mp[cuisine])
            else:
                break
        tmp = []
        maxRating = -mp[cuisine][0][0]
        # print(mp, cuisine)
        # print(ratings)
        while mp[cuisine] and -mp[cuisine][0][0] == maxRating:
            rating, food = heapq.heappop(mp[cuisine])
            i = idxMp[food]
            if ratings[i] == maxRating:
                tmp.append((rating, food))

        for t in tmp:
            heapq.heappush(mp[cuisine], t)
        return min([e[1] for e in tmp])



# brute force with nested hash map: 5%
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.idxMp = {}
        self.mp = {}
        self.ratings = ratings
        self.cuisines = cuisines

        mp = self.mp
        idxMp = self.idxMp
        n = len(foods)
        for i in range(n):
            if cuisines[i] not in mp:
                mp[cuisines[i]] = defaultdict(set)
            mp[cuisines[i]][ratings[i]].add(foods[i])
            idxMp[foods[i]] = i

    def changeRating(self, food: str, newRating: int) -> None:
        mp = self.mp
        idxMp = self.idxMp
        ratings = self.ratings
        cuisines = self.cuisines

        i = idxMp[food]
        prevRating = ratings[i]
        ratings[i] = newRating
        cuisine = cuisines[i]

        mp[cuisine][prevRating].remove(food)
        if len(mp[cuisine][prevRating]) == 0:
            mp[cuisine].pop(prevRating)
        mp[cuisine][newRating].add(food)

    def highestRated(self, cuisine: str) -> str:
        mp = self.mp
        maxRating = max(mp[cuisine].keys())
        return min(mp[cuisine][maxRating])

