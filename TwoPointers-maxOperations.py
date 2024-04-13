from collections import Counter

class Solution(object):
    def maxOperations(self, nums, k):
        count = 0
        numFreq=Counter(nums)

        for num in nums:
            complement = k - num
            if complement in numFreq and numFreq[complement] > 0 and numFreq[num] > 0:
                if num == complement and numFreq[num] < 2:
                    continue
                count += 1
                numFreq[num] -= 1
                numFreq[complement] -= 1

        return count