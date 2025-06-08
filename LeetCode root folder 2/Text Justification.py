# fking murdered the question, dare to challenge me?!!
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = []
        total = 0
        res = []
        for word in words:
            nextLength = total + len(word) + len(line)
            if nextLength > maxWidth:

                emptys = maxWidth - total
                gaps = len(line)-1
                if not gaps:
                    diff = maxWidth - (total + len(line)-1)
                    string = ' '.join(line) + ' '*diff
                    res.append(string)
                else:
                    remain = emptys % gaps
                    increment = emptys // gaps
                    a = ' '*(increment+1)
                    b = ' '*increment
                    str1 = a.join(line[:remain+1])
                    str2 = b.join(line[remain+1:])
                    string = b.join([str1, str2])
                    res.append(string)
                line = [word]
                total = len(word)
            else:
                line.append(word)
                total += len(word)
        diff = maxWidth - (total + len(line)-1)
        string = ' '.join(line) + ' '*diff
        res.append(string)
        # print(res)
        return res

# only left justified
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = []
        total = 0
        res = []
        for word in words:
            nextLength = total + len(word) + len(line)
            if nextLength > maxWidth:
                diff = maxWidth - (total + len(line)-1)
                string = ' '.join(line) + ' '*diff
                res.append(string)
                line = [word]
                total = len(word)
            else:
                line.append(word)
                total += len(word)
        diff = maxWidth - (total + len(line)-1)
        string = ' '.join(line) + ' '*diff
        res.append(string)
        # print(res)
        return res