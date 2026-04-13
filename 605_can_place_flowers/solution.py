'''
[000] can be the only group to plant, so two [0] appends to flowerbed top and bottom.
pointer i iterates through flowerbed
Only if f[i-1]==0 f[i]==0 f[i+1]==0 flower can be planted.
if it is, plant f[i] and decrement n, and if n == 0 True, if not False
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) + 1):
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
                f[i] = 1
                n -= 1
        return n <= 0