class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = list(s)
        i = 0

        for char in s:
            if char == '*':
                i -= 1
            else:
                result[i] = char
                i += 1
        return ''.join(result[:i])
    