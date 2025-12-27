class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp_x = x
        rev_x = 0

        if 0 < x < 10:
            return True

        if x < 0:
            return False

        while rev_x < x:
            if temp_x == 0:
                break
            rev_x = (rev_x * 10) + (temp_x % 10)
            temp_x = temp_x // 10

        return rev_x == x
