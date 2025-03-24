class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        def merge_meetings(meetings):
            if not meetings:
                return []

            # Step 1: Sort meetings based on start time
            meetings.sort()

            ans = []
            start = meetings[0][0] 
            end = meetings[0][1]

            for meeting in meetings[1:]:  
                if meeting[0] <= end:
                    end = max(end, meeting[1])
                else:
                    ans.append([start, end])
                    start, end = meeting[0], meeting[1]

            ans.append([start, end])
            return ans
        
        # Step 1: Merge overlapping meetings
        merged_meetings = merge_meetings(meetings)

        # Step 2: Calculate the total blocked days
        blocked_days = sum(end - start + 1 for start, end in merged_meetings)

        # Step 3: Compute the available days
        return days - blocked_days
            
                
        