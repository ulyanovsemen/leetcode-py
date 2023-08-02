nums = [2, 11, 7, 15]
target = 9
# nums = [3, 3]
# target = 6


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}

        for y in range(len(nums)):

            if nums[y] in d:
                return [d[nums[y]], y]

            d[target - nums[y]] = y


solution = Solution()
print(solution.twoSum(nums, target))
