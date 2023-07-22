# from a2t2 import CatsTrie
# from a2t2Final import CatsTrie
from Assignments.Assignment2.assignment2 import CatsTrie
import unittest


class GPTTests(unittest.TestCase):

    def test_edge_case_1(self):
        sentences = [
            "fg", "fg", "fg", "fg", "fg", "fg", "abc", "abc", "abc", "abc", "abc",
            "abdc", "abdc", "abdc", "abdz", "abdz", "abdz", "abdz", "ac", "ac", "ac", "ac", "ac"
        ]
        mycattrie = CatsTrie(sentences)
        self.assertEqual(mycattrie.autoComplete(""), "fg")
        self.assertEqual(mycattrie.autoComplete("z"), None)
        self.assertEqual(mycattrie.autoComplete("a"), "abc")
        self.assertEqual(mycattrie.autoComplete("ab"), "abc")
        self.assertEqual(mycattrie.autoComplete("abd"), "abdz")
        self.assertEqual(mycattrie.autoComplete("abdd"), None)
        self.assertEqual(mycattrie.autoComplete("bdz"), None)
        self.assertEqual(mycattrie.autoComplete("dz"), None)
        self.assertEqual(mycattrie.autoComplete("bc"), None)

    def test_edge_case_2(self):
        sentences = [
            "f", "f", "f", "f", "f", "f", "abca", "abca", "abca", "abca",
            "abc", "abc", "abc", "abc", "ad", "ad", "ad", "ad", "ad"
        ]
        mycattrie = CatsTrie(sentences)
        self.assertEqual(mycattrie.autoComplete("a"), "ad")
        self.assertEqual(mycattrie.autoComplete("abcd"), None)
    def test_edge_case_2_specific(self): #FAIL
        sentences = [
            "f", "f", "f", "f", "f", "f", "abca", "abca", "abca", "abca",
            "abc", "abc", "abc", "abc", "ad", "ad", "ad", "ad", "ad"
        ]
        mycattrie = CatsTrie(sentences)
        self.assertEqual(mycattrie.autoComplete(""), "f")
        self.assertEqual(mycattrie.autoComplete("abc"), "abc")


    def test_edgerunners_case_3(self):
        # Lyrics from I Really Want to Stay at Your House
        # Source: https://open.spotify.com/track/7mykoq6R3BArsSpNDjFQTm?si=ad96c59a91464936
        sentences = [
            'i', 'couldnt', 'wait', 'for', 'you', 'to', 'come', 'clear', 'the', 'cupboards',
            'but', 'now', 'youre', 'going', 'to', 'leave', 'with', 'nothing', 'but', 'a', 'sign',
            'another', 'evening', 'ill', 'be', 'sitting', 'reading', 'in', 'between', 'your', 'lines',
            'because', 'i', 'miss', 'you', 'all', 'the', 'time',

            'so', 'get', 'away',
            'another', 'way', 'to', 'feel', 'what', 'you', 'didnt', 'want', 'yourself', 'to', 'know',
            'and', 'let', 'yourself', 'go', 'you', 'know', 'you', 'didnt', 'lose', 'your', 'selfcontrol',
            'lets', 'start', 'at', 'the', 'rainbow',
            'turn', 'away',
            'another', 'way', 'to', 'be', 'where', 'you', 'didnt', 'want', 'yourself', 'to', 'go',
            'and', 'let', 'yourself', 'go',
            'is', 'that', 'a', 'compromise',

            'so', 'what', 'do', 'you', 'wanna', 'do', 'whats', 'your', 'pointofview',
            'theres', 'a', 'party', 'soon', 'do', 'you', 'wanna', 'go',
            'a', 'handshake', 'with', 'you', 'whats', 'your', 'pointofview',
            'im', 'on', 'top', 'of', 'you', 'i', 'dont', 'wanna', 'go',
            'cause', 'i', 'really', 'wanna', 'stay', 'at', 'your', 'house',
            'and', 'i', 'hope', 'this', 'works', 'out',
            'but', 'you', 'know', 'how', 'much', 'you', 'broke', 'me', 'apart',
            'im', 'done', 'with', 'you', 'im', 'ignoring', 'you',
            'i', 'dont', 'wanna', 'know',

            'and', 'im', 'aware', 'that', 'you', 'were', 'lying', 'in', 'the', 'gutter',
            'cause', 'i', 'did', 'everything', 'to', 'be', 'there', 'by', 'your', 'sideide',
            'so', 'when', 'you', 'tell', 'me', 'im', 'the', 'reason', 'i', 'just', 'cant', 'believe', 'the', 'lies',
            'and', 'why', 'do', 'i', 'so', 'want', 'to', 'call', 'you', 'call', 'you', 'call', 'you', 'call', 'you',

            'so', 'what', 'do', 'you', 'wanna', 'do', 'whats', 'your', 'pointofview',
            'theres', 'a', 'party', 'soon', 'do', 'you', 'wanna', 'go',
            'a', 'handshake', 'with', 'you', 'whats', 'your', 'pointofview',
            'im', 'on', 'top', 'of', 'you', 'i', 'dont', 'wanna', 'go',
            'cause', 'i', 'really', 'wanna', 'stay', 'at', 'your', 'house',
            'and', 'i', 'hope', 'this', 'works', 'out',
            'but', 'you', 'know', 'how', 'much', 'you', 'broke', 'me', 'apart',
            'im', 'done', 'with', 'you', 'im', 'ignoring', 'you',
            'i', 'dont', 'wanna', 'know',

            'oh',
            'ohoh', 'ohohoh',
            'i', 'dont', 'know', 'why', 'im', 'no', 'one',

            'so', 'get', 'away',
            'another', 'way', 'to', 'feel', 'what', 'you', 'didnt', 'want', 'yourself', 'to', 'know',
            'and', 'let', 'yourself', 'go',
            'you', 'know', 'you', 'didnt', 'lose', 'your', 'selfcontrol',
            'lets', 'start', 'at', 'the', 'rainbow',
            'turn', 'away',
            'another', 'way', 'to', 'be', 'where', 'you', 'didnt', 'want', 'yourself', 'to', 'go',
            'let', 'yourself', 'go',
            'is', 'that', 'a', 'compromise',

            'so', 'what', 'do', 'you', 'wanna', 'do', 'whats', 'your', 'pointofview',
            'theres', 'a', 'party', 'soon', 'do', 'you', 'wanna', 'go',
            'a', 'handshake', 'with', 'you', 'whats', 'your', 'pointofview',
            'im', 'on', 'top', 'of', 'you', 'i', 'dont', 'wanna', 'go',
            'cause', 'i', 'really', 'wanna', 'stay', 'at', 'your', 'house',
            'and', 'i', 'hope', 'this', 'works', 'out',
            'but', 'you', 'know', 'how', 'much', 'you', 'broke', 'me', 'apart',
            'im', 'done', 'with', 'you', 'im', 'ignoring', 'you',
            'i', 'dont', 'wanna', 'know'
        ]
        mycattrie = CatsTrie(sentences)
        self.assertEqual(mycattrie.autoComplete("b"), "but")
        self.assertEqual(mycattrie.autoComplete("c"), "call")
        self.assertEqual(mycattrie.autoComplete("e"), "evening")
        self.assertEqual(mycattrie.autoComplete("f"), "feel")
        self.assertEqual(mycattrie.autoComplete("h"), "handshake")
        self.assertEqual(mycattrie.autoComplete("j"), "just")
        self.assertEqual(mycattrie.autoComplete("k"), "know")
        self.assertEqual(mycattrie.autoComplete("m"), "me")
        self.assertEqual(mycattrie.autoComplete("o"), "of")
        self.assertEqual(mycattrie.autoComplete("p"), "pointofview")
        self.assertEqual(mycattrie.autoComplete("q"), None)
        self.assertEqual(mycattrie.autoComplete("r"), "really")
        self.assertEqual(mycattrie.autoComplete("u"), None)
        self.assertEqual(mycattrie.autoComplete("v"), None)
        self.assertEqual(mycattrie.autoComplete("w"), "wanna")
        self.assertEqual(mycattrie.autoComplete("x"), None)
        self.assertEqual(mycattrie.autoComplete("z"), None)
        self.assertEqual(mycattrie.autoComplete("control"), None)
        self.assertEqual(mycattrie.autoComplete("view"), None)

        self.assertEqual(mycattrie.autoComplete("don"), "dont")
        self.assertEqual(mycattrie.autoComplete("ing"), None)
        self.assertEqual(mycattrie.autoComplete("one"), "one")

    def test_edgerunners_case_3_specific(self): #Failed
        # Lyrics from I Really Want to Stay at Your House
        # Source: https://open.spotify.com/track/7mykoq6R3BArsSpNDjFQTm?si=ad96c59a91464936
        sentences = [
            'i', 'couldnt', 'wait', 'for', 'you', 'to', 'come', 'clear', 'the', 'cupboards',
            'but', 'now', 'youre', 'going', 'to', 'leave', 'with', 'nothing', 'but', 'a', 'sign',
            'another', 'evening', 'ill', 'be', 'sitting', 'reading', 'in', 'between', 'your', 'lines',
            'because', 'i', 'miss', 'you', 'all', 'the', 'time',

            'so', 'get', 'away',
            'another', 'way', 'to', 'feel', 'what', 'you', 'didnt', 'want', 'yourself', 'to', 'know',
            'and', 'let', 'yourself', 'go', 'you', 'know', 'you', 'didnt', 'lose', 'your', 'selfcontrol',
            'lets', 'start', 'at', 'the', 'rainbow',
            'turn', 'away',
            'another', 'way', 'to', 'be', 'where', 'you', 'didnt', 'want', 'yourself', 'to', 'go',
            'and', 'let', 'yourself', 'go',
            'is', 'that', 'a', 'compromise',

            'so', 'what', 'do', 'you', 'wanna', 'do', 'whats', 'your', 'pointofview',
            'theres', 'a', 'party', 'soon', 'do', 'you', 'wanna', 'go',
            'a', 'handshake', 'with', 'you', 'whats', 'your', 'pointofview',
            'im', 'on', 'top', 'of', 'you', 'i', 'dont', 'wanna', 'go',
            'cause', 'i', 'really', 'wanna', 'stay', 'at', 'your', 'house',
            'and', 'i', 'hope', 'this', 'works', 'out',
            'but', 'you', 'know', 'how', 'much', 'you', 'broke', 'me', 'apart',
            'im', 'done', 'with', 'you', 'im', 'ignoring', 'you',
            'i', 'dont', 'wanna', 'know',

            'and', 'im', 'aware', 'that', 'you', 'were', 'lying', 'in', 'the', 'gutter',
            'cause', 'i', 'did', 'everything', 'to', 'be', 'there', 'by', 'your', 'sideide',
            'so', 'when', 'you', 'tell', 'me', 'im', 'the', 'reason', 'i', 'just', 'cant', 'believe', 'the', 'lies',
            'and', 'why', 'do', 'i', 'so', 'want', 'to', 'call', 'you', 'call', 'you', 'call', 'you', 'call', 'you',

            'so', 'what', 'do', 'you', 'wanna', 'do', 'whats', 'your', 'pointofview',
            'theres', 'a', 'party', 'soon', 'do', 'you', 'wanna', 'go',
            'a', 'handshake', 'with', 'you', 'whats', 'your', 'pointofview',
            'im', 'on', 'top', 'of', 'you', 'i', 'dont', 'wanna', 'go',
            'cause', 'i', 'really', 'wanna', 'stay', 'at', 'your', 'house',
            'and', 'i', 'hope', 'this', 'works', 'out',
            'but', 'you', 'know', 'how', 'much', 'you', 'broke', 'me', 'apart',
            'im', 'done', 'with', 'you', 'im', 'ignoring', 'you',
            'i', 'dont', 'wanna', 'know',

            'oh',
            'ohoh', 'ohohoh',
            'i', 'dont', 'know', 'why', 'im', 'no', 'one',

            'so', 'get', 'away',
            'another', 'way', 'to', 'feel', 'what', 'you', 'didnt', 'want', 'yourself', 'to', 'know',
            'and', 'let', 'yourself', 'go',
            'you', 'know', 'you', 'didnt', 'lose', 'your', 'selfcontrol',
            'lets', 'start', 'at', 'the', 'rainbow',
            'turn', 'away',
            'another', 'way', 'to', 'be', 'where', 'you', 'didnt', 'want', 'yourself', 'to', 'go',
            'let', 'yourself', 'go',
            'is', 'that', 'a', 'compromise',

            'so', 'what', 'do', 'you', 'wanna', 'do', 'whats', 'your', 'pointofview',
            'theres', 'a', 'party', 'soon', 'do', 'you', 'wanna', 'go',
            'a', 'handshake', 'with', 'you', 'whats', 'your', 'pointofview',
            'im', 'on', 'top', 'of', 'you', 'i', 'dont', 'wanna', 'go',
            'cause', 'i', 'really', 'wanna', 'stay', 'at', 'your', 'house',
            'and', 'i', 'hope', 'this', 'works', 'out',
            'but', 'you', 'know', 'how', 'much', 'you', 'broke', 'me', 'apart',
            'im', 'done', 'with', 'you', 'im', 'ignoring', 'you',
            'i', 'dont', 'wanna', 'know'
        ]
        mycattrie = CatsTrie(sentences)
        self.assertEqual(mycattrie.autoComplete(""), "you")
        self.assertEqual(mycattrie.autoComplete("a"), "a")
        self.assertEqual(mycattrie.autoComplete("d"), "do")
        self.assertEqual(mycattrie.autoComplete("g"), "go")
        self.assertEqual(mycattrie.autoComplete("i"), "i")
        self.assertEqual(mycattrie.autoComplete("l"), "let")
        self.assertEqual(mycattrie.autoComplete("n"), "no")
        self.assertEqual(mycattrie.autoComplete("s"), "so")
        self.assertEqual(mycattrie.autoComplete("t"), "to")
        self.assertEqual(mycattrie.autoComplete("y"), "you")
        self.assertEqual(mycattrie.autoComplete("you"), "you")
        self.assertEqual(mycattrie.autoComplete("your"), "your")
        self.assertEqual(mycattrie.autoComplete("youre"), "youre")
        self.assertEqual(mycattrie.autoComplete("do"), "do")
        self.assertEqual(mycattrie.autoComplete("on"), "on")
        self.assertEqual(mycattrie.autoComplete("oh"), "oh")

if __name__ == "__main__":
    unittest.main()