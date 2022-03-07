import copy

'''
	给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
	你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

	给定 nums = [2, 7, 11, 15], target = 9
	因为 nums[0] + nums[1] = 2 + 7 = 9
	所以返回 [0, 1]
'''


class SumNumber:
    nums = []

    def sum(self, n, target):
        print("nums:", n)

        for k, v in enumerate(n):
            for i in range(k, len(n)):
                if v + n[i] == target:
                    print(k, i)


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, v in enumerate(nums):
            number = target - v
            if number in nums[i + 1:]:
                index = nums.index(number)
                return [i, index]
        return None


class Solution2:
    def toSum(self, nums, target):

        original = copy.copy(nums)
        nums.sort()

        left = 0
        right = len(nums) - 1

        for i in range(0, len(nums)):
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                return original.index(nums[left]), original.index(nums[right])


# s = SumNumber()
# s.sum([2, 8, 11, 7],9)

# ss = Solution()
# print(ss.twoSum([2, 8, 11, 7],9))

s = Solution()
print(s.twoSum([3,3], 6))
