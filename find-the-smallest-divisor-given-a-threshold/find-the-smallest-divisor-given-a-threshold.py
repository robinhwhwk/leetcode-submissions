class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # binary search
        # range: [1, max(nums)]
        def valid(divisor) -> bool:
            # return whether the divisor is valid i.e.
            # divide every number by divisor and see if they are <= threshold
            return sum([ceil(num / divisor) for num in nums]) <= threshold
        low, high = 1, max(nums)
        last_valid = -1
        while low <= high:
            mid = (low + high) // 2
            if valid(mid):
                # last_valid = mid
                high = mid - 1
            else:
                low = mid + 1
        return low