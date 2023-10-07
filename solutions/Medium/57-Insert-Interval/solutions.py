        idx, n = 0, len(intervals)
        output = []
        
        while idx < n and new_start > intervals[idx][0]:
            output.append(intervals[idx])
            idx += 1
            
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
            output[-1][1] = max(output[-1][1], new_end)
        new_start, new_end = newInterval
        else:
[List[int]]:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List
        
        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx += 1
            if output[-1][1] < start:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], end)
        return output
        