'''
strip() # remove \n, " ", \t from head and tail. 
lstrip() # remove from left.
rstrip() # remove from right.

split("?") # split strings into lists with ?.
s = "orange, banana, apple"
s.split(",") # [orange, "banana", "apple"]

slice
(start: stop: step)
[::-1] # from end to start backfard in -1
[:-1] # from start to indent-"-1" (==s[end]) step forward in +1
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        splited_s = s.split()
        reversed_s = splited_s[::-1]
        return " ".join(reversed_s) 

