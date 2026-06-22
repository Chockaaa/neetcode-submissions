class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_1 = {}
        word_2 = {}

        if len(s) != len(t):
            return False

        for idx in range(len(s)):
            if s[idx] in word_1:
                word_1[s[idx]] += 1
            else:
                word_1[s[idx]] = 1
            
            if t[idx] in word_2:
                word_2[t[idx]] += 1
            else:
                word_2[t[idx]] = 1

        for key, value in word_1.items():
            if key not in word_2 or int(value) != word_2[key]:
                return False
        
        return True



