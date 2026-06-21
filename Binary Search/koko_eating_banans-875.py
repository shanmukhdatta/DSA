## comment that gives the question statment :
## Leetcode 875. Koko Eating Bananas
## Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
## The guards have gone and will come back in h hours. 
## Koko can decide her bananas-per-hour eating speed of k. 
## Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
## If the pile has less than k bananas, she eats all the bananas in that pile and will not eat any more bananas during this hour. 
## Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return. 
## Return the minimum integer k such that she can eat all the bananas within h hours.


import math
class solution:
    def minEatingSpeed(self, piles : list[int], h: int) -> int:
        # possiblities aray of K is [1,max(piles)]
        l,r = 1,max(piles)
        k = r

        while l <=r:
            m = (l+r)//2
            hours = 0

            for p in piles:
                hours += math.ceil(p/m) # 
            if hours <=h:
                k = min(k,m)
                r = m-1
            else:
                l = m+1
        return k

