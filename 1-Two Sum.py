"""
#OS:windows,python3.6
@author:yi
created:Sept 12,2018
task:
	Given an array(list) of integers, return indices of the two numbers such that they add up to a specific target.
	You may assume that each input would have exactly one solution, and you may not use the same element twice.
	Example:
	Given nums = [2, 7, 11, 15], target = 9,
	Because nums[0] + nums[1] = 2 + 7 = 9,
	return [0, 1].
algorithm：
	creat a dictionary which key is value of list and value is index of list
	choose any a value of list and then judge whether the difference between target and value chosed in list
	list of python has method index() which can find index according to the value.
time complexity:
	O(n)
"""
# coding=utf-8
class Solution(object):
	"""Solution"""
	def twoSum(self, nums, target):
		"""
		instance function in order to return indexs of target

		parameters:
			nums -- given a list of int,list of integers.
			target -- target number,int.

		return:
			indexs list of two factors included in nums,list of integers
		"""
		if len(nums) <= 1:
			return False
		buff_dict = {}
		for i in range(len(nums)):
			if nums[i] in buff_dict:
				return [buff_dict[nums[i]], i]
			else:
				buff_dict[target - nums[i]] = i


# test solution
if __name__ == "__main__":
	solu = Solution()
	index_list = solu.twoSum([0,3,7,9],10)
	print(index_list)