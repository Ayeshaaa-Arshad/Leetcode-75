from collections import Counter
class Solution(object):
    def maxOperations(self, nums, k):
        count = 0
        num_freq=Counter(nums)

        for num in nums:
            complement = k - num
            if complement in num_freq and num_freq[complement] > 0 and num_freq[num] > 0:
                if num == complement and num_freq[num] < 2:
                    continue
                count += 1
                num_freq[num] -= 1
                num_freq[complement] -= 1

        return count


