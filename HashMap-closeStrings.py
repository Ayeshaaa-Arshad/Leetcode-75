from collections import Counter
class Solution(object):
    def closeStrings(self, word1, word2):
        if len(word1) != len(word2):
            return False

        word1_dict = Counter(word1)
        word2_dict = Counter(word2)

        if set(word1)!=set(word2):
            return False

        return sorted(word1_dict.values()) == sorted(word2_dict.values())
