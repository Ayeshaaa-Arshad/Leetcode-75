class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        firstMin = float('inf')
        secondMin = float('inf')

        for num in nums:
            if num <= firstMin:
                firstMin = num
            elif num <= secondMin:
                secondMin = num
            else:
                return True

        return False
