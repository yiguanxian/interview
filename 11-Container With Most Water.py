"""
#OS:windows,python3.6
@author:yi
created:Oct 9,2018
task:
	Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
	n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
	Find two lines, which together with x-axis forms a container, such that the container contains the most water.
my algorithm:
	思想是贪心原理，先从底边最大的情况考虑，计算最大面积后，此时要将底边长度减1，只需要将杯壁较短的那一边移动一个单位距离，
	得到的解必定优于杯壁较长那边移动的情况。这样保证每次移动都得到的是局部最优解。
	T O(n)
	S O(1)

"""
# coding=utf-8
class Solution(object): 
	def maxArea(self, height):
		"""'
		parameters:
			height -- ,list
		return:
			maxarea -- ,integer
		"""
		left_boundary,right_boundary,maxarea,tmp = 0,len(height)-1,0,0
		while(left_boundary < right_boundary):
		    tmp = min(height[left_boundary],height[right_boundary])*(right_boundary-left_boundary)
		    maxarea = max(tmp,maxarea)
		    if min(height[left_boundary],height[right_boundary]) == height[left_boundary]:
		        left_boundary+=1
		    else:
		        right_boundary-=1
		return maxarea


# test
so = Solution()
print(so.maxArea([1,8,6,2,5,4,8,3,7]))