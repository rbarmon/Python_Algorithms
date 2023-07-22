import unittest
# from a2t2 import CatsTrie
# from a2t2Final import CatsTrie
from Assignments.Assignment2.assignment2 import CatsTrie


__author__ = "Compiled by Junru (William) Wei, last updated 21/05/2023"


class CatGPTTest(unittest.TestCase):

    #These All have the same problem
    def test_01_specific(self): #FAIL
        sentences = ["ab", "a"]
        trie = CatsTrie(sentences)
        self.assertTrue(trie.autoComplete("") == "a")
        self.assertTrue(trie.autoComplete("a") == "a")

    def test_02_specific(self): #FAIL
        sentences = ["a", "ab"]
        trie = CatsTrie(sentences)
        self.assertTrue(trie.autoComplete("") == "a")
        self.assertTrue(trie.autoComplete("a") == "a")

    def test_default_spec(self): #FAIL
        sentences = ["abc", "abczacy", "dbcef", "xzz", "gdbc", "abczacy", "xyz", "abczacy", "dbcef", "xyz", "xxx",
                     "xzz"]
        trie = CatsTrie(sentences)
        self.assertTrue(trie.autoComplete("abc") == "abczacy")

    def test_05_spec(self):
        sentences = ["a", "a", "aa", "aa"]
        trie = CatsTrie(sentences)
        self.assertTrue(trie.autoComplete("") == "a")
        self.assertTrue(trie.autoComplete("a") == "a")


    def test_07_spec(self):
        # Extract of The Oxford 3000 word list
        # Source: https://www.oxfordlearnersdictionaries.com/wordlist/american_english/oxford3000/
        sentences = ["fit", "fix", "fixed",
                     "flag", "flame", "flash", "flat", "flavor",
                     "flesh",
                     "flight",
                     "float", "flood","floor","flour","flow","flower",
                     "flu",
                     "fly","flying",
                     "focus", "fold", "folding", "folk",
                     "follow", "following",
                     "food", "foot", "football",
                     "for", "force", "forecast", "foreign", "forest", "forever", "forget", "forgive", "fork", "form", "formal", "former", "formerly", "formula", "fortune","forward",
                     "found", "foundation"]
        trie = CatsTrie(sentences)
        # Inner branch decider------------------------------------------
        # These need to compare between levels
        # self.assertTrue(trie.autoComplete("") == "fit") #fit vs. fix vs. fixed
        # self.assertTrue(trie.autoComplete("f") == "fit") #fit vs. fix vs. fixed
        # self.assertTrue(trie.autoComplete("fi") == "fit") #fit vs. fix vs. fixed
        # self.assertTrue(trie.autoComplete("fix") == "fix") #fix vs. fixed
        #But this works -> Inner branch lexico decider + freq
        self.assertTrue(trie.autoComplete("fit") == "fit")

        #This works because its just lexico on the same level
        self.assertTrue(trie.autoComplete("fl") == "flag") #"flag", "flame", "flash", "flat", "flavor", on "a" compare g,m,s,t,v
        self.assertTrue(trie.autoComplete("fla") == "flag")

        # Inner branch decider------------------------------------------
        self.assertTrue(trie.autoComplete("foo") == "food") #"food", "foot", "football" multilayer issue t vs tball
        self.assertTrue(trie.autoComplete("flo") == "float")
        # "float", "flood", "floor", "flour", "flow", "flower", probably a  "flood", "floor" od vs or problem

        self.assertTrue(trie.autoComplete("for") == "for")
        self.assertTrue(trie.autoComplete("fo") == "focus")

       #These traverse to the point where it doesnt mess up
        self.assertTrue(trie.autoComplete("flat") == "flat")
        self.assertTrue(trie.autoComplete("flu") == "flu")
        self.assertTrue(trie.autoComplete("fixe") == "fixed")













    def test_07(self):
        # Extract of The Oxford 3000 word list
        # Source: https://www.oxfordlearnersdictionaries.com/wordlist/american_english/oxford3000/
        sentences = ["fit", "fix", "fixed", "flag", "flame", "flash", "flat", "flavor", "flesh", "flight", "float",
                     "flood",
                     "floor", "flour", "flow", "flower", "flu", "fly", "flying", "focus", "fold", "folding", "folk",
                     "follow", "following", "food", "foot", "football", "for", "force", "forecast", "foreign", "forest",
                     "forever", "forget", "forgive", "fork", "form", "formal", "former", "formerly", "formula",
                     "fortune",
                     "forward", "found", "foundation"]
        trie = CatsTrie(sentences)

        self.assertTrue(trie.autoComplete("forc") == "force")


        self.assertTrue(trie.autoComplete("fify") == None)
        self.assertTrue(trie.autoComplete("fiu") == None)
        self.assertTrue(trie.autoComplete("fiv") == None)
        self.assertTrue(trie.autoComplete("fiw") == None)
        self.assertTrue(trie.autoComplete("fiy") == None)
        self.assertTrue(trie.autoComplete("fj") == None)
        self.assertTrue(trie.autoComplete("fk") == None)
        self.assertTrue(trie.autoComplete("forb") == None)
        self.assertTrue(trie.autoComplete("ford") == None)
        self.assertTrue(trie.autoComplete("monash") == None)




    def test_default(self):
        sentences = ["abc", "abazacy", "dbcef", "xzz", "gdbc", "abazacy", "xyz", "abazacy", "dbcef", "xyz", "xxx",
                     "xzz"]
        trie = CatsTrie(sentences)

        self.assertTrue(trie.autoComplete("x") == "xyz")
        self.assertTrue(trie.autoComplete("") == "abazacy")
        self.assertTrue(trie.autoComplete("ab") == "abazacy")
        self.assertTrue(trie.autoComplete("a") == "abazacy")
        self.assertTrue(trie.autoComplete("dbcef") == "dbcef")
        self.assertTrue(trie.autoComplete("dbcefz") == None)
        self.assertTrue(trie.autoComplete("ba") == None)



    def test_01(self):
        sentences = ["ab", "a"]
        trie = CatsTrie(sentences)
        self.assertTrue(trie.autoComplete("ab") == "ab")
        self.assertTrue(trie.autoComplete("abc") == None)
        self.assertTrue(trie.autoComplete("b") == None)
        self.assertTrue(trie.autoComplete("fittwozerozerofour") == None)


    def test_02(self):
        sentences = ["a", "ab"]
        trie = CatsTrie(sentences)
        self.assertTrue(trie.autoComplete("ab") == "ab")
        self.assertTrue(trie.autoComplete("abc") == None)
        self.assertTrue(trie.autoComplete("b") == None)
        self.assertTrue(trie.autoComplete("fittwozerozerofour") == None)



    def test_05(self):
        sentences = ["a", "a", "aa", "aa"]
        trie = CatsTrie(sentences)
        self.assertTrue(trie.autoComplete("aa") == "aa")
        self.assertTrue(trie.autoComplete("b") == None)



if __name__ == "__main__":
    unittest.main()