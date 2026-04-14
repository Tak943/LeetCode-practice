# 151 Reverse Words in a String
# difficulty: Medium
# On my own?: no

# approach
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

# What I learned
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