"""
#OS:windows,python3.6
@author:yi
created:Oct 5,2018
task:
	Implement atoi which converts a string to an integer.
	
	The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
	Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, 
	and interprets them as a numerical value.

	The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

	If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str 
	is empty or it contains only whitespace characters, no conversion is performed.If no valid conversion could be performed, a zero value is returned.
my algorithm:
	使用正则表达式进行匹配出带符号的数字字符，再用python内置int()函数转换
	time complexity:O(log(n))
	space complexity:O(1)

"""
# coding=utf-8
import re
class Solution(object):
    def myAtoi(self, str):
        """
        para:
        	str -- ,String
        return: 
        	output_int -- ,int
        """
        # 去除str首尾的空格和\n,\t等转义字符
        temp = str.strip()
        # 编译一个正则表达式,[+-]:匹配+或-或无
        reg = re.compile("(^[+-]?[0]?\d+)\D*")
        temp = re.findall(reg,temp)
        if not temp:
            return 0
        # temp是列表，通过join把它变成字符串
        output = "".join(temp)
        output_int = int(output)
        limit = pow(2,31)
        output_int = max(output_int,-limit)
        output_int = min(output_int,limit-1)
        return output_int


# test
so = Solution()
print(so.myAtoi("  4193 with words 145"))
