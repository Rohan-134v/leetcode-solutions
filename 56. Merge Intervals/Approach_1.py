class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
            
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            last_added_interval = res[-1]
            current_interval = intervals[i]
            
            if current_interval[0] <= last_added_interval[1]:
                last_added_interval[1] = max(last_added_interval[1], current_interval[1])
            else:
                res.append(current_interval)
                
        return res