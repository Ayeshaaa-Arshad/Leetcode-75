class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        size = len(flowerbed)
        if n == 0:
            return True

        for i in range(size):
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i - 1] == 0) and (i == size - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
        return False if n > 0 else True
