class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}

        for key in nums:
            if key in nums_dict:
                return True

            nums_dict[key] = 1

        return False
