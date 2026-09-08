from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_1 = Counter()
        list_2 = Counter()
        for char in s:
            list_1[char] += 1

        for char in t:
            list_2[char] += 1

        return list_1 == list_2
        