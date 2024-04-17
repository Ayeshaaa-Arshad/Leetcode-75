class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        kidWithMaxCandies=max(candies)
        resultantArray=[False]*len(candies)

        for i in range (len(candies)):
            if candies[i]+extraCandies>=kidWithMaxCandies:
                resultantArray[i]=True

        return resultantArray

sol=Solution()
print(sol.kidsWithCandies([2,3,5,1,3],3))


