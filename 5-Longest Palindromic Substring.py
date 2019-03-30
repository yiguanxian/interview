"""
#OS:windows,python3.6
@author:yi
created:Sept 27,2018
task:
	Given a string s, find the longest palindromic substring(最长回文子串) in s. You may assume that the maximum length of s is 1000.
	Example 1:
	Input: "babad"
	Output: "bab"
	Note: "aba" is also a valid answer.
my python algorithm:(Brute-force解法)
	input:string s
	
	process:
		1:get length of s,denoted l
		2:repeat
		3:	find all substring which have i length.	
		4:until i>l
		5:if substring is palindromic
		6:	append to list
		7:	return the longest substring of the list
		8:else	
		9:	return False
	
	output:longest palindromic substring、
	time complexity:O(n^3)=找到所有子串O(n^2)*判断子串是否为回文串O(n)，无需额外提供空间，space complexity：O(1)
other algorithm:
	1.dynamic programming,time complexity:O(n^2)=找到所有子串O(n^2)*判断是否为回文串O(1),该方法需要额外的空间维护dp数组，space complexity:O(n^2)
	2.manacher algorithm,time complexity:O(n),space complexity:O(n)
	3.(highly recommended)I find the best python solution in discussion area:it provides simple code and the time complexity is O(n),space complexity is O(1) 
"""
# coding=utf-8
class Solution(object):
	def longestPalindrome1(self, s):
	    """
		brute-force solution

	    para:
	    	s -- String

	    return:
	    	longestpalindrome -- String
	    """
	    lens=len(s)
	    if lens<2:
	        return s
	    maxlen=0
	    start=0
	    for i in range(lens):
	        for j in range(i+1,lens):
	            begin=i
	            end=j
	            # judge the palindrome
	            while begin<end:
	                if s[begin]!=s[end]:
	                    break
	                begin+=1
	                end-=1
	            if begin>=end and j-i>maxlen:
	                maxlen=j-i+1
	                start=i
	    if maxlen>0:
	        return s[start:start + maxlen]
	    return None
	

	def longestPalindrome2(self, s):
		"""
		dynamic programming
		"""
		if not s:
			return None
		lens=len(s)
		if lens<2:
			return s
		maxlen=0
		start=0
		dp=[[0 for _ in range(lens)] for _ in range(lens)]
		print(dp[2][3])

		#step 1
		for i in range(lens):
			dp[i][i]=True
			if i<lens-1 and s[i]==s[i+1]:
				dp[i][i+1]=1
				start=i
				maxlen=2
 
        #step 2
		for i in range(3,lens+1):
			for j in range(0,lens-i+1):
				r=j+i-1
				if dp[j+1][r-1] and s[j]==s[r]:
					dp[j][r]=1
					maxlen=i
					start=j
        #step 3
		if maxlen>=2:
		    return s[start:start+maxlen]
		return None
	

	def longestPalindrome3(self, s):
		"""
		manacher algorithm
		"""
		if not s:
		    return None
		if len(s)<2:
			return s
		T='#'.join('@{}$'.format(s))#step 1
		#step2
		n=len(T)
		P=[0]*n
		c=0
		r=0
		for i in range(1,n-1):
		    i_mirror=c-(i-c)#i关于中心c的对称位置
		    if r>i:#利用之前回文串字符对比重复部分
		        P[i]=min(r-i,P[i_mirror])
		    # 中心扩展法完成之前没有涉及的字符比对
		    while T[i+1+P[i]]==T[i-1-P[i]]:
		        P[i]=P[i]+1
		    #更新当前回文串中心c及终止位置r
		    if i+P[i]>r:
		        c=i
		        r=i+P[i]
		#找到最大回文半径及对应的回文中心
		maxlen=0
		centeridx=0
		for i in range(1,n-1):
		    if P[i]>maxlen:
		        maxlen=P[i]
		        centeridx=i
		#获取最长回文串
		begin=(centeridx-maxlen)//2
		end=(centeridx+maxlen)//2
		return s[begin:end]
	

	def longestPalindrome4(self, s):
		"""
		discussion area best python algorithm
		"""
		begin_index, maxlength = 0, 0
		# useing for loop in order to find all substrings,which begin with begin_index(denoted with end_index and maxlength),
		# end with end_index,length with maxlength.
		for end_index in range(len(s)):
		    # 当终点索引减子字符串长度大于等于1时，表示当前子串的左侧至少还有两个字符，那么将当前子串的起索引往前推两个位置终索引不动并
		    # 判断这个子串是否为回文，如果是，则记录下起索引和子串长度，此处只需重置即可，因为我只需要最终状态
		    if end_index - maxlength >=1 and s[end_index - maxlength-1: end_index+1] == s[end_index - maxlength-1: end_index+1][::-1]:
		        begin_index = end_index - maxlength - 1
		        maxlength += 2
		    # 同理
		    elif end_index - maxlength >= 0 and s[end_index - maxlength: end_index+1] == s[end_index - maxlength: end_index+1][::-1]:
		        begin_index = end_index - maxlength
		        maxlength += 1
		return s[begin_index: begin_index+maxlength]

# test
if __name__ == "__main__":
	solution = Solution()
	palindrome1 = solution.longestPalindrome1("babad")
	palindrome2 = solution.longestPalindrome2("babad")
	palindrome3 = solution.longestPalindrome3("babad")
	palindrome4 = solution.longestPalindrome4("cbbd")	   
	print(palindrome1,palindrome2,palindrome3,palindrome4)
	