"""
#OS:windows,python3.6
@author:yi
created:Sept 16,2018
task:
	Given a string, find the length of the longest substring without repeating characters.
	Input: "pwwkew"
	Output: 3
	Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring. 
important points:
	1.distinguish the difference between substring and subsquence 
	2.列表和数组的不同点：从初始化就可以看出来，列表以空表初始化，然后往后面追加值，是一种链式结构；而数组初始化是要确定shape且
	往里面填充初始值，欲改变数组只需将其中的值重置即可。区别在于一个不用固定范围，一个要固定范围；一个是开辟非连续存储空间，
	一个是开辟连续存储空间；也正是因为这些区别从而导致它们的初始化方式不同。
time complexity:
	O(n)
"""
# coding=utf-8
class Solution(object):
		def lengthOfLongestSubstring(self, s):
			"""
			obtain the longest substring without repeating characters.
			you have to distinguish the substring and subsquence 

			para:
			s -- String

			return:
			max(list1) -- the length of the longest substring without repeating characters.
			"""
			list_word = []
			list1 = []
			if len(s) == 0:
				return 0
			else:
				for i in s:
					if i in list_word:
						list1.append(len(list_word))
						list_word = list_word[list_word.index(i)+1:]
						list_word.append(i)
					else:
						list_word.append(i)
						list1.append(len(list_word))
			return max(list1)


# test
if __name__ == "__main__":
	so = Solution()
	print(so.lengthOfLongestSubstring("pwwkew"))