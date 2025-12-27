class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        romanKEY = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        sum = 0

        for i in range(len(s) - 1):

            if romanKEY[s[i]] < romanKEY[s[i + 1]]:
                sum -= romanKEY[s[i]]
            else:
                sum += romanKEY[s[i]]

        sum += romanKEY[s[-1]]
        return sum


x = "III"
Solution().romanToInt(x)
