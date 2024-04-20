class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1] * len(nums)
        result[0] = 1

        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]

        product = nums[len(nums) - 1]
        for i in range(len(nums) - 1, 0, -1):
            result[i - 1] = result[i - 1] * product
            product *= nums[i - 1]
        return result

sol = Solution()
sol.productExceptSelf([-1,1,0,-3,3])
