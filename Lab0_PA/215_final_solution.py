import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = nums[:k] # :k takes all the elements from the position 0 to the position k

        # to create a heap I need to provide the numbers that will compose it
        heapq.heapify(min_heap) # this thing transforms a list in a min-heap

        # the remaining numbers in the list are the remaining k ones
        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heapq.heappushpop(min_heap, nums[i])

        return min_heap[0]

if __name__ == '__main__':
    case1_leetcode = [3,2,1,5,6,4]
    case2_leetcode = [3,2,3,1,2,4,5,5,6]

    k1 = 2
    k2 = 4

    sol = Solution()
    result1 = sol.findKthLargest(case1_leetcode, k1)
    result2 = sol.findKthLargest(case2_leetcode, k2)

    print(f"First result: {result1} Second result: {result2}")