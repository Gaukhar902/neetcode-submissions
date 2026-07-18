class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0

        for num in range(len(nums)):
            if nums[num] != val:
                nums[write] = nums[num]
                write += 1
        return write