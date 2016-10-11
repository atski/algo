#see https://leetcode.com/problems/two-sum/

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        dict = {}
        for i in xrange(len(nums)):
            if not nums[i] in dict:
                dict[target - nums[i]] = i
            else:
                return [dict[nums[i]] + 1, i + 1]
        return None