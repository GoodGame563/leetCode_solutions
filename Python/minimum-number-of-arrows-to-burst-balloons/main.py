

class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points = sorted(points)
        new_arr = []
        last_range = points[0]
        for point in points[1:]:
            if last_range[1] >= point[0]:
                last_range = [point[0], min(last_range[1], point[1])]
                continue
            new_arr.append(last_range)
            last_range = point
        new_arr.append(last_range)
        return len(new_arr)
    
points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
print(Solution().findMinArrowShots(points))
print("Hello from minimum-number-of-arrows-to-burst-balloons!")
