from collections import Counter


# class Solution(object):
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        num = 0
        num49 = 0

        roman49KEY = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        roman49INST = {"IV": 0, "IX": 0, "XL": 0, "XC": 0, "CD": 0, "CM": 0}
        roman49NUM = {"IV": 0, "IX": 0, "XL": 0, "XC": 0, "CD": 0, "CM": 0}

        ALL49 = "IVIXXLXCCDCM"
        newS = s

        if any("IV" or "IX" or "XL" or "XC" or "CD" or "CM" in s):

            for i in range(len(s) - 1):
                roman49 = s[i] + s[i + 1]

                if roman49 in ("IV", "itIX", "XL", "XC", "CD", "CM"):
                    roman49INST[roman49] += 1
                    newS = newS.replace(roman49, "")

            for i in range(0, len(ALL49) - 1, 2):
                sum49 = ALL49[i] + ALL49[i + 1]
                roman49NUM[sum49] += roman49KEY[sum49] * roman49INST[sum49]

            num49 = sum(roman49NUM.values())

        if newS != "":
            for i in newS:

                romanKEY = {
                    "I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000,
                }
                romanINST = {"I": 0, "V": 0, "X": 0, "L": 0, "C": 0, "D": 0, "M": 0}
                romanNUM = {"I": 0, "V": 0, "X": 0, "L": 0, "C": 0, "D": 0, "M": 0}

                for i in newS:
                    romanINST[i] += 1

                for i in "IVXLCDM":
                    romanNUM[i] += romanKEY[i] * romanINST[i]

            num = sum(romanNUM.values())

        self = num + num49

        return self


x = "IV"

Solution().romanToInt(x)


# loop through string and store each instance of roman num in dict
#        roman = {IVXLCDM}
