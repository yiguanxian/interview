"""
#OS:windows,python3.6
@author:yi
created:Oct 8,2018
task:
	Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
	Example 3:
	Input:
	s = "ab"
	p = ".*"
	Output: true
	Explanation: ".*" means "zero or more (*) of any character (.)".
	Example 4:
	Input:
	s = "aab"
	p = "c*a*b"
	Output: true
	Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
	Example 5:
	Input:
	s = "mississippi"
	p = "mis*is*p*."
	Output: false
my algorithm:
	using re.match() 
	return True ro False of result
	time complexity:O(log(n))
	space complexity:O(1)

special attention:
	.表示匹配任意字符
	*表示匹配0次或多次前一元素
	.*表示以贪婪方式匹配任意(包括0)长度字符串，直到下一个匹配元素,注意似乎多个模式元素在一起的时候其表达的含义不一定就是合并思路的含义，这就要求多多
	练习，多见，多记忆，而后自然就通顺了。
"""
# coding=utf-8
import re
class Solution(object):
    def isMatch(self, s, p):
        """
        type s: str
        type p: str
        rtype: bool
        """
        pattern = re.match(p,s)
        if pattern != None:
            return pattern.group() == s
        return False


# test
so = Solution()
print(so.isMatch("mississippi", "mis*is*ip*."))