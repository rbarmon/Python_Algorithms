"""
2 catGPT (10 marks)
"""


# The longest sentence would have M characters, as mapped from the cat vocabulary. M  is a positive integer.
# A cat word can occur more than once in a single sentence. For example, the string baacbb represents a valid sentence.
# It is possible for more than a single sentence to have the same words. Have a look at the example in Section 2.4.
# You can assume that there is only a maximum of 26 unique cat words in total, represented as lower case characters from a to z.

# Consider implementing a Node class to help encapsulate additional information that you might want to store in your CatsTrie class to help solve this problem.
class CharacterNode:
    def __init__(self, character):
        self.connected_nodes = [None] * 26
        self.character = character
        self.frequency = 1
        self.is_end = False
        self.sentence = None

    # def __init__(self, character, true, sentence):
    #     self.connected_nodes = [None] * 26
    #     self.character = character
    #     self.frequency = 1
    #     self.is_end = true
    #     self.sentence = sentence

    def updateFrequency(self):
        self.frequency += 1

    def last_letter(self):
        self.is_end = True


    def store_sentence_in_last_letter(self, sentence):
        self.sentence = sentence

class EndNode:
    def __init__(self, sentence):
        self.character = '$'
        self.sentence = sentence
        self.frequency = 1


    def updateFrequency(self):
        self.frequency += 1

