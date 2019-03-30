"""
#OS:windows,python3.6
@author:yi
created:Sept 29,2018
task:
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)
    Example 1:
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
my algorithm:
    we have fund the rule about every line character index of output:(n denoted numRows)
        first line index sequence:0 ,(0)+(2n-2),(0+2n-2)+(2n-2)...
        last line index sequence:n-1,(n-1)+(2n-2),(n-1+2n-2)+(2n-2),...
        other line index sequence(such as seconde line):1,(1)+(2n-2-2row),(1)+(2n-2),(1+2n-2)+(2n-2-2row),(1+2n-2)+(2n-2)...
        这里整个Z型转换，行中相邻两个字母在S中的索引之差就只有两种取值可能：2n-2,和2n-2-2row,每行字母它们在s中的索引存在如下特点：
        1.第一行和最后一行相邻索引差均为2n-2,其中n为numRows
        2.中间任何行先是相邻字母索引差为2n-2-2row，再是与当前字母的左相邻的左相邻字母索引差为2n-2,后面的依次重复，其中row为当前行索引
	time complexity:O(len(s)+nRows)
	space complexity:O(1)
"""


# coding=utf-8
class Solution:
    def convert(self, s, nRows):
        if nRows==1:
            return s
        if len(s)<=1:
            return s
        # 第一种索引差取值，包括第一行和最后一行相邻字母索引差和中间行当前字母左相邻的左相邻字母的索引差
        index_diff1=2*nRows-2
        result=[]
        for row in range(nRows):
            # 第二种索引差，只含在中间行相邻字母的索引差
            index_diff2 = index_diff1 - 2*row
            # 用i来记录第row行从左往右每一个字母的索引，其初始值为row
            i=row
            while i<len(s):
                result.append(s[i])
                if row!=0 and row!=nRows-1 and i+index_diff2<len(s):
                    result.append(s[i+index_diff2])
                i+=index_diff1
        return "".join(result)
so= Solution()
print(so.convert("PAYPALISHIRING",4))