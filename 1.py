class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):  # loops through nums
            num1 = nums[i]  # assign the number to a variable
            for j in range(len(nums)):  # loop again to get the rest of numbers
                if j == i:  # skip if i and j are the same index
                    continue
                else:  # if not, continue
                    num2 = nums[j]  # if num1 and num2 add up to target, print
                    if (num1 + num2) == target:
                        return [i, j]
