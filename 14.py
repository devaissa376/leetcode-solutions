class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        curr_index = 0  # for indexing through each item in list
        first_word = strs[0]

        LCP = ""

        for i in range(
            len(min(strs, key=len))
        ):  # only loop num times as length of shortest word
            how_many = (
                0  # how many elements in array have same nth letter as first word
            )

            for i in strs:  # loop through all items in array
                if (
                    i[curr_index] == first_word[curr_index]
                ):  # if array element nth index = that of first word

                    how_many += 1  # then add 1 to how_many

            if how_many < len(strs):  # if how_many is less than the length of the array
                break  # then it's not part of the longest common prefix, break
            else:
                LCP += first_word[
                    curr_index
                ]  # if how_many is equal to length of array, append that letter to LCP

            curr_index += 1  # move onto next letter

        return LCP  # return longest common prefix


x = ["dog", "racecar", "car"]
Solution().longestCommonPrefix(x)
