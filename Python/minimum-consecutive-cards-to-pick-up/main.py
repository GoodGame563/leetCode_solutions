class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        min_cons = float("+inf")
        see = {}
        for i, c in enumerate(cards):
            if c in see:
                min_cons = min(min_cons, i - see[c]+1)          
            see[c] = i
        return -1 if min_cons == float("+inf") else min_cons
    
print(Solution().minimumCardPickup(cards = [3,4,2,3,4,7]))

print("Hello from minimum-consecutive-cards-to-pick-up!")
