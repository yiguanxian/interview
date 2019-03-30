"""
#OS:windows,python3.6
@author:yi
created:Oct 9,2018
task:
	Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
	Example 4:
	Input: 58
	Output: "LVIII"
	Explanation: C = 100, L = 50, XXX = 30 and III = 3.
	Example 5:
	Input: 1994
	Output: "MCMXCIV"
	Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
my algorithm:
	将输入整型数按照基本的罗马数值进行整除，我要知道商和余数，使用python内置函数divmod()
	time complexity:O(1)
	space complexity:O(1)
"""
class Solution:
    def intToRoman(self, num):
        """
        type num: int
        rtype: str
        """
        base_sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV"]
        base_val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4]
        result = ""
        for i in range(len(base_val)):
            quo,  res = divmod(num, base_val[i])
            if quo > 0:
                result += quo * base_sym[i]
                num = res
            if num == 0:
                return result
        if num > 0:
            result += num*"I"
        return result


so = Solution()
print(so.intToRoman(201))
