# class ConnectedAdjacencyList:
#     def __init__(self, character, connected_nodes):
#         self.connected_nodes = connected_nodes
#         self.connected_adjacency_list = []
#         self.character = character
#         self.frequency = 1
#         self.sentence_counter = 0
#         self.is_end = False
#         self.sentence = None
#
#     def find(self, node):
#         pass
#


class CharacterNode:
    def __init__(self, character):
        self.connected_nodes = [None] * 26
        # self.connected_adj_list = ConnectedAdjacencyList(character, self.connected_nodes)
        self.character = character #The string character
        self.frequency = 1  #The number of times the character occurs in the trie for that specific position
        self.max_sentence_frequency = 0
        self.parent = None
        self.sentence_counter = 0  #If the node is a end of sentence node represents the number of times the sentence is in sentences[]
        self.is_end = False #Boolean that will be True if the node is the end of a sentence>
        self.sentence = None #If the node is a end of sentence, will be the sentence in string form.

    def updateFrequency(self):
        self.frequency += 1

    def last_letter(self):
        self.is_end = True
    def store_sentence_in_last_letter(self, sentence):
        self.sentence = sentence
# The CatsTrie class structure
class CatsTrie:
    def __init__(self, sentences):
        self.N = len(sentences)
        # N sentences, where N is a positive integer.
        # self.M = None
        # The longest sentence would have M characters, as mapped from the cat vocabulary. M  is a positive integer.
        # A cat word can occur more than once in a single sentence. For example, the string baacbb represents a valid sentence.
        # It is possible for more than a single sentence to have the same words. Have a look at the example in Section 2.4.
        self.trie = CharacterNode(' ')

        self.generateTrie(sentences) #26
        # You can assume that there is only a maximum of 26 unique cat words in total, represented as lower case characters from a to z.


    def generateTrie(self, sentences):

        # sentences = ["abc", "abazacy", "dbcef", "xzz", "gdbc", "abazacy", "xyz", "abazacy", "dbcef", "xyz", "xxx", "xzz"]

        # connected_nodes[None,...,None]
        # CharacterNode.connected_nodes[]

        # trie.connected_nodes[ord(sentences[i][j]) - 97].connected_nodes[],


        for i in range(len(sentences)):
            for j in range(len(sentences[i])):
                #Add to trie directly for the first level of the trie
                if j == 0:
                    #If the position for the character is None meaning no character yet then create a New Node
                    if self.trie.connected_nodes[ord(sentences[i][j]) - 97] is None:
                        #If the letter is the last letter of the sentence. Create a node to indicate a word ends there
                        #give sentence counter = 1
                        if j == len(sentences[i]) - 1:
                            node = CharacterNode(sentences[i][j])
                            node.last_letter()
                            node.store_sentence_in_last_letter(sentences[i])
                            node.sentence_counter += 1
                            node.max_sentence_frequency += 1
                            node.parent = self.trie

                            print("A")
                            if node.sentence_counter > self.trie.max_sentence_frequency:
                                val = node.sentence_counter
                                self.trie.max_sentence_frequency = val


                            self.trie.connected_nodes[ord(sentences[i][j]) - 97] = node
                            temp = self.trie.connected_nodes[ord(sentences[i][j]) - 97]
                        else:
                        #if not last letter then just create a node
                            node = CharacterNode(sentences[i][j])
                            node.parent = self.trie
                            self.trie.connected_nodes[ord(sentences[i][j]) - 97] = node
                            temp = self.trie.connected_nodes[ord(sentences[i][j]) - 97]
                    #If the position for the character is not None then update the details of that node.
                    else:
                        #if the character is the last letter of the sentence update its details give the sentence_counter += 1
                        if j == len(sentences[i]) - 1:
                            self.trie.connected_nodes[ord(sentences[i][j]) - 97].last_letter()
                            self.trie.connected_nodes[ord(sentences[i][j]) - 97].store_sentence_in_last_letter(sentences[i])
                            self.trie.connected_nodes[ord(sentences[i][j]) - 97].updateFrequency()
                            self.trie.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter += 1
                            self.trie.connected_nodes[ord(sentences[i][j]) - 97].max_sentence_frequency += 1


                            print("B")
                            if self.trie.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter > self.trie.max_sentence_frequency:
                                val = self.trie.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter
                                self.trie.max_sentence_frequency = val


                            temp = self.trie.connected_nodes[ord(sentences[i][j]) - 97]
                        #otherwise just update frequency
                        else:
                            self.trie.connected_nodes[ord(sentences[i][j]) - 97].updateFrequency()
                            temp = self.trie.connected_nodes[ord(sentences[i][j]) - 97]

                #If current character of the sentence is the last character of the sentence and its not on the first layer of the trie

                elif j == len(sentences[i]) - 1:
                    # print("hey")
                    # If the position to enter the node is None that means its empty so add a Node that knows its the end
                    if temp.connected_nodes[ord(sentences[i][j]) - 97] is None:
                        node = CharacterNode(sentences[i][j])
                        node.last_letter()
                        node.store_sentence_in_last_letter(sentences[i])
                        node.sentence_counter += 1
                        node.max_sentence_frequency += 1

                        print("C")
                        # node.parent = temp
                        # max_sentence_temp = node
                        # while max_sentence_temp.parent:
                        #     if node.sentence_counter > max_sentence_temp.parent.max_sentence_frequency:
                        #         max_sentence_temp.parent.max_sentence_frequency = node.sentence_counter
                        #     else:
                        #         break
                        #     max_sentence_temp = max_sentence_temp.parent
                        # temp.connected_nodes[ord(sentences[i][j]) - 97] = node

                        temp.connected_nodes[ord(sentences[i][j]) - 97] = node
                        print(temp.connected_nodes[ord(sentences[i][j]) - 97].character)
                        print(temp.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter)
                        print(temp.connected_nodes[ord(sentences[i][j]) - 97].max_sentence_frequency)

                        for k in range(len(sentences[i])):
                            if k == 0:
                                if temp.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter > self.trie.connected_nodes[ord(sentences[i][k]) - 97].max_sentence_frequency:
                                    val = temp.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter
                                    self.trie.connected_nodes[ord(sentences[i][k]) - 97].max_sentence_frequency = val
                                    print('---------------------------------------------------------------------------------b-----------------------')
                                    print(self.trie.connected_nodes[ord(sentences[i][k]) - 97].max_sentence_frequency)
                                    print(self.trie.connected_nodes[ord(sentences[i][k]) - 97].character)
                                max_sentence_temp = self.trie.connected_nodes[ord(sentences[i][k]) - 97]
                                print(max_sentence_temp.character)

                            # elif k == len(sentences[i]) - 1:
                            #     break
                            else:
                                if temp.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter > max_sentence_temp.connected_nodes[ord(sentences[i][k]) - 97].max_sentence_frequency:
                                    print('inner')
                                    val = temp.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter
                                    max_sentence_temp.connected_nodes[ord(sentences[i][k]) - 97].max_sentence_frequency = val
                                print(max_sentence_temp.connected_nodes[ord(sentences[i][k]) - 97].character)
                                print(max_sentence_temp.connected_nodes[ord(sentences[i][k]) - 97].max_sentence_frequency)
                                max_sentence_temp = max_sentence_temp.connected_nodes[ord(sentences[i][k]) - 97]
                                print(
                                    '--------------------------------------------------------------------------------a-----------------------')

                        temp = temp.connected_nodes[ord(sentences[i][j]) - 97]


                    # Otherwise update node
                    else:
                        temp.connected_nodes[ord(sentences[i][j]) - 97].updateFrequency()
                        temp.connected_nodes[ord(sentences[i][j]) - 97].last_letter()
                        temp.connected_nodes[ord(sentences[i][j]) - 97].store_sentence_in_last_letter(sentences[i])
                        temp.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter += 1
                        temp.connected_nodes[ord(sentences[i][j]) - 97].max_sentence_frequency += 1

                        print("D")
                        #
                        # max_sentence_temp = temp.connected_nodes[ord(sentences[i][j]) - 97]
                        # while max_sentence_temp.parent:
                        #     if node.sentence_counter > max_sentence_temp.parent.max_sentence_frequency:
                        #         max_sentence_temp.parent.max_sentence_frequency = node.sentence_counter
                        #     else:
                        #         break
                        #     max_sentence_temp = max_sentence_temp.parent
                        # temp.connected_nodes[ord(sentences[i][j]) - 97] = node
                        #
                        # temp.connected_nodes[ord(sentences[i][j]) - 97] = node

                        for k in range(len(sentences[i])):
                            if k == 0:
                                if temp.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter > self.trie.connected_nodes[ord(sentences[i][k]) - 97].max_sentence_frequency:
                                    val = temp.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter
                                    self.trie.connected_nodes[ord(sentences[i][k]) - 97].max_sentence_frequency = val
                                max_sentence_temp = self.trie.connected_nodes[ord(sentences[i][k]) - 97]
                            elif k == len(sentences[i]) - 1:
                                break
                            else:
                                if temp.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter > max_sentence_temp.connected_nodes[ord(sentences[i][k]) - 97].max_sentence_frequency:
                                    val = temp.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter
                                    max_sentence_temp.connected_nodes[ord(sentences[i][k]) - 97].max_sentence_frequency = val
                                max_sentence_temp = max_sentence_temp.connected_nodes[ord(sentences[i][k]) - 97]


                        # max_sentence_temp = temp.connected_nodes[ord(sentences[i][j]) - 97]
                        # while max_sentence_temp.parent:
                        #     if max_sentence_temp.sentence_counter > max_sentence_temp.parent.max_sentence_frequency:
                        #         max_sentence_temp.parent.max_sentence_frequency = max_sentence_temp.sentence_counter
                        #     else:
                        #         break
                        #     max_sentence_temp = max_sentence_temp.parent

                        temp = temp.connected_nodes[ord(sentences[i][j]) - 97]

                #If the node isn't an end node then just apply the same conditions as above to either create or update a node
                else:
                    if temp.connected_nodes[ord(sentences[i][j]) - 97] is None:
                        # node = CharacterNode(sentences[i][j])
                        temp.connected_nodes[ord(sentences[i][j]) - 97] = CharacterNode(sentences[i][j])
                        temp = temp.connected_nodes[ord(sentences[i][j]) - 97]
                    else:
                        temp.connected_nodes[ord(sentences[i][j]) - 97].updateFrequency()
                        temp = temp.connected_nodes[ord(sentences[i][j]) - 97]

    def findSentence(self, temp):

        # print(temp.connected_nodes)
        # print(temp.character)
        # print(temp.is_end)
        # print("max sentence frequency")
        # print(temp.max_sentence_frequency)
        # print("sentence counter")
        # print(temp.sentence_counter)

        # print(temp.connected_nodes[0].frequency)

        print("hey")
        while temp:
            max_freq = None
            #Find the node with the highest frequency in general
            for i in range(26):
                if temp.connected_nodes[i] is None:
                    continue
                #Max_freq for this node has not yet been found then just set
                elif max_freq == None:
                    max_freq = temp.connected_nodes[i]
                    print(max_freq.character)
                else:
                    print("ELSE")
                    print(temp.connected_nodes[i].character)
                    print(temp.connected_nodes[i].max_sentence_frequency)
                    print(max_freq.character)
                    print(max_freq.max_sentence_frequency)
                    if temp.connected_nodes[i].max_sentence_frequency > max_freq.max_sentence_frequency:
                        print(temp.connected_nodes[i].character)
                        max_freq = temp.connected_nodes[i]
                    elif temp.connected_nodes[i].max_sentence_frequency < max_freq.max_sentence_frequency:
                        print(max_freq.character)
                        continue
                    elif temp.connected_nodes[i].max_sentence_frequency == max_freq.max_sentence_frequency:
                        # tiebreaker
                        print("hello")
                        print(temp.connected_nodes[i].character)
                        print(temp.connected_nodes[i].max_sentence_frequency)
                        print(max_freq.character)
                        print(max_freq.max_sentence_frequency)


                        if ord(temp.connected_nodes[i].character) < ord(max_freq.character):
                            max_freq = temp.connected_nodes[i]
                        else:
                            continue

            if max_freq == None:
                print(temp.sentence)
                print("here")
                return temp.sentence
            else:
                # print(max_freq.character)
                # print(max_freq.frequency)

                if temp.is_end == True:
                    print("hey")
                    print(temp.sentence)

                    print("Final Output")
                    # print(self.branch_decider(temp))
                    print("hey")
                    print(self.branch_decider(temp))
                    return self.branch_decider(temp)

                temp = max_freq

    def branch_decider(self, temp):

        max_freq = None
        for i in range(26):
            if temp.connected_nodes[i] is None:
                continue
            # Max_freq for this node has not yet been found then just set
            elif max_freq == None:
                max_freq = temp.connected_nodes[i]
                # print(max_freq.character)
            else:
                if temp.connected_nodes[i].max_sentence_frequency > max_freq.max_sentence_frequency:
                    print(temp.connected_nodes[i].character)
                    max_freq = temp.connected_nodes[i]
                elif temp.connected_nodes[i].max_sentence_frequency < max_freq.max_sentence_frequency:
                    print(max_freq.character)
                    continue
                elif temp.connected_nodes[i].max_sentence_frequency == max_freq.max_sentence_frequency:
                    # tiebreaker
                    if ord(temp.connected_nodes[i].character) < ord(max_freq.character):
                        max_freq = temp.connected_nodes[i]
                    else:
                        continue
        # if all_node in connected_nodes of temp is have a lower max_sentence_frequency than temp.sentence_count
        #     then return temp.sentence
        if max_freq == None:
            return temp.sentence
        elif temp.sentence_counter > max_freq.max_sentence_frequency:
            return temp.sentence
        # if equal do ord check just return because its the branch so will always be higher lexicographically
        elif temp.sentence_counter == max_freq.max_sentence_frequency:
            return temp.sentence
        # if there is a node with a higher freq call findSentence again:
        elif temp.sentence_counter < max_freq.max_sentence_frequency:
            print("Max Senteence Frequency")
            print(max_freq.max_sentence_frequency)
            print(max_freq.character)

            # temp = max_freq
            return self.findSentence(max_freq)



        # if temp.sentence_counter > self.frequencyDecider(max_freq).sentence
        #     print(self.frequencyDecider(max_freq).sentence)
        #     if option_1.frequency > option_2.frequency:
        #         # print(temp.connected_nodes[i].character)
        #         max_freq = temp.connected_nodes[i]
        #     elif option_1.frequency < option_2.frequency:
        #         # print(max_freq.character)
        #         continue
        #     else:
        #         # tiebreaker
        #         if ord(temp.connected_nodes[i].character) < ord(max_freq.character):
        #             max_freq = temp.connected_nodes[i]
        #         else:
        #             continue
        #     if temp.sentence < self.frequencyDecider(max_freq).sentence:
        #         print(temp.sentence)
        #         return temp.sentence
        # else:
        #     option_1 = self.frequencyDecider(temp.connected_nodes[i])
        #     option_2 = self.frequencyDecider(max_freq)
        #     if option_1.frequency > option_2.frequency:
        #         # print(temp.connected_nodes[i].character)
        #         max_freq = temp.connected_nodes[i]
        #     elif option_1.frequency < option_2.frequency:
        #         # print(max_freq.character)
        #         continue
        #     else:
        #         # tiebreaker
        #         if ord(temp.connected_nodes[i].character) < ord(max_freq.character):
        #             max_freq = temp.connected_nodes[i]
        #         else:
        #             continue



        # # print(temp.connected_nodes)
        # # print(temp.character)
        # # print(temp.connected_nodes[0].frequency)
        # while temp:
        #     max_freq = None
        #     for i in range(26):
        #         if temp.connected_nodes[i] is None:
        #             continue
        #         elif max_freq == None:
        #             max_freq = temp.connected_nodes[i]
        #             # print(max_freq.character)
        #         else:
        #             if temp.connected_nodes[i].frequency == 1 or max_freq.frequency == 1:
        #                 if temp.connected_nodes[i].frequency > max_freq.frequency:
        #                     # print(temp.connected_nodes[i].character)
        #                     max_freq = temp.connected_nodes[i]
        #                 elif temp.connected_nodes[i].frequency < max_freq.frequency:
        #                     # print(max_freq.character)
        #                     continue
        #                 else:
        #                     # tiebreaker
        #                     if ord(temp.connected_nodes[i].character) < ord(max_freq.character):
        #                         max_freq = temp.connected_nodes[i]
        #                     else:
        #                         continue
        #             else:
        #                 option_1 = self.frequencyDecider(temp.connected_nodes[i])
        #                 option_2 = self.frequencyDecider(max_freq)
        #                 if option_1.frequency > option_2.frequency:
        #                     # print(temp.connected_nodes[i].character)
        #                     max_freq = temp.connected_nodes[i]
        #                 elif option_1.frequency < option_2.frequency:
        #                     # print(max_freq.character)
        #                     continue
        #                 else:
        #                     # tiebreaker
        #                     if ord(temp.connected_nodes[i].character) < ord(max_freq.character):
        #                         max_freq = temp.connected_nodes[i]
        #                     else:
        #                         continue
        #                 # option_1 = self.findSentence(self, temp.connected_nodes[i])
        #                 # option_2 = self.findSentence(self, max_freq)
        #                 # if temp.connected_nodes[i].frequency > max_freq.frequency:
        #                 #     print(temp.connected_nodes[i].character)
        #                 #     max_freq = temp.connected_nodes[i]
        #                 # elif temp.connected_nodes[i].frequency < max_freq.frequency:
        #                 #     print(max_freq.character)
        #                 #     continue
        #                 # else:
        #                 #     # tiebreaker
        #                 #     if ord(temp.connected_nodes[i].character) < ord(max_freq.character):
        #                 #         max_freq = temp.connected_nodes[i]
        #                 #     else:
        #                 #         continue
        #     if max_freq == None:
        #         # print(temp)
        #         return temp
        #     else:
        #         # print(max_freq.character)
        #         # print(max_freq.frequency)
        #         temp = max_freq
        #



    def autoComplete(self, prompt):
        #1. highest frequency
        #If same then 2. smaller lexico string
        #3.If none exist then return None

        print('---------------------------------------------------------------------------------------------------------')
        temp = self.trie

        for i in range(len(prompt)):
            if temp.connected_nodes[ord(prompt[i]) - 97]:
                temp = temp.connected_nodes[ord(prompt[i]) - 97]
            else:
                #If prompt goes beyond the possible sentences in the trie then return None
                print(None)
                return None
        # print('hey')

        # Call findSentence for cases that handle determining #1. highest sentence frequency and 2. If same Frequency pick smaller lexico string
        return self.findSentence(temp)

