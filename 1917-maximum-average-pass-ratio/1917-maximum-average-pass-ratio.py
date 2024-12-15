import heapq

class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        # Create a max-heap based on the potential increase in pass ratio
        max_heap = []
        
        # Populate the heap with the initial classes and their potential increases
        for passi, totali in classes:
            # Calculate the current pass ratio and the potential increase
            current_ratio = passi / totali
            # Calculate the increase in pass ratio if we add one extra student
            increase = (passi + 1) / (totali + 1) - current_ratio
            # Push the negative of the increase to create a max-heap
            heapq.heappush(max_heap, (-increase, passi, totali))
        
        # Assign extra students
        for _ in range(extraStudents):
            # Get the class with the maximum increase in pass ratio
            increase, passi, totali = heapq.heappop(max_heap)
            increase = -increase  # Convert back to positive
            # Assign one extra student to this class
            passi += 1
            totali += 1
            # Recalculate the new increase and push it back into the heap
            new_increase = (passi + 1) / (totali + 1) - (passi / totali)
            heapq.heappush(max_heap, (-new_increase, passi, totali))
        
        # Calculate the final average pass ratio
        total_pass_ratio = 0
        for _, passi, totali in max_heap:
            total_pass_ratio += passi / totali
        
        return total_pass_ratio / len(classes)
