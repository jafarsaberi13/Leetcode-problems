class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer1 = 0
        pointer2 = 0
        while pointer1 < len(nums):
            if nums[pointer1] == 0:
                pointer1 += 1
            else:
                if nums[pointer2] == 0:
                    nums[pointer2], nums[pointer1] = nums[pointer1], nums[pointer2]
                    pointer1 += 1
                    if (pointer2 + 1) < len(nums) and nums[pointer2 + 1] == 0:
                        pointer2 += 1
                    else:
                        while (pointer2 + 1) < len(nums) and nums[pointer2 + 1] != 0:
                            pointer2 += 1
                else:
                    pointer1 += 1
                    pointer2 += 1

        