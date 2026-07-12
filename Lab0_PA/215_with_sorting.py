class kth_largest_element:
    def findKthLargest(self, nums:list[int], k: int) -> int:
        nums.sort()

        return nums[len(nums) - k]
        # return nums[-k]

if __name__ == '__main__':
    case1_leetcode = [3,2,1,5,6,4]
    case2_leetcode = [3,2,3,1,2,4,5,5,6]

    k1 = 2
    k2 = 4

    sol = kth_largest_element()
    result1 = sol.findKthLargest(case1_leetcode, k1)
    result2 = sol.findKthLargest(case2_leetcode, k2)

    print(f"First result: {result1} Second result: {result2}")