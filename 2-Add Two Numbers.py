"""
#OS:windows,python3.6
@author:yi
created:Sept 13,2018
task:
	You are given two non-empty linked lists representing two non-negative integers. 
	The digits are stored in reverse order and each of their nodes contain a single digit. 
	Add the two numbers and return it as a linked list.
	You may assume the two numbers do not contain any leading zero, except the number 0 itself.
	Example:
	Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
	Output: 7 -> 0 -> 8
	Explanation: 342 + 465 = 807.
time complexity:
	O(logn)
 """
# coding=utf-8
class ListNode(object):
	"""define node of linked list"""
	def __init__(self, x):
		"""
		define constructor function

		parameters:
			x -- value of every node,int
		"""
		self.value = x
		# attribution of next to be a ListNode 
		self.next = None


def creat_linked_list(_list_):
	"""
	creat linked list with ListNode

	para:
		_list_ -- node list of linked list,any length list 

	return:
		root -- root node of linked list,ListNode
	"""
	if len(_list_) == 0:
		return False
	if len(_list_) == 1:
		return ListNode(_list_[0])
	else:
		root = ListNode(_list_[0])
		temp = root
		for i in _list_[1:]:
			temp.next=ListNode(i)  
			temp=temp.next  
	return root 


class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		add two linked list

		parameters:
			l1 -- the head node of first linked list,ListNode
			l2 -- the head node of second linked list,ListNode
		
		return: 
			root_node.next -- next node of 0 node ,ListNode
		"""
		carry = 0
		root_node = ListNode(0)
		temp_node = root_node
		while l1 or l2:
			x = l1.value if l1 else 0
			y = l2.value if l2 else 0
			sum = x + y + carry
			carry = sum // 10
			temp_node.next = ListNode(sum % 10)
			temp_node = temp_node.next
			l1 = l1.next if l1 else l1
			l2 = l2.next if l2 else l2
			if carry >0 :
				temp_node.next = ListNode(carry)
		return root_node.next


if __name__ == "__main__":
	l1 = creat_linked_list([2,4,3])
	l2 = creat_linked_list([5,6,4])
	solution = Solution()
	first_value = solution.addTwoNumbers(l1, l2).value
	second_value = solution.addTwoNumbers(l1, l2).next.value
	third_value = solution.addTwoNumbers(l1, l2).next.next.value
	print("the sum linked list is :{0}->{1}->{2}".format(first_value,second_value,third_value))