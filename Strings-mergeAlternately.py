class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        a_ptr=0
        b_ptr=0
        result=""
        while(a_ptr<len(word1) and b_ptr<len(word2)):
            result+=word1[a_ptr]+word2[b_ptr]
            a_ptr+=1
            b_ptr+=1

        if a_ptr !=len(word1):
            result+=word1[a_ptr:len(word1)+1]
        else:
            result +=word2[b_ptr:len(word2) + 1]
        return result

sol=Solution()
print(sol.mergeAlternately("ab","pcd"))