# The CatsTrie class structure
class CatsTrie:
    def __init__(self, sentences):
        """
            The __init__(sentences) constructor of CatsTrie class would run in O(NM) time and space
            where:
            • N is the number of sentence in sentences.
            • M is the number of characters in the longest sentence.
        """
        self.N = len(sentences)
        # N sentences, where N is a positive integer.
        # self.M = None
        # The longest sentence would have M characters, as mapped from the cat vocabulary. M  is a positive integer.
        # A cat word can occur more than once in a single sentence. For example, the string baacbb represents a valid sentence.
        # It is possible for more than a single sentence to have the same words. Have a look at the example in Section 2.4.
        self.trie = CharacterNode(' ')

        self.generateTrie(self.trie, sentences) #26
        # You can assume that there is only a maximum of 26 unique cat words in total, represented as lower case characters from a to z.

    def generateTrie(self, trie, sentences):

        # sentences = ["abc", "abazacy", "dbcef", "xzz", "gdbc", "abazacy", "xyz", "abazacy", "dbcef", "xyz", "xxx", "xzz"]

        # connected_nodes[None,...,None]
        # CharacterNode.connected_nodes[]

        # trie.connected_nodes[ord(sentences[i][j]) - 97].connected_nodes[],


        for i in range(len(sentences)):
            # while len(sentences[i]):
            for j in range(len(sentences[i])):
                if j == 0:
                    if self.trie.connected_nodes[ord(sentences[i][j]) - 97] is None:
                        node = CharacterNode(sentences[i][j])
                        self.trie.connected_nodes[ord(sentences[i][j]) - 97] = node
                        temp = self.trie.connected_nodes[ord(sentences[i][j]) - 97]
                    else:
                        self.trie.connected_nodes[ord(sentences[i][j]) - 97].updateFrequency()
                        temp = self.trie.connected_nodes[ord(sentences[i][j]) - 97]
                    # self.trie.connected_nodes
                elif j == len(sentences[i]) - 1:
                    # print("hey")
                    if temp.connected_nodes[ord(sentences[i][j]) - 97] is None:
                        node = CharacterNode(sentences[i][j])
                        node.last_letter()
                        node.store_sentence_in_last_letter(sentences[i])

                        # temp.connected_nodes[ord(sentences[i][j]) - 97] = CharacterNode(sentences[i][j], True, sentences[i])
                        temp.connected_nodes[ord(sentences[i][j]) - 97] = node
                        temp = temp.connected_nodes[ord(sentences[i][j]) - 97]
                    else:
                        temp.connected_nodes[ord(sentences[i][j]) - 97].updateFrequency()
                        temp.connected_nodes[ord(sentences[i][j]) - 97].last_letter()
                        temp.connected_nodes[ord(sentences[i][j]) - 97].store_sentence_in_last_letter(sentences[i])
                        temp = temp.connected_nodes[ord(sentences[i][j]) - 97]
                else:
                    if temp.connected_nodes[ord(sentences[i][j]) - 97] is None:
                        # node = CharacterNode(sentences[i][j])
                        temp.connected_nodes[ord(sentences[i][j]) - 97] = CharacterNode(sentences[i][j])
                        temp = temp.connected_nodes[ord(sentences[i][j]) - 97]
                    else:
                        temp.connected_nodes[ord(sentences[i][j]) - 97].updateFrequency()
                        temp = temp.connected_nodes[ord(sentences[i][j]) - 97]


    def findSentence(self, temp):

        print(temp.connected_nodes)
        print(temp.character)
        # print(temp.connected_nodes[0].frequency)
        while temp:
            min_freq = None
            for i in range(26):
                if temp.connected_nodes[i] is None:
                    continue
                elif min_freq == None:
                    min_freq = temp.connected_nodes[i]
                    print(min_freq.character)
                else:
                    if temp.connected_nodes[i].frequency == 1 or min_freq.frequency == 1:
                        if temp.connected_nodes[i].frequency > min_freq.frequency:
                            print(temp.connected_nodes[i].character)
                            min_freq = temp.connected_nodes[i]
                        elif temp.connected_nodes[i].frequency < min_freq.frequency:
                            print(min_freq.character)
                            continue
                        else:
                            # tiebreaker
                            if ord(temp.connected_nodes[i].character) < ord(min_freq.character):
                                min_freq = temp.connected_nodes[i]
                            else:
                                continue
                    else:
                        option_1 = self.frequencyDecider(temp.connected_nodes[i])
                        option_2 = self.frequencyDecider(min_freq)
                        if option_1.frequency > option_2.frequency:
                            print(temp.connected_nodes[i].character)
                            min_freq = temp.connected_nodes[i]
                        elif option_1.frequency < option_2.frequency:
                            print(min_freq.character)
                            continue
                        else:
                            # tiebreaker
                            if ord(temp.connected_nodes[i].character) < ord(min_freq.character):
                                min_freq = temp.connected_nodes[i]
                            else:
                                continue
            if min_freq == None:
                print(temp.sentence)
                return temp.sentence
            else:
                print(min_freq.character)
                print(min_freq.frequency)
                temp = min_freq

    def frequencyDecider(self, temp):

        print(temp.connected_nodes)
        print(temp.character)
        # print(temp.connected_nodes[0].frequency)
        while temp:
            min_freq = None
            for i in range(26):
                if temp.connected_nodes[i] is None:
                    continue
                elif min_freq == None:
                    min_freq = temp.connected_nodes[i]
                    print(min_freq.character)
                else:
                    if temp.connected_nodes[i].frequency == 1 or min_freq.frequency == 1:
                        if temp.connected_nodes[i].frequency > min_freq.frequency:
                            print(temp.connected_nodes[i].character)
                            min_freq = temp.connected_nodes[i]
                        elif temp.connected_nodes[i].frequency < min_freq.frequency:
                            print(min_freq.character)
                            continue
                        else:
                            # tiebreaker
                            if ord(temp.connected_nodes[i].character) < ord(min_freq.character):
                                min_freq = temp.connected_nodes[i]
                            else:
                                continue
                    else:
                        option_1 = self.frequencyDecider(temp.connected_nodes[i])
                        option_2 = self.frequencyDecider(min_freq)
                        if option_1.frequency > option_2.frequency:
                            print(temp.connected_nodes[i].character)
                            min_freq = temp.connected_nodes[i]
                        elif option_1.frequency < option_2.frequency:
                            print(min_freq.character)
                            continue
                        else:
                            # tiebreaker
                            if ord(temp.connected_nodes[i].character) < ord(min_freq.character):
                                min_freq = temp.connected_nodes[i]
                            else:
                                continue
                        # option_1 = self.findSentence(self, temp.connected_nodes[i])
                        # option_2 = self.findSentence(self, min_freq)
                        # if temp.connected_nodes[i].frequency > min_freq.frequency:
                        #     print(temp.connected_nodes[i].character)
                        #     min_freq = temp.connected_nodes[i]
                        # elif temp.connected_nodes[i].frequency < min_freq.frequency:
                        #     print(min_freq.character)
                        #     continue
                        # else:
                        #     # tiebreaker
                        #     if ord(temp.connected_nodes[i].character) < ord(min_freq.character):
                        #         min_freq = temp.connected_nodes[i]
                        #     else:
                        #         continue
            if min_freq == None:
                print(temp)
                return temp
            else:
                print(min_freq.character)
                print(min_freq.frequency)
                temp = min_freq

    def autoComplete(self, prompt):
        """
        The autoComplete(self, prompt) of the CatsTrie class would run in O(X + Y ) time where:
        • X is the length of the prompt.
        • Y is the length of the most frequent sentence in sentences that begins with the prompt, unless such sentence do not exist (in which case autoComplete(self, prompt) should have complexity O(X)). Thus, this is an output-sensitive complexity.

        prompt is a string with characters in the set of [a...z]. This string represents the incomplete sentence that is to be completed by the trie.


        The function would then return a string that represents the completed sentence from the prompt. Do note the following:
        • If such a sentence exist, return the completed sentence with the highest frequency in the cat sentences list.
        • If there are multiple possible auto-complete sentences with the same highest frequency, then you would return the lexicographically smaller string.
        • If such a sentence does not exist, return None
        """

        temp = self.trie

        for i in range(len(prompt)):
            if temp.connected_nodes[ord(prompt[i]) - 97]:
                temp = temp.connected_nodes[ord(prompt[i]) - 97]
            else:
                print(None)
                return None
        # print('hey')

        # self.trie
        return self.findSentence(temp)



            # if i == len(prompt) - 1:
            #     temp.connected_nodes(ord(prompt[i]) - 97)
            #     temp = temp.connected_nodes(ord(prompt[i]) - 97)
            # else:
            #     if temp.connected_nodes(ord(prompt[i]) - 97):
            #         temp = temp.connected_nodes(ord(prompt[i]) - 97)
            #



                # ab

        # connected_nodes[ord(sentences[i][j]) - 97]
        #
        # self.character = character
        # self.frequency = 1
        # self.is_end = False
        # self.sentence = None

        #1. highest frequency

        #If same then 2. smaller lexico string

        #3.If none exist then return None


        # based on the most commonly used sentences.




    # def characterIndex(self, character):
    #     # match character:
    #     #     case 'a':
    #     #         return 0
    #     if character == 'a':   return 0
    #     elif character == 'b': return 1
    #     elif character == 'c': return 2
    #     elif character == 'd': return 3
    #     elif character == 'e': return 4
    #     elif character == 'f': return 5
    #     elif character == 'g': return 6
    #     elif character == 'h': return 7
    #     elif character == 'i': return 8
    #     elif character == 'j': return 9
    #     elif character == 'k': return 10
    #     elif character == 'l': return 11
    #     elif character == 'm': return 12
    #     elif character == 'n': return 13
    #     elif character == 'o': return 14
    #     elif character is 'p': return 15
    #     elif character is 'q': return 16
    #     elif character is 'r': return 17
    #     elif character is 's': return 18
    #     elif character is 't': return 19
    #     elif character is 'u': return 20
    #     elif character is 'v': return 21
    #     elif character is 'w': return 22
    #     elif character is 'x': return 23
    #     elif character is 'y': return 24
    #     else: return 25