def characterIndex(self, character):
    if character == 'a':   return 0
    elif character == 'b': return 1
    elif character == 'c': return 2
    elif character == 'd': return 3
    elif character == 'e': return 4
    elif character == 'f': return 5
    elif character == 'g': return 6
    elif character == 'h': return 7
    elif character == 'i': return 8
    elif character == 'j': return 9
    elif character == 'k': return 10
    elif character == 'l': return 11
    elif character == 'm': return 12
    elif character == 'n': return 13
    elif character == 'o': return 14
    elif character == 'p': return 15
    elif character == 'q': return 16
    elif character == 'r': return 17
    elif character == 's': return 18
    elif character == 't': return 19
    elif character == 'u': return 20
    elif character == 'v': return 21
    elif character == 'w': return 22
    elif character == 'x': return 23
    elif character == 'y': return 24
    elif character == 'z': return 25
    else: return None


if __name__ == '__main__':
    # sentences = ["ab", "a"]
    # trie = CatsTrie(sentences)
    # print(sentences)
    # trie.autoComplete("") == "a"
    # trie.autoComplete("a") == "a"

    # def test_01_specific(self): #FAIL
    #     sentences = ["ab", "a"]
    #     trie = CatsTrie(sentences)
    #     self.assertTrue(trie.autoComplete("") == "a")
    #     self.assertTrue(trie.autoComplete("a") == "a")
    #
    # def test_02_specific(self): #FAIL
    #     sentences = ["a", "ab"]
    #     trie = CatsTrie(sentences)
    #     self.assertTrue(trie.autoComplete("") == "a")
    #     self.assertTrue(trie.autoComplete("a") == "a")
    #
    # def test_edge_case_2_specific(self): #FAIL
    #     sentences = [
    #         "f", "f", "f", "f", "f", "f", "abca", "abca", "abca", "abca",
    #         "abc", "abc", "abc", "abc", "ad", "ad", "ad", "ad", "ad"
    #     ]
    #     mycattrie = CatsTrie(sentences)
    #     self.assertEqual(mycattrie.autoComplete(""), "f")
    #     self.assertEqual(mycattrie.autoComplete("abc"), "abc")

    # sentences = ["abc", "abazacy", "dbcef", "xzz", "gdbc", "abazacy", "xyz",
    #              "abazacy", "dbcef", "xyz", "xxx", "xzz"]
    sentences = [ "xzz",  "xyz", "xyz", "xxx", "xzz"]
    print(sentences)
    # Creating a CatsTrie object
    mycattrie = CatsTrie(sentences)
    #
    # # Example 1.1
    # # A simple example
    # prompt = "ab"
    # mycattrie.autoComplete(prompt)
    # abazacy
    #
    # # Example 1.2
    # # Another simple example
    # prompt = "a"
    # mycattrie.autoComplete(prompt)
    # abazacy
    #
    # # Example 1.3 ok
    # # What if the prompt is the same as an existing sentence?
    # prompt = "dbcef"
    # mycattrie.autoComplete(prompt)
    # # dbcef
    #
    #
    # # Example 1.4 OK
    # # What if the length is longer?
    # prompt = "dbcefz"
    # mycattrie.autoComplete(prompt)
    # # None
    #
    # # Example 1.5 OK
    # # What if sentences doesn’t exist.
    # prompt = "ba"
    # mycattrie.autoComplete(prompt)
    # # None
    #
    # # Example 1.6
    # # A scenario where the tiebreaker is used
    prompt = "x"
    mycattrie.autoComplete(prompt)
    # # xyz
    #
    # # Example 1.7
    # # A scenario where the prompt is empty
    # prompt = ""
    # mycattrie.autoComplete(prompt)
    # # abazacy