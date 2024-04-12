class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        substr = s[:k]
        maxLen = 0
        currentLen = sum(substr.count(vowel) for vowel in "aeiouAEIOU")

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        for i in range(k, len(s)):
            maxLen = max(maxLen, currentLen)
            if s[i] in vowels:
                currentLen += 1
            if s[i - k] in vowels:
                currentLen -= 1

        maxLen = max(maxLen, currentLen)
        return maxLen