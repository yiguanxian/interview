"""
#OS:windows,python3.6
@author:yi
created:Oct 8,2018
task:
	Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
	Example 2:
	Input: -121
	Output: false
	Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
	Example 3:
	Input: 10
	Output: false
	Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
algorithm:
	the negative values must be not palindrome numbers.built function int() will ignore first position 0.you can try judge the palindrome numbers
	using the definition by slice of list.
	time complexity:O(log(n))
	space complexity:O(1)
"""
# coding=utf-8
class Solution:
    def isPalindrome(self, x):
        """
        type x: int
        rtype: bool
        """
        if x < 0:
            return False
        else:
            x = str(x)
            if x == x[::-1]:
                return True
            else:
                return False


# test
so = Solution()
print(so.isPalindrome(-121))            
