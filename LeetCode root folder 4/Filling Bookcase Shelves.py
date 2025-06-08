# stuck on testcase:
# books = [[9,9],[5,4],[3,1],[1,5],[7,3]], selfWidth = 10
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        @cache
        def recursive(i, width):
            nonlocal n, shelfWidth
            if i >= n:
                return 0, 0
            w, h = books[i]
            if width+w <= shelfWidth:
                tot, hei = recursive(i+1, width+w)
                maxH = max(hei, h)
                res = tot

                tot, hei = recursive(i+1, 0)

                if tot+hei+h < res+maxH:
                    maxH = h
                    res = tot+hei
                print(i, res, maxH)
                return res, maxH
            else:
                return float('inf'), float('inf')

        tot, hei = recursive(0, 0)
        return tot+hei