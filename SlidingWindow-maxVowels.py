class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start=0
        end=0
        maxFreq=0
        maxZeros=0
        size=len(nums)

        while(end<size):
            if nums[end]==0:
                maxZeros+=1

            while(maxZeros>k):
                if nums[start]==0:
                    maxZeros-=1
                start=start+1

            maxFreq=max(maxFreq,end-start+1)
            end+=1

        return maxFreq
    