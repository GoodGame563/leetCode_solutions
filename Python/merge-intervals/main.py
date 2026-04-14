class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        new = [intervals[0]]
        for i in range(1, len(intervals)):
            if new[-1][1] >= intervals[i][0]:
                last_el = new.pop()
                new.append([last_el[0],intervals[i][1] if intervals[i][1]>last_el[1] else last_el[1]])
                continue
            new.append(intervals[i])
        return new
        
print(Solution().merge(intervals =[[1,4],[5,6]]))
