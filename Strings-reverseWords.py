class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        splitWords=s.split()

        result=splitWords[::-1]

        return ' '.join(result)

s=Solution()
print(s.reverseWords("a good   example"))
