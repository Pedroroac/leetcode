# 1. Two Sum
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        print (f'This is the length: {len(nums)}')
        setNums = set(nums)
        for number in nums:
            secondNumber = target - number
            print(f'The first number is {number} and the second: {secondNumber} and target {target}')
            if secondNumber in setNums:
                return [nums.index(number),nums.index(secondNumber)]

solution = Solution()
print (solution.twoSum([2,7,11,15],9))