class SortedList:
	class Node:
		
		# Node is internal.  Feel free to add
		# to the argument list for its init function if you want
		# you can add additonal data members if you like
		def __init__(self, data, next=None, prev=None):
			self.data = data 
			self.next = next 
			self.prev = prev

	# Sorted list is external, do not change its prototype.
	# you can add additional data members if you like
	def __init__(self):
		self.front = SortedList.Node(None)
		self.back = SortedList.Node(None, None, self.front)
		self.front.next = self.back


	def insert(self,data):
		""" Creates a new node with the data and inserts it into the linked list keeping it sorted """
		if (self.front.next == self.back):
			ref = self.front
		else:
			curr = self.front.next
			while (curr != self.back and data > curr.data):
				curr=curr.next
			ref= curr.prev
		nn = SortedList.Node(data, ref.next, ref)
		ref.next.prev = nn
		ref.next = nn

	def remove(self,data):
		""" Finds and removes node containing data from the list. Returns True if it is removed, False otherwise """
		if (self.front.next == self.back):
			return False
		else:
			curr = self.front.next
			while (curr != self.back and data >= curr.data):
				if curr.data == data:
					curr.next.prev = curr.prev
					curr.prev.next = curr.next
					curr = None
					return True
				curr = curr.next
			return False

	def is_present(self, data):
		""" Checks in each node if data is present, returns true is data is found and false otherwise """
		if (self.front.next == self.back):
			return False
		else:
			curr = self.front.next
			while (curr != self.back and data >= curr.data):
				if curr.data == data:
					return True
				curr = curr.next
			return False
		

	def __len__(self):
		""" Counts each node in the linked list, except sentinel nodes and return the number """
		count = 0
		if (self.front.next == self.back):
			return count
		else:
			curr = self.front.next
			while (curr != self.back):
				count+=1
				curr = curr.next
			return count




	# The functions below called __iter__ and __reversed__ 
	# allows an external function to
	# iterate through your list. 
	#
	# myll = SortedList()
	# 
	# for i in myll:
	#     print(i)
	# 
	# for i in reversed(myll):
	# 	  print(i)
	#
	# with each iteration, curr goes through only one step of the while loop
	# (ie you don't run it all at once..)
	# there are two versions of these function as sentinels nodes do 
	# make a difference in terms of where you start and end
	# keep only the version you are using and erase the version you are 
	# not using (or comment it out...)

	# NOTE: if you change the names of your data members, you need
	# to change them in the functions below or your tests won't pass.

	# This is the version you need if you do not use sentinels:
	# def __iter__(self):
	# 	curr = self.front
	# 	while curr:
	# 		yield curr.data
	# 		curr=curr.next

	# def __reversed__(self):
	# 	curr = self.back
	# 	while curr:
	# 		yield curr.data
	# 		curr=curr.prev

	# This is the version you need if you used sentinels:
	def __iter__(self):
		curr = self.front.next
		while curr != self.back:
			yield curr.data
			curr=curr.next

	def __reversed__(self):
		curr = self.back.prev
		while curr != self.front:
			yield curr.data
			curr=curr.prev