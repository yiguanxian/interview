"""
#OS:windows,python3.6
@author:yi
created:Oct 5,2018
task:
	Given a 32-bit signed integer, reverse digits of an integer.
	Example 1:
	Input: 123
	Output: 321
Note:1.you should take the sign(符号) into account.
	 2.如果个位是0，翻转后最高位0不应该出现
	 3.your function return 0,if the reversed integer overflows.

my algorithm:略
	time complexity:O(log(n))
	space complexity:O(1)
"""
# coding=utf-8
class  Solutionreverse(object):
	def reverse(self,x):
		"""
		para: 
			x -- input integer,int
		return:
			reversed_int -- reversed integer,int
		"""
		if x >= 0 :
			reversed_int = int(str(x)[::-1])
			if reversed_int <= 2147483647:
				return reversed_int
			else:
				return 0 
		else:
			reversed_int = -1*int(str(-x)[::-1])
			if reversed_int >= -2147483648:
				return reversed_int
			else:
				return 0 
# test
so = Solutionreverse()
print(so.reverse(1563847412))
