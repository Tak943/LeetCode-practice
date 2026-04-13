# 1071 Greatest Common Divisor of Strings
# difficulty: Easy
# On my own ?: no

# approaching
1. iterating for laragest l reversed from larger-length word.
2. helper function 'isDevisor' 
 if len1 or len2 cannot be modded by l, how many times l is multiplied, l will never become str1 or str2.
 if it is not, l can become them by multipling some times (f1, f2).
3. when loop ends, that means devisor is not founded ("").

# What I learned
I have to pay attention to indent position.