# number one boring bullshit so far, I am avoiding it and I would not do it if not because someone posted the
# dictionary from digit to word in comment

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return 'Zero'
        mp = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion"
        }

        def helper(s):
            while s and s[0] == '0': s = s[1:]
            if not s: return ''
            l = len(s)
            if l == 3:
                res = mp[int(s[0])] + ' Hundred '
                x = int(s[1:])
                if x == 0: return res[:-1]
                if x in mp: res += mp[x]
                else: res += mp[int(s[1] + '0')] + ' ' + mp[int(s[2])]
            elif l == 2:
                x = int(s)
                if x in mp: res = mp[x]
                else: res = mp[int(s[0] + '0')] + ' ' + mp[int(s[1])]
            else:
                res = mp[int(s[0])]
            return res

        s = str(num)
        x = 1
        ans = []
        for i in range(len(s) - 1, -1, -3):
            cr = s[max(0, i - 2):i + 1]
            extra = (' ' + mp[x]) if x != 1 else  ''
            res = helper(cr)
            if res: ans.append(res + extra)
            x *= 1000

        ans = ans[::-1]
        # print(ans)
        return ' '.join(ans)