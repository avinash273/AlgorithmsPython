Input = [9,6,4,2,3,5,7,0,1]


class Solution:
    def missingNumber(nums):
        nums.sort()
        if (len(nums) == 1 and nums[0] != 0):
            return nums[0] - 1
        elif (len(nums) == 1 and nums[0] == 0):
            return 1
        else:
            for i in range(len(nums) - 1):
                if (nums[i] + 1 != nums[i + 1]):
                    return nums[i] + 1
            return nums[i] + 2


print(Solution.missingNumber(Input))