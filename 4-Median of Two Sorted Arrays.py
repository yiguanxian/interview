"""
#OS:windows,python3.6
@author:yi
created:Sept 21,2018
task:
	There are two sorted arrays nums1 and nums2 of size m and n respectively.
	Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
	You may assume nums1 and nums2 cannot be both empty.
	Example:
	nums1 = [1, 3]
	nums2 = [2]
	The median is 2.0
about time complexity :
	if there are not input parameters:
		time complexity is constant level ，it equals O(1)

	if there are input parameters and input data scale equals n:
		time complexity is logarithm level, it equals O(log(n))
		such as this task

	if there are input parameters,input data scale equals n and looping n times:
		time complexity is linear level,it equals O(n)
time complextiy:
	O(logn)
"""
# coding=utf-8
class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		find the median in two sorted arrays

		paras:
			nums1 -- one array,list of python
			nums2 -- another one array,list of python

		return:
			median -- median of two array
		"""
		l = sorted(nums1 + nums2)
		length = len(l) 
		if length % 2 == 0:
			median = (l[(length // 2) - 1] + l[(length // 2)]) / 2.0
		else:
			median = l[(length // 2)]
		return median


if __name__ == "__main__":
	so = Solution()
	print(so.findMedianSortedArrays([1.0,2.0,4.0], [3.0,9.0]))