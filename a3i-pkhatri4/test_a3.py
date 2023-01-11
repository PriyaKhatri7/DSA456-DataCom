#
#   Author: Catherine Leung
#   These are the unit tests for functions and classes of assingment1
#   To use this, run: python test_a3.py

import unittest
from a3 import Trie

class A3TestCase(unittest.TestCase):
    """These are the test cases for functions and classes of a1"""
    
    def test_insert_search(self):
        words = ["yellow", "yell", "yeti", "yes","red","redraw","ran","y"]
        the_trie = Trie()
        for i in range(8):
            the_trie.insert(words[i])
            i+=1

        for i in range(8):
            self.assertEqual(the_trie.search(words[i]), True)

        self.assertEqual(the_trie.search("yel"), False)
        self.assertEqual(the_trie.search("yello"), False)
        self.assertEqual(the_trie.search("yetis"), False)
        self.assertEqual(the_trie.search("ranger"), False)
        self.assertEqual(the_trie.search("redr"), False)
        self.assertEqual(the_trie.search("redra"), False)
            
    def test_get_all(self):
        words = ["yellow", "yell", "yeti", "yes","red","redraw","ran"]
        the_trie = Trie()
        for i in range(7):
            the_trie.insert(words[i])
            i+=1

        all_words =the_trie.get_all()
        words.sort()

        self.assertEqual(len(all_words), len(words))
        self.assertEqual(all_words,words)

    def test_begins_with(self):
        words = ["yellow", "yell", "yeti", "yes","red","redraw","ran"]
        the_trie = Trie()
        for i in range(7):
            the_trie.insert(words[i])
            i+=1

        result = the_trie.begins_with("yel")

        self.assertEqual(result,["yell","yellow"])

        result = the_trie.begins_with("red")

        self.assertEqual(result,["red","redraw"])

        result = the_trie.begins_with("y")

        self.assertEqual(result,["yell","yellow","yes","yeti"])

    def test_big_trie(self):
        file = open("dictionary.txt", "r")
        words = file.readlines()
        file.close()
        for i in range(len(words)):
            words[i]=words[i].strip()

        half = len(words)//2
        the_trie = Trie()
        for i in range(0,half):
            the_trie.insert(words[i])
            i+=1

        for i in range(0,half):
            self.assertEqual(the_trie.search(words[i]), True)

        for i in range (half,len(words)):
            self.assertEqual(the_trie.search(words[i]), False)

        for i in range(half,len(words)):
            the_trie.insert(words[i])
            i+=1


        all_words=the_trie.get_all()

        words.sort()
      
        self.assertEqual(len(all_words), len(words))
        self.assertEqual(all_words,words)



        prefix_and_result ={
            "carrot": ["carrot","carroter","carrotiest","carrotiness","carrotins",
                        "carrottop","carrotwood"],
            "swimm":["swimmable","swimmeret","swimmers","swimmiest","swimminess",
                        "swimmingly","swimmings","swimmy"],
            "toron":["toronto"],
            "orange":["orange","orangeades","orangeat","orangeberry","orangeish",
                        "orangeist","orangeman","oranger","orangeroot","oranges",
                        "orangewood"],
            "harmoni":["harmoniacal","harmonic","harmonical","harmonicalness",
                        "harmonichord","harmonicism","harmonics","harmonious",
                        "harmoniousness","harmoniphone","harmonisation",
                        "harmonised","harmonising","harmonistic","harmonite",
                        "harmoniums","harmonization","harmonize","harmonizer","harmonizes"]
        }
        prefixes = prefix_and_result.keys()

        for prefix in prefixes:
            result = the_trie.begins_with(prefix)
            self.assertEqual(result, prefix_and_result[prefix])


if __name__ == '__main__':
    unittest.main()