if __name__ == '__main__':
    # Example 1, similar to the introduction
    # but with some additional sentences
    sentences = ["abc", "abazacy", "dbcef", "xzz", "gdbc", "abazacy", "xyz",
                 "abazacy", "dbcef", "xyz", "xxx", "xzz"]
    # Creating a CatsTrie object
    mycattrie = CatsTrie(sentences)
    # print(mycattrie.trie.connected_nodes)
    # print(mycattrie.trie.connected_nodes[0])
    # print(mycattrie.trie.connected_nodes[0].connected_nodes[1])
    # print(mycattrie.trie.connected_nodes[0].connected_nodes[1].connected_nodes[2])
    # print(mycattrie.trie.connected_nodes[0].character)
    # print(mycattrie.trie.connected_nodes[0].connected_nodes[1].character)
    # print(mycattrie.trie.connected_nodes[0].connected_nodes[1].frequency)
    # print(mycattrie.trie.connected_nodes[0].connected_nodes[1].connected_nodes[2].character)
    # print(mycattrie.trie.connected_nodes[0].connected_nodes[1].connected_nodes[2].is_end)
    # print(mycattrie.trie.connected_nodes[0].connected_nodes[1].connected_nodes[2].sentence)
    #
    # print(mycattrie.trie.connected_nodes[0].connected_nodes[1].connected_nodes[0].connected_nodes[25].character)
    #
    # # tri =
    #
    # print(mycattrie.trie.connected_nodes[23].connected_nodes[25].connected_nodes[25].sentence)
    # print(mycattrie.trie.connected_nodes[23].connected_nodes[25].connected_nodes[25].is_end)
    # print(mycattrie.trie.connected_nodes[23].connected_nodes[25].is_end)


    # # Example 1.1
    # # A simple example
    # prompt = "ab"
    # mycattrie.autoComplete(prompt)
    # abazacy

    # # Example 1.2
    # # Another simple example
    # prompt = "a"
    # mycattrie.autoComplete(prompt)
    # # abazacy
    #
    # # Example 1.3 ok
    # # What if the prompt is the same as an existing sentence?
    # prompt = "dbcef"
    # mycattrie.autoComplete(prompt)
    # # dbcef


    # Example 1.4 OK
    # What if the length is longer?
    # prompt = "dbcefz"
    # mycattrie.autoComplete(prompt)
    # None

    # Example 1.5 OK
    # What if sentences doesn’t exist.
    # prompt = "ba"
    # mycattrie.autoComplete(prompt)
    # None

    # # Example 1.6
    # # A scenario where the tiebreaker is used
    # prompt = "x"
    # mycattrie.autoComplete(prompt)
    # # xyz
    #
    # # Example 1.7
    # # A scenario where the prompt is empty
    # prompt = ""
    # mycattrie.autoComplete(prompt)
    # # abazacy