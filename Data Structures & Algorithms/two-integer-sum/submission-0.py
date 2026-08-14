class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            component = target - num
            if component in seen:
                return [seen[component], i]
            seen[num] = i            