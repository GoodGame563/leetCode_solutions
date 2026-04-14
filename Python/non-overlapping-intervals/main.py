from operator import itemgetter

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals = sorted(intervals, key=itemgetter(1))
        non_over = [intervals[0]]
        for el in intervals[1:]:
            if el[0] >= non_over[-1][1]:
                non_over.append(el)
        return len(intervals)-len(non_over)

print(Solution().eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]]))
