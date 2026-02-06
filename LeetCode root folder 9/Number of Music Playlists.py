# I am fking good!
# 2400 solved independently under 2hr
# the key is that to abstract the songs. treat it as if picking which does not matter, but at each position picking
# either a new song or a repeated song (the real index of such song does not matter at all, another word, the real
# identity of the song you pick does not matter at all for this process of counting playlist, you can definitely
# count the playlist just knowing the count of repeated songs and unpicked songs without knowing what songs are them)


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10 ** 9 + 7
        @cache
        def recursive(i, x):
            nonlocal n, k, goal
            if i >= goal: return 1 if x == 0 else 0
            res = 0
            # n-x - k
            if x+k < n: res += (n-x-k) * recursive(i + 1, x)  # if pick repeated one
            if x: res += x * recursive(i + 1, x - 1)  # if pick new one
            return res % mod

        return recursive(0, n)
