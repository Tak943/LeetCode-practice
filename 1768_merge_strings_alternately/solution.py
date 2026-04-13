'''
Result is inputed into array and joined with empty string "" at the end.
Using pointer i for word1 and pointer j for word2, iterating for length word1 and word2.
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = []
        while i != len(word1) and j != len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)
