'''
iterating for laragest l reversed from larger-length word.
helper function 'isDevisor' 
# if len1 or len2 cannot be modded by l, how many times l is multiplied, l will never become str1 or str2.
if it is not, l can become them by multipling some times (f1, f2).
when loop ends, that means devisor is not founded ("").
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        
        def isDevisor(l):
            if len1 % l or len2 % l:
                return False
            f1, f2 = len1 // l, len2 // l
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        for l in range(min(len1, len2), 0, -1):
            if isDevisor(l):
                return str1[:l]
        return ""