'''
 l             r     l     r     l   r
[I,c,e,C,r,e,A,m]    IceCreAm   AceCreIm   
while loop until left conflicts right.
if s[left] in vowel, stop moving. otherwise moving forward.
if s[right] in vowel, stop moving. otherwise moving backward. 
and swap each other.

DON'T FORGET POINTER MOVE when swaping
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

        left, right = 0, len(s) - 1
        while left < right:
            if s_list[left] not in vowels: # if true, move false, stop
                left += 1
            elif s_list[right] not in vowels: # if true, move false, stop
                right -= 1
            else: # both false, found vowels in both side
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        return "".join(s_list)