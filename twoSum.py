# 1. Two Sum
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #print (f'This is the length: {len(nums)}')
        numsLength = len(nums)
        for x in range(numsLength):
            for y in range (x+1,numsLength):
                #print (f'The x is: {x} and y is: {y}')
                result = nums[x] + nums[y]
                #print (f'The result should be: {result}')
                if result == target:
                    return [x,y]

solution = Solution()
print (solution.twoSum([2,7,11,15],9))