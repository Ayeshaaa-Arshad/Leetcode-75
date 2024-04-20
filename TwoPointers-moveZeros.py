class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None (the function should modify the input array in-place)
        """
        non_zero = 0  
        for current in range(len(nums)):
            if nums[current] != 0:
                nums[current], nums[non_zero] = nums[non_zero], nums[current]
                non_zero += 1
