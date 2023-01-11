# if you wish to use your sorted list from a1, copy and paste it here
# this is not the best way to do this but the test scripts are not
# designed to pick up an extra file. 

class ChainingHash:

	# This is a single record in a chaining hash table.  You can
	# change this in any way you wish (including not using it at all)
	class Record:
		def __init__(self, key = None, value=None):
			self.key=key
			self.value=value


	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice (but it must be a hash
	# table that use chaining for collision resolution
	def __init__(self, cap=32):
		""" Create a list with capacity elements all initalized to None """
		self.cap = cap
		self.the_table = [[] for i in range(self.cap)]
		self.length = 0

	def insert(self,key, value):
		""" Adds a new key-value pair to the table. If exists, return False, Othersise adds new key-value and return True. If adding the new record causes the load factor to exceed 0.7, 
        you must grow your table by doubling its capacity """
		self.length += 1
		index = hash(key) % self.cap

		for record in self.the_table[index]:
			if(record[0] == key):
				self.length -= 1
				return False
		if ((1.0* (self.length) / self.cap) > 1):
			self._grow()

		self.the_table[index].append((key,value))
		return True

	def modify(self, key, value):
		""" Modifies existing pairs, if no record, return False, otherwise updates and passed returning True """
		index = hash(key) % self.cap

		for num, record in enumerate(self.the_table[index]):
			if (record[0] == key):
				self.the_table[index][num]=(key,value)
				return True

		return False

	def remove(self, key):
		""" If no matching key exists, return False. Otherwise, return True """
		index = hash(key) % self.cap

		for num, record in enumerate(self.the_table[index]):
			if(record[0]==key):
				del self.the_table[index][num]
				self.length -= 1
				return True

		return False

	def search(self, key):
		""" Returns value of record with matching key. If nothing matching, return None """
		index = hash(key) % self.cap

		for record in self.the_table[index]:
			if(record[0] == key):
				return record[1]
		return None

	def capacity(self):
		""" Checks for number of available spots in the table """
		return self.cap

	def __len__(self):
		""" Number of records stored in the table """
		return self.length

	def _grow(self):
		self.length = 1
		self.cap = self.cap * 2
		oldTable = self.the_table
		self.the_table = [[] for i in range(self.cap)]
		for item in oldTable:
			for pop in item:
					self.insert(pop[0], pop[1])

class LinearProbingHash:

	# This is a single record in a chaining hash table.  You can
	# change this in anyway you wish (including not using it at all)
	class Record:
		def __init__(self, key = None, value=None):
			self.key = key
			self.the_table = value


	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice (but it must be a hash
	# table that use linear probing for collision resolution)

	def __init__(self, cap = 32):
		self.cap = cap
		self.the_table = [None] * self.cap
		self.length = 0
		self.max_load_factor = 0.70

	def insert(self,key, value):
		""" Adds a new key-value pair to the table. If exists, return False, Othersise adds new key-value and return True. If adding the new record causes the load factor to exceed 0.7, 
        you must grow your table by doubling its capacity """
		self.length += 1
		hashed_key = hash(key) % self.cap
		
		while self.the_table[hashed_key] is not None:
			if self.the_table[hashed_key][0] == key:
				self.length -= 1
				return False

			hashed_key = self._hash(hashed_key)

		if self.length / float(self.cap) >= self.max_load_factor:
			self._grow()
		tuple = (key, value)
		self.the_table[hashed_key] = tuple
		return True

	def modify(self, key, value):
		""" Modifies existing key-value pair into the table. If no matching record, returns False. Otherwise, 
		modifies the changes the existing value into the one passed into the function and returns True """
		index = hash(key) % self.cap
		record = index
		while self.the_table[index] is not None and index != record - 1:
			if(self.the_table[index][0]==key and self.the_table[index][0] != None):
				self.the_table[index] = (key,value)
				return True

			index = self._hash(index)
		return False

	def remove(self, key):
		""" Removes the key-value pair with the matching key. If no matching key exists, return False. Otherwise, return True """
		count = 0

		for item in self.the_table:
			if(item is not None):
				if(item[0] == key):
					self.the_table[count] = None
					self.length -= 1
					return True
			count += 1
		return False

	def search(self, key):
		""" Returns value of record with matching key. If nothing matching, return None """
		for item in self.the_table:
			if (item is not None):
				if (item[0] == key):
					return item[1]
		return None

	def capacity(self):
		""" Checks for number of available spots in the table """
		return self.cap

	def __len__(self):
		""" Number of records stored in the table """
		if(self.length > self.cap):
			self.length -= 1
		return self.length

	def _grow(self):
		""" This function doubles the capacity of the table and rehashes all the key-value pairs """
		self.cap *= 2
		self.length = 1
		old_table = self.the_table
		self.the_table = [None] * self.cap
		for tuple in old_table:
			if tuple is not None:
				self.insert(tuple[0],tuple[1])

	def _hash(self, key):
		""" This function returns the index of the table where the key-value pair should be stored """
		return (key + 1) % self.cap 
