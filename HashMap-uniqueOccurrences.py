from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr_dict = Counter(arr)
        occurences = set()

        for values in arr_dict.values():
            occurences.add(values)

        return len(arr_dict.values()) == len(occurences)


sol = Solution()
print(sol.uniqueOccurrences([1, 2, 2]))
