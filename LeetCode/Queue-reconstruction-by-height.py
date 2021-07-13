# https://leetcode.com/problems/Queue-reconstruction-by-height/
import heapq

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []

        for person in people:
            heapq.heappush(heap, [-person[0], person[1]])

        result = []

        for _ in range(len(heap)):
            pop = heapq.heappop(heap)
            result.insert(pop[1], [-pop[0], pop[1]])

        return result
