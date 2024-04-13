class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=0
        end=0
        maxFreq=0
        NumZeros=0


        while end<len(nums):
            if nums[end]==0:
                NumZeros+=1
            while(NumZeros>1):
                if nums[start]==0:
                    NumZeros-=1
                start=start+1
            maxFreq=max(maxFreq,end-start+1)
            end+=1
        return maxFreq-1
    