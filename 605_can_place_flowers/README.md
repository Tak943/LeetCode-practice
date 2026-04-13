# 605 Can Place Flowers
# dificulty: Easy
# On my own: no

# approaching
[000] can be the only group to plant, so two [0] appends to flowerbed top and bottom.
pointer i iterates through flowerbed
Only if f[i-1]==0 f[i]==0 f[i+1]==0 flower can be planted.
if it is, plant f[i] and decrement n, and if n == 0 True, if not False
DONT'FORGET n==0

# What I learned
SHOULD CONSIDER n==0
return n <= 0 ...True or False  
'if' is not always necessary.