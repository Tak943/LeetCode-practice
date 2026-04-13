# 1768. Merge Strings Alternately
# difficulty: Easy

# approaching
1. preparing an empty array8res[].
2. iterating while two pointer(i,j) doesn't equal to word1 and word2, and then append to res[].
3. After escaping from while loop, append their rest of words to res[].
4. Using join method, connecting res[] words. 

# time complexity: O(n+m)
reason: iterating for two words' length

# space complexity: O(n)
reason: Using a new array.

# What I learned
- Even if I deal with strings, use array (res[]) and "".join(res)
- When I want to add words or numbers to array, use res.append(word[i])