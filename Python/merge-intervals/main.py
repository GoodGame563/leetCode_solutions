from operator import itemgetter
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key= itemgetter(0))
        new = [intervals[0]]
        for i in range(1, len(intervals)):
            if new[-1][1] >= intervals[i][0]:
                new[-1] = [new[-1][0],intervals[i][1] if intervals[i][1]>new[-1][1] else new[-1][1]]
                continue
            new.append(intervals[i])
        return new
        
print(Solution().merge(intervals =[[1,3],[2,6],[8,10],[15,18]]))
