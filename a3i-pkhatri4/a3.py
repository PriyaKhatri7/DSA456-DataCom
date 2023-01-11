def get_idx(ch):
    return ord(ch.lower()) - ord('a')
    
class Trie:
    class TrieNode:
        
        # TrieNode is internal.  Feel free to add
        # to the argument list for its init function.
        # add to this init function whatever data members you like
        def __init__(self):
            self.children = [None] * 26
            self.terminal = False
                    

    # You cannot alter the prototype of this __init__ function
    # However you can add whatever data members you need
    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word):
        """ Function adds word to the Trie in while loop """
        pos = 0
        node = self.root
        while pos < len(word):
            idx = get_idx(word[pos])
            if node.children[idx] == None:
                node.children[idx] = self.TrieNode()
            node = node.children[idx]
            pos += 1
        node.terminal = True

    def search(self, word):
        """ Function searches for word in the Trie in while loop, returns True if found, False otherwise """
        pos = 0
        node = self.root

        while pos < len(word):
            idx = get_idx(word[pos])
            if node.children[idx] == None:
                return False
            node = node.children[idx]
            pos += 1

        return node.terminal

    def get_all(self):
        """ Function returns the list of all words in the Trie in alphabetical order """
        res = []
        self.get_all_helper(self.root, "", res)
        return res

    def get_all_helper(self, node, prefix, res):
        """ Function to get the Trie for the range of 26 pointers for get_all() function. """
        if node.terminal:
            res.append(prefix)
        for i in range(26):
            if node.children[i] != None:
                self.get_all_helper(node.children[i], prefix + chr(i + ord('a')), res)

    def begins_with(self, prefix):
        """ Function returns the list of all words that begin with prefix in the Trie in alphabetical order"""
        res = []
        # get all words that begin with prefix
        pos = 0
        node = self.root
        while pos < len(prefix):
            idx = get_idx(prefix[pos])
            if node.children[idx] == None:
                return []
            node = node.children[idx]
            pos += 1
        self.get_all_helper(node, prefix, res)

        return res