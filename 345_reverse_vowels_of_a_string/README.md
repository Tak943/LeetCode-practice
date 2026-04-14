# 345 Revers Vowels of a Strings
# difficulty: Easy
# On my own?: no

# approaching
 l             r     l     r     l   r
[I,c,e,C,r,e,A,m]    IceCreAm   AceCreIm   
while loop until left conflicts right.
if s[left] in vowel, stop moving. otherwise moving forward.
if s[right] in vowel, stop moving. otherwise moving backward. 
and swap each other.

DON'T FORGET POINTER MOVE when swaping

# What I learned
for i in range():
    if statementA:
        processA
    elif statementB:
        processB
    else statementC:
        processC

if stA is true, process processA and rest of processes are not implemented. After that, continue for loop straightly.

strings cannot access directly, like if strigs = "abc", it is not be able to do like strigs[0] = c. immutable