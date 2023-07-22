import unittest
# from a2t2 import CatsTrie
# from a2t2Final import CatsTrie
from Assignments.Assignment2.assignment2 import CatsTrie


__author__ = "Compiled by Junru (William) Wei, last updated 21/05/2023"


class CatGPTTest(unittest.TestCase):

    def test_08(self):
        # Extract of the Constitution of the United States, Article I
        # Source: https://www.archives.gov/founding-docs/constitution-transcript
        sentences = [

            "we", "the", "people", "of", "the", "united", "states", "in", "order", "to", "form", "a", "more", "perfect",
            "union", "establish", "justice", "insure", "domestic", "tranquility", "provide", "for", "the", "common",
            "defence", "promote", "the", "general", "welfare", "and", "secure", "the", "blessings", "of", "liberty", "to",
            "ourselves", "and", "our", "posterity", "do", "ordain", "and", "establish", "this", "constitution", "for",
            "the", "united", "states", "of", "america",

            "article", "one",

            "section", "one",

            "all", "legislative", "powers", "herein", "granted", "shall", "be", "vested", "in", "a", "congress", "of",
            "the", "united", "states", "which", "shall", "consist", "of", "a", "senate", "and", "house", "of",
            "representatives",

            "section", "two",

            "the", "house", "of", "representatives", "shall", "be", "composed", "of", "members", "chosen", "every",
            "second", "year", "by", "the", "people", "of", "the", "several", "states", "and", "the", "electors", "in",
            "each", "state", "shall", "have", "the", "qualifications", "requisite", "for", "electors", "of", "the", "most",
            "numerous", "branch", "of", "the", "state", "legislature",
            "no", "person", "shall", "be", "a", "representative", "who", "shall", "not", "have", "attained", "to", "the",
            "age", "of", "twenty", "five", "years", "and", "been", "seven", "years", "a", "citizen", "of", "the", "united",
            "states", "and", "who", "shall", "not", "when", "elected", "be", "an", "inhabitant", "of", "that", "state",
            "in", "which", "he", "shall", "be", "chosen",
            "representatives", "and", "direct", "taxes", "shall", "be", "apportioned", "among", "the", "several", "states",
            "which", "may", "be", "included", "within", "this", "union", "according", "to", "their", "respective",
            "numbers", "which", "shall", "be", "determined", "by", "adding", "to", "the", "whole", "number", "of", "free",
            "persons", "including", "those", "bound", "to", "service", "for", "a", "term", "of", "years", "and",
            "excluding", "indians", "not", "taxed", "three", "fifths", "of", "all", "other", "persons", "the", "actual",
            "enumeration", "shall", "be", "made", "within", "three", "years", "after", "the", "first", "meeting", "of",
            "the", "congress", "of", "the", "united", "states", "and", "within", "every", "subsequent", "term", "of", "ten",
            "years", "in", "such", "manner", "as", "they", "shall", "by", "law", "direct", "the", "number", "of",
            "representatives", "shall", "not", "exceed", "one", "for", "every", "thirty", "thousand", "but", "each",
            "state", "shall", "have", "at", "least", "one", "representative", "and", "until", "such", "enumeration",
            "shall", "be", "made", "the", "state", "of", "new", "hampshire", "shall", "be", "entitled", "to", "chuse",
            "three", "massachusetts", "eight", "rhodeisland", "and", "providence", "plantations", "one", "connecticut",
            "five", "newyork", "six", "new", "jersey", "four", "pennsylvania", "eight", "delaware", "one", "maryland",
            "six", "virginia", "ten", "north", "carolina", "five", "south", "carolina", "five", "and", "georgia", "three",
            "when", "vacancies", "happen", "in", "the", "representation", "from", "any", "state", "the", "executive",
            "authority", "thereof", "shall", "issue", "writs", "of", "election", "to", "fill", "such", "vacancies",
            "the", "house", "of", "representatives", "shall", "chuse", "their", "speaker", "and", "other", "officers",
            "and", "shall", "have", "the", "sole", "power", "of", "impeachment",

            "section", "three",

            "the", "senate", "of", "the", "united", "states", "shall", "be", "composed", "of", "two", "senators", "from",
            "each", "state", "chosen", "by", "the", "legislature", "thereof", "for", "six", "years", "and", "each",
            "senator", "shall", "have", "one", "vote",
            "immediately", "after", "they", "shall", "be", "assembled", "in", "consequence", "of", "the", "first",
            "election", "they", "shall", "be", "divided", "as", "equally", "as", "may", "be", "into", "three", "classes",
            "the", "seats", "of", "the", "senators", "of", "the", "first", "class", "shall", "be", "vacated", "at", "the",
            "expiration", "of", "the", "second", "year", "of", "the", "second", "class", "at", "the", "expiration", "of",
            "the", "fourth", "year", "and", "of", "the", "third", "class", "at", "the", "expiration", "of", "the", "sixth",
            "year", "so", "that", "one", "third", "may", "be", "chosen", "every", "second", "year", "and", "if",
            "vacancies", "happen", "by", "resignation", "or", "otherwise", "during", "the", "recess", "of", "the",
            "legislature", "of", "any", "state", "the", "executive", "thereof", "may", "make", "temporary", "appointments",
            "until", "the", "next", "meeting", "of", "the", "legislature", "which", "shall", "then", "fill", "such",
            "vacancies",
            "no", "person", "shall", "be", "a", "senator", "who", "shall", "not", "have", "attained", "to", "the", "age",
            "of", "thirty", "years", "and", "been", "nine", "years", "a", "citizen", "of", "the", "united", "states", "and",
            "who", "shall", "not", "when", "elected", "be", "an", "inhabitant", "of", "that", "state", "for", "which", "he",
            "shall", "be", "chosen",
            "the", "vice", "president", "of", "the", "united", "states", "shall", "be", "president", "of", "the", "senate",
            "but", "shall", "have", "no", "vote", "unless", "they", "be", "equally", "divided",
            "the", "senate", "shall", "chuse", "their", "other", "officers", "and", "also", "a", "president", "pro",
            "tempore", "in", "the", "absence", "of", "the", "vice", "president", "or", "when", "he", "shall", "exercise",
            "the", "office", "of", "president", "of", "the", "united", "states",
            "the", "senate", "shall", "have", "the", "sole", "power", "to", "try", "all", "impeachments", "when", "sitting",
            "for", "that", "purpose", "they", "shall", "be", "on", "oath", "or", "affirmation", "when", "the", "president",
            "of", "the", "united", "states", "is", "tried", "the", "chief", "justice", "shall", "preside", "and", "no",
            "person", "shall", "be", "convicted", "without", "the", "concurrence", "of", "two", "thirds", "of", "the",
            "members", "present",
            "judgment", "in", "cases", "of", "impeachment", "shall", "not", "extend", "further", "than", "to", "removal",
            "from", "office", "and", "disqualification", "to", "hold", "and", "enjoy", "any", "office", "of", "honor",
            "trust", "or", "profit", "under", "the", "united", "states", "but", "the", "party", "convicted", "shall",
            "nevertheless", "be", "liable", "and", "subject", "to", "indictment", "trial", "judgment", "and", "punishment",
            "according", "to", "law",

            "section", "four",

            "the", "times", "places", "and", "manner", "of", "holding", "elections", "for", "senators", "and",
            "representatives", "shall", "be", "prescribed", "in", "each", "state", "by", "the", "legislature", "thereof",
            "but", "the", "congress", "may", "at", "any", "time", "by", "law", "make", "or", "alter", "such", "regulations",
            "except", "as", "to", "the", "places", "of", "chusing", "senators",
            "the", "congress", "shall", "assemble", "at", "least", "once", "in", "every", "year", "and", "such", "meeting",
            "shall", "be", "on", "the", "first", "monday", "in", "december", "unless", "they", "shall", "by", "law",
            "appoint", "a", "different", "day",

            "section", "five",

            "each", "house", "shall", "be", "the", "judge", "of", "the", "elections", "returns", "and", "qualifications",
            "of", "its", "own", "members", "and", "a", "majority", "of", "each", "shall", "constitute", "a", "quorum", "to",
            "do", "business", "but", "a", "smaller", "number", "may", "adjourn", "from", "day", "to", "day", "and", "may",
            "be", "authorized", "to", "compel", "the", "attendance", "of", "absent", "members", "in", "such", "manner",
            "and", "under", "such", "penalties", "as", "each", "house", "may", "provide",
            "each", "house", "may", "determine", "the", "rules", "of", "its", "proceedings", "punish", "its", "members",
            "for", "disorderly", "behaviour", "and", "with", "the", "concurrence", "of", "two", "thirds", "expel", "a",
            "member",
            "each", "house", "shall", "keep", "a", "journal", "of", "its", "proceedings", "and", "from", "time", "to",
            "time", "publish", "the", "same", "excepting", "such", "parts", "as", "may", "in", "their", "judgment",
            "require", "secrecy", "and", "the", "yeas", "and", "nays", "of", "the", "members", "of", "either", "house",
            "on", "any", "question", "shall", "at", "the", "desire", "of", "one", "fifth", "of", "those", "present", "be",
            "entered", "on", "the", "journal",
            "neither", "house", "during", "the", "session", "of", "congress", "shall", "without", "the", "consent", "of",
            "the", "other", "adjourn", "for", "more", "than", "three", "days", "nor", "to", "any", "other", "place", "than",
            "that", "in", "which", "the", "two", "houses", "shall", "be", "sitting",

            "section", "six",

            "the", "senators", "and", "representatives", "shall", "receive", "a", "compensation", "for", "their",
            "services", "to", "be", "ascertained", "by", "law", "and", "paid", "out", "of", "the", "treasury", "of", "the",
            "united", "states", "they", "shall", "in", "all", "cases", "except", "treason", "felony", "and", "breach", "of",
            "the", "peace", "be", "privileged", "from", "arrest", "during", "their", "attendance", "at", "the", "session",
            "of", "their", "respective", "houses", "and", "in", "going", "to", "and", "returning", "from", "the", "same",
            "and", "for", "any", "speech", "or", "debate", "in", "either", "house", "they", "shall", "not", "be",
            "questioned", "in", "any", "other", "place",
            "no", "senator", "or", "representative", "shall", "during", "the", "time", "for", "which", "he", "was",
            "elected", "be", "appointed", "to", "any", "civil", "office", "under", "the", "authority", "of", "the",
            "united", "states", "which", "shall", "have", "been", "created", "or", "the", "emoluments", "whereof", "shall",
            "have", "been", "encreased", "during", "such", "time", "and", "no", "person", "holding", "any", "office",
            "under", "the", "united", "states", "shall", "be", "a", "member", "of", "either", "house", "during", "his",
            "continuance", "in", "office",

            "section", "seven",

            "all", "bills", "for", "raising", "revenue", "shall", "originate", "in", "the", "house", "of",
            "representatives", "but", "the", "senate", "may", "propose", "or", "concur", "with", "amendments", "as", "on",
            "other", "bills",
            "every", "bill", "which", "shall", "have", "passed", "the", "house", "of", "representatives", "and", "the",
            "senate", "shall", "before", "it", "become", "a", "law", "be", "presented", "to", "the", "president", "of",
            "the", "united", "states", "if", "he", "approve", "he", "shall", "sign", "it", "but", "if", "not", "he",
            "shall", "return", "it", "with", "his", "objections", "to", "that", "house", "in", "which", "it", "shall",
            "have", "originated", "who", "shall", "enter", "the", "objections", "at", "large", "on", "their", "journal",
            "and", "proceed", "to", "reconsider", "it", "if", "after", "such", "reconsideration", "two", "thirds", "of",
            "that", "house", "shall", "agree", "to", "pass", "the", "bill", "it", "shall", "be", "sent", "together", "with",
            "the", "objections", "to", "the", "other", "house", "by", "which", "it", "shall", "likewise", "be",
            "reconsidered", "and", "if", "approved", "by", "two", "thirds", "of", "that", "house", "it", "shall", "become",
            "a", "law", "but", "in", "all", "such", "cases", "the", "votes", "of", "both", "houses", "shall", "be",
            "determined", "by", "yeas", "and", "nays", "and", "the", "names", "of", "the", "persons", "voting", "for",
            "and", "against", "the", "bill", "shall", "be", "entered", "on", "the", "journal", "of", "each", "house",
            "respectively", "if", "any", "bill", "shall", "not", "be", "returned", "by", "the", "president", "within",
            "ten", "days", "sundays", "excepted", "after", "it", "shall", "have", "been", "presented", "to", "him", "the",
            "same", "shall", "be", "a", "law", "in", "like", "manner", "as", "if", "he", "had", "signed", "it", "unless",
            "the", "congress", "by", "their", "adjournment", "prevent", "its", "return", "in", "which", "case", "it",
            "shall", "not", "be", "a", "law",
            "every", "order", "resolution", "or", "vote", "to", "which", "the", "concurrence", "of", "the", "senate", "and",
            "house", "of", "representatives", "may", "be", "necessary", "except", "on", "a", "question", "of",
            "adjournment", "shall", "be", "presented", "to", "the", "president", "of", "the", "united", "states", "and",
            "before", "the", "same", "shall", "take", "effect", "shall", "be", "approved", "by", "him", "or", "being",
            "disapproved", "by", "him", "shall", "be", "repassed", "by", "two", "thirds", "of", "the", "senate", "and",
            "house", "of", "representatives", "according", "to", "the", "rules", "and", "limitations", "prescribed", "in",
            "the", "case", "of", "a", "bill",

            "section", "eight",

            "the", "congress", "shall", "have", "power", "to", "lay", "and", "collect", "taxes", "duties", "imposts", "and",
            "excises", "to", "pay", "the", "debts", "and", "provide", "for", "the", "common", "defence", "and", "general",
            "welfare", "of", "the", "united", "states", "but", "all", "duties", "imposts", "and", "excises", "shall", "be",
            "uniform", "throughout", "the", "united", "states",
            "to", "borrow", "money", "on", "the", "credit", "of", "the", "united", "states",
            "to", "regulate", "commerce", "with", "foreign", "nations", "and", "among", "the", "several", "states", "and",
            "with", "the", "indian", "tribes",
            "to", "establish", "an", "uniform", "rule", "of", "naturalization", "and", "uniform", "laws", "on", "the",
            "subject", "of", "bankruptcies", "throughout", "the", "united", "states",
            "to", "coin", "money", "regulate", "the", "value", "thereof", "and", "of", "foreign", "coin", "and", "fix",
            "the", "standard", "of", "weights", "and", "measures",
            "to", "provide", "for", "the", "punishment", "of", "counterfeiting", "the", "securities", "and", "current",
            "coin", "of", "the", "united", "states",
            "to", "establish", "post", "offices", "and", "post", "roads",
            "to", "promote", "the", "progress", "of", "science", "and", "useful", "arts", "by", "securing", "for",
            "limited", "times", "to", "authors", "and", "inventors", "the", "exclusive", "right", "to", "their",
            "respective", "writings", "and", "discoveries",
            "to", "constitute", "tribunals", "inferior", "to", "the", "supreme", "court",
            "to", "define", "and", "punish", "piracies", "and", "felonies", "committed", "on", "the", "high", "seas", "and",
            "offences", "against", "the", "law", "of", "nations",
            "to", "declare", "war", "grant", "letters", "of", "marque", "and", "reprisal", "and", "make", "rules",
            "concerning", "captures", "on", "land", "and", "water",
            "to", "raise", "and", "support", "armies", "but", "no", "appropriation", "of", "money", "to", "that", "use",
            "shall", "be", "for", "a", "longer", "term", "than", "two", "years",
            "to", "provide", "and", "maintain", "a", "navy",
            "to", "make", "rules", "for", "the", "government", "and", "regulation", "of", "the", "land", "and", "naval",
            "forces",
            "to", "provide", "for", "calling", "forth", "the", "militia", "to", "execute", "the", "laws", "of", "the",
            "union", "suppress", "insurrections", "and", "repel", "invasions",
            "to", "provide", "for", "organizing", "arming", "and", "disciplining", "the", "militia", "and", "for",
            "governing", "such", "part", "of", "them", "as", "may", "be", "employed", "in", "the", "service", "of", "the",
            "united", "states", "reserving", "to", "the", "states", "respectively", "the", "appointment", "of", "the",
            "officers", "and", "the", "authority", "of", "training", "the", "militia", "according", "to", "the",
            "discipline", "prescribed", "by", "congress",
            "to", "exercise", "exclusive", "legislation", "in", "all", "cases", "whatsoever", "over", "such", "district",
            "not", "exceeding", "ten", "miles", "square", "as", "may", "by", "cession", "of", "particular", "states", "and",
            "the", "acceptance", "of", "congress", "become", "the", "seat", "of", "the", "government", "of", "the",
            "united", "states", "and", "to", "exercise", "like", "authority", "over", "all", "places", "purchased", "by",
            "the", "consent", "of", "the", "legislature", "of", "the", "state", "in", "which", "the", "same", "shall", "be",
            "for", "the", "erection", "of", "forts", "magazines", "arsenals", "dockyards", "and", "other", "needful",
            "buildingsand",
            "to", "make", "all", "laws", "which", "shall", "be", "necessary", "and", "proper", "for", "carrying", "into",
            "execution", "the", "foregoing", "powers", "and", "all", "other", "powers", "vested", "by", "this",
            "constitution", "in", "the", "government", "of", "the", "united", "states", "or", "in", "any", "department",
            "or", "officer", "thereof",

            "section", "nine",

            "the", "migration", "or", "importation", "of", "such", "persons", "as", "any", "of", "the", "states", "now",
            "existing", "shall", "think", "proper", "to", "admit", "shall", "not", "be", "prohibited", "by", "the",
            "congress", "prior", "to", "the", "year", "one", "thousand", "eight", "hundred", "and", "eight", "but", "a",
            "tax", "or", "duty", "may", "be", "imposed", "on", "such", "importation", "not", "exceeding", "ten", "dollars",
            "for", "each", "person",
            "the", "privilege", "of", "the", "writ", "of", "habeas", "corpus", "shall", "not", "be", "suspended", "unless",
            "when", "in", "cases", "of", "rebellion", "or", "invasion", "the", "public", "safety", "may", "require", "it",
            "no", "bill", "of", "attainder", "or", "ex", "post", "facto", "law", "shall", "be", "passed",
            "no", "capitation", "or", "other", "direct", "tax", "shall", "be", "laid", "unless", "in", "proportion", "to",
            "the", "census", "or", "enumeration", "herein", "before", "directed", "to", "be", "taken",
            "no", "tax", "or", "duty", "shall", "be", "laid", "on", "articles", "exported", "from", "any", "state",
            "no", "preference", "shall", "be", "given", "by", "any", "regulation", "of", "commerce", "or", "revenue", "to",
            "the", "ports", "of", "one", "state", "over", "those", "of", "another", "nor", "shall", "vessels", "bound",
            "to", "or", "from", "one", "state", "be", "obliged", "to", "enter", "clear", "or", "pay", "duties", "in",
            "another",
            "no", "money", "shall", "be", "drawn", "from", "the", "treasury", "but", "in", "consequence", "of",
            "appropriations", "made", "by", "law", "and", "a", "regular", "statement", "and", "account", "of", "the",
            "receipts", "and", "expenditures", "of", "all", "public", "money", "shall", "be", "published", "from", "time",
            "to", "time",
            "no", "title", "of", "nobility", "shall", "be", "granted", "by", "the", "united", "states", "and", "no",
            "person", "holding", "any", "office", "of", "profit", "or", "trust", "under", "them", "shall", "without", "the",
            "consent", "of", "the", "congress", "accept", "of", "any", "present", "emolument", "office", "or", "title",
            "of", "any", "kind", "whatever", "from", "any", "king", "prince", "or", "foreign", "state",

            "section", "ten",

            "no", "state", "shall", "enter", "into", "any", "treaty", "alliance", "or", "confederation", "grant", "letters",
            "of", "marque", "and", "reprisal", "coin", "money", "emit", "bills", "of", "credit", "make", "any", "thing",
            "but", "gold", "and", "silver", "coin", "a", "tender", "in", "payment", "of", "debts", "pass", "any", "bill",
            "of", "attainder", "ex", "post", "facto", "law", "or", "law", "impairing", "the", "obligation", "of",
            "contracts", "or", "grant", "any", "title", "of", "nobility",
            "no", "state", "shall", "without", "the", "consent", "of", "the", "congress", "lay", "any", "imposts", "or",
            "duties", "on", "imports", "or", "exports", "except", "what", "may", "be", "absolutely", "necessary", "for",
            "executing", "its", "inspection", "laws", "and", "the", "net", "produce", "of", "all", "duties", "and",
            "imposts", "laid", "by", "any", "state", "on", "imports", "or", "exports", "shall", "be", "for", "the", "use",
            "of", "the", "treasury", "of", "the", "united", "states", "and", "all", "such", "laws", "shall", "be",
            "subject", "to", "the", "revision", "and", "controul", "of", "the", "congress",
            "no", "state", "shall", "without", "the", "consent", "of", "congress", "lay", "any", "duty", "of", "tonnage",
            "keep", "troops", "or", "ships", "of", "war", "in", "time", "of", "peace", "enter", "into", "any", "agreement",
            "or", "compact", "with", "another", "state", "or", "with", "a", "foreign", "power", "or", "engage", "in", "war",
            "unless", "actually", "invaded", "or", "in", "such", "imminent", "danger", "as", "will", "not", "admit", "of",
            "delay"

        ]
        trie = CatsTrie(sentences)
        self.assertTrue(trie.autoComplete("") == "the")
        self.assertTrue(trie.autoComplete("monash") == None)  # :(
        self.assertTrue(trie.autoComplete("a") == "and")
        self.assertTrue(trie.autoComplete("al") == "all")
        self.assertTrue(trie.autoComplete("any") == "any")
        self.assertTrue(trie.autoComplete("b") == "be")
        self.assertTrue(trie.autoComplete("by") == "by")
        self.assertTrue(trie.autoComplete("c") == "congress")
        self.assertTrue(trie.autoComplete("d") == "during")
        self.assertTrue(trie.autoComplete("e") == "each")
        self.assertTrue(trie.autoComplete("f") == "for")
        self.assertTrue(trie.autoComplete("g") == "government")
        self.assertTrue(trie.autoComplete("h") == "house")
        self.assertTrue(trie.autoComplete("ha") == "have")
        self.assertTrue(trie.autoComplete("i") == "in")
        self.assertTrue(trie.autoComplete("j") == "journal")
        self.assertTrue(trie.autoComplete("k") == "keep")
        self.assertTrue(trie.autoComplete("l") == "law")
        self.assertTrue(trie.autoComplete("m") == "may")
        self.assertTrue(trie.autoComplete("n") == "no")
        self.assertTrue(trie.autoComplete("not") == "not")
        self.assertTrue(trie.autoComplete("o") == "of")
        self.assertTrue(trie.autoComplete("on") == "on")
        self.assertTrue(trie.autoComplete("or") == "or")
        self.assertTrue(trie.autoComplete("p") == "president")
        self.assertTrue(trie.autoComplete("q") == "qualifications")
        self.assertTrue(trie.autoComplete("r") == "representatives")
        self.assertTrue(trie.autoComplete("s") == "shall")
        self.assertTrue(trie.autoComplete("st") == "states")
        self.assertTrue(trie.autoComplete("su") == "such")
        self.assertTrue(trie.autoComplete("t") == "the")
        self.assertTrue(trie.autoComplete("to") == "to")
        self.assertTrue(trie.autoComplete("u") == "united")
        self.assertTrue(trie.autoComplete("v") == "vacancies")
        self.assertTrue(trie.autoComplete("w") == "which")
        self.assertTrue(trie.autoComplete("x") == None)
        self.assertTrue(trie.autoComplete("y") == "years")
        self.assertTrue(trie.autoComplete("z") == None)


    def test_09(self):
        # Extract from the FIT2004 S1 2023 A2 assignment brief, Monash University
        sentences = [

            "fit", "two", "zero", "zero", "four", "s", "one", "twenty", "twenty", "three", "assignment", "two",

            "deadline",

            "friday", "twenty", "sixth", "may", "twenty", "twenty", "three", "sixteen", "thirty", "sharp", "aedt",

            "late", "submission", "penalty",

            "ten", "percent", "penalty", "per", "day", "submissions", "more", "than", "seven", "calendar", "days", "late",
            "will", "receive", "zero", "the", "number", "of", "days", "late", "is", "rounded", "up", "eg", "five",
            "minutes", "late", "means", "one", "day", "late", "twenty", "seven", "hours", "late", "is", "two", "days",
            "late",
            "for", "special", "consideration", "please", "visit", "the", "following", "page", "and", "fill", "out", "the",
            "appropriate", "form",
            "https", "colon", "slash", "slash", "forms", "dot", "monash", "dot", "edu", "slash", "special", "hyphen",
            "consideration", "for", "clayton", "students",
            "https", "colon", "slash", "slash", "sors", "dot", "monash", "dot", "edu", "dot", "my", "slash", "for",
            "malaysian", "students",
            "the", "deadlines", "in", "this", "unit", "are", "strict", "last", "minute", "submissions", "are", "at", "your",
            "own", "risk",

            "programming", "criteria",

            "it", "is", "required", "that", "you", "implement", "this", "exercise", "strictly", "using", "the", "python",
            "programming", "language", "version", "should", "not", "be", "earlier", "than", "three", "point", "five",
            "this", "practical", "work", "will", "be", "marked", "on", "the", "time", "complexity", "space", "complexity",
            "and", "functionality", "of", "your", "program", "and", "your", "documentation",
            "your", "program", "will", "be", "tested", "using", "automated", "test", "scripts", "it", "is", "therefore",
            "critically", "important", "that", "you", "name", "your", "files", "and", "functions", "as", "specified", "in",
            "this", "document", "if", "you", "do", "not", "it", "will", "make", "your", "submission", "difficult", "to",
            "mark", "and", "you", "will", "be", "penalised",

            "submission", "requirement",

            "you", "will", "submit", "a", "single", "python", "file", "assignment", "two", "dot", "py", "moodle", "will",
            "not", "accept", "submissions", "of", "other", "file", "types",

            "plagiarism",

            "the", "assignments", "will", "be", "checked", "for", "plagiarism", "using", "an", "advanced", "plagiarism",
            "detector", "in", "previous", "semesters", "many", "students", "were", "detected", "by", "the", "plagiarism",
            "detector", "and", "almost", "all", "got", "zero", "mark", "for", "the", "assignment", "or", "even", "zero",
            "marks", "for", "the", "unit", "as", "penalty", "and", "as", "a", "result", "the", "large", "majority", "of",
            "those", "students", "failed", "the", "unit", "helping", "others", "to", "solve", "the", "assignment", "is",
            "not", "accepted", "please", "do", "not", "share", "your", "solutions", "partially", "or", "completely", "to",
            "others", "using", "contents", "from", "the", "internet", "books", "etc", "without", "citing", "is",
            "plagiarism", "if", "you", "use", "such", "content", "as", "part", "of", "your", "solution", "and", "properly",
            "cite", "it", "it", "is", "not", "plagiarism", "but", "you", "wouldnt", "be", "getting", "any", "marks", "that",
            "are", "possibly", "assigned", "for", "that", "part", "of", "the", "task", "as", "it", "is", "not", "your",
            "own", "work",

            "the", "use", "of", "generative", "ai", "and", "similar", "tools", "is", "not", "allowed", "in", "this", "unit",

            "end", "of", "page", "one",

            "learning", "outcomes",

            "this", "assignment", "achieves", "the", "learning", "outcomes", "of",
            "one", "analyse", "general", "problem", "solving", "strategies", "and", "algorithmic", "paradigms", "and",
            "apply", "them", "to", "solving", "new", "problems",
            "two", "prove", "correctness", "of", "programs", "analyse", "their", "space", "and", "time", "complexities",
            "three", "compare", "and", "contrast", "various", "abstract", "data", "types", "and", "use", "them",
            "appropriately",
            "four", "develop", "and", "implement", "algorithms", "to", "solve", "computational", "problems",

            "in", "addition", "you", "will", "develop", "the", "following", "employability", "skills",
            "text", "comprehension",
            "designing", "test", "cases",
            "ability", "to", "follow", "specifications", "precisely",

            "assignment", "timeline",

            "in", "order", "to", "be", "successful", "in", "this", "assessment", "the", "following", "steps", "are",
            "provided", "as", "a", "suggestion", "this", "is", "an", "approach", "which", "will", "be", "useful", "to",
            "you", "both", "in", "future", "units", "and", "in", "industry",

            "planning",

            "one", "read", "the", "assignment", "specification", "as", "soon", "as", "possible", "and", "write", "out", "a",
            "list", "of", "questions", "you", "have", "about", "it",
            "two", "try", "to", "resolve", "these", "questions", "by", "viewing", "the", "faq", "on", "ed", "or", "by",
            "thinking", "through", "the", "problems", "over", "time",
            "three", "as", "soon", "as", "possible", "start", "thinking", "about", "the", "problems", "in", "the",
            "assignment",
            "it", "is", "strongly", "recommended", "that", "you", "do", "not", "write", "code", "until", "you", "have", "a",
            "solid", "feeling", "for", "how", "the", "problem", "works", "and", "how", "you", "will", "solve", "it",
            "four", "writing", "down", "small", "examples", "and", "solving", "them", "by", "hand", "is", "an", "excellent",
            "tool", "for", "coming", "to", "a", "better", "understanding", "of", "the", "problem",
            "as", "you", "are", "doing", "this", "you", "will", "also", "get", "a", "feel", "for", "the", "kinds", "of",
            "edge", "cases", "your", "code", "will", "have", "to", "deal", "with",
            "five", "write", "down", "a", "highlevel", "description", "of", "the", "algorithm", "you", "will", "use",
            "six", "determine", "the", "complexity", "of", "your", "algorithm", "idea", "ensuring", "it", "meets", "the",
            "requirements",

            "end", "of", "page", "two",

            "implementing",

            "one", "think", "of", "test", "cases", "that", "you", "can", "use", "to", "check", "if", "your", "algorithm",
            "works",
            "use", "the", "edge", "cases", "you", "found", "during", "the", "previous", "phase", "to", "inspire", "your",
            "test", "cases",
            "it", "is", "also", "a", "good", "idea", "to", "generate", "large", "random", "test", "cases",
            "sharing", "test", "cases", "is", "allowed", "as", "it", "is", "not", "helping", "solve", "the", "assignment",
            "two", "code", "up", "your", "algorithm", "remember", "decomposition", "and", "comments", "and", "test", "it",
            "on", "the", "tests", "you", "have", "thought", "of",
            "three", "try", "to", "break", "your", "code", "think", "of", "what", "kinds", "of", "inputs", "you", "could",
            "be", "presented", "with", "which", "your", "code", "might", "not", "be", "able", "to", "handle",
            "large", "inputs",
            "small", "inputs",
            "inputs", "with", "strange", "properties",
            "what", "if", "everything", "is", "the", "same",
            "what", "if", "everything", "is", "different",
            "etc",

            "before", "submission",

            "make", "sure", "that", "the", "inputoutput", "format", "of", "your", "code", "matches", "the", "specification",
            "make", "sure", "your", "filenames", "match", "the", "specification",
            "make", "sure", "your", "functions", "are", "named", "correctly", "and", "take", "the", "correct", "inputs",
            "remove", "print", "statements", "and", "test", "code", "from", "the", "file", "you", "are", "going", "to",
            "submit",

            "end", "of", "page", "three",

            "documentation",

            "for", "this", "assignment", "and", "all", "assignments", "in", "this", "unit", "you", "are", "required", "to",
            "document", "and", "comment", "your", "code", "appropriately", "whilst", "part", "of", "the", "marks", "of",
            "each", "question", "are", "for", "documentation", "there", "is", "a", "baseline", "level", "of",
            "documentation", "you", "must", "have", "in", "order", "for", "your", "code", "to", "receive", "marks",
            "in", "other", "words",
            "insufficient", "documentation", "might", "result", "in", "you", "getting", "zero", "for", "the", "entire",
            "question", "for", "which", "it", "is", "insufficient",
            "this", "documentationcommenting", "must", "consist", "of", "but", "is", "not", "limited", "to",
            "for", "each", "function", "highlevel", "description", "of", "that", "function", "this", "should", "be", "a",
            "two", "or", "three", "sentence", "explanation", "of", "what", "this", "function", "does",
            "your", "main", "function", "in", "the", "assignment", "should", "contain", "a", "generalised", "description",
            "of", "the", "approach", "your", "solution", "uses", "to", "solve", "the", "assignment", "task",
            "for", "each", "function", "specify", "what", "the", "input", "to", "the", "function", "is", "and", "what",
            "output", "the", "function", "produces", "or", "returns", "if", "appropriate",
            "for", "each", "function", "the", "appropriate", "big", "oh", "or", "big", "theta", "time", "and", "space",
            "complexity", "of", "that", "function", "in", "terms", "of", "the", "input", "size", "make", "sure", "you",
            "specify", "what", "the", "variables", "involved", "in", "your", "complexity", "refer", "to", "remember",
            "that", "the", "complexity", "of", "a", "function", "includes", "the", "complexity", "of", "any", "function",
            "calls", "it", "makes",
            "within", "functions", "comments", "where", "appropriate", "generally", "speaking", "you", "would", "comment",
            "complicated", "lines", "of", "code", "which", "you", "should", "try", "to", "minimise", "or", "a", "large",
            "block", "of", "code", "which", "performs", "a", "clear", "and", "distinct", "task", "often", "blocks", "like",
            "this", "are", "good", "candidates", "to", "be",
            "their", "own", "functions",

            "a", "suggested", "function", "documentation", "layout", "would", "be", "as", "follows",

            "def", "my", "underscore", "function", "left", "bracket", "argv", "one", "comma", "argv", "two", "right",
            "bracket", "colon",
            "start", "of", "comment", "block",
            "function", "description",
            "approach", "description", "if", "main", "function",
            "input",
            "argv", "one",
            "argv", "two",
            "output", "return", "or", "postcondition",
            "time", "complexity",
            "aux", "space", "complexity",
            "end", "of", "comment", "block",
            "then", "write", "your", "codes", "here",

            "there", "is", "a", "documentation", "guide", "available", "on", "moodle", "in", "the", "assignment", "section",
            "which", "contains", "a", "demonstration", "of", "how", "to", "document", "code", "to", "the", "level",
            "required", "in", "the", "unit",

            "end", "of", "page", "four"

        ]
        trie = CatsTrie(sentences)
        self.assertTrue(trie.autoComplete("") == "the")
        self.assertTrue(trie.autoComplete("a") == "and")
        self.assertTrue(trie.autoComplete("b") == "be")
        self.assertTrue(trie.autoComplete("c") == "code")
        self.assertTrue(trie.autoComplete("d") == "documentation")
        self.assertTrue(trie.autoComplete("e") == "end")
        self.assertTrue(trie.autoComplete("f") == "for")
        self.assertTrue(trie.autoComplete("g") == "getting")
        self.assertTrue(trie.autoComplete("h") == "have")
        self.assertTrue(trie.autoComplete("i") == "is")
        self.assertTrue(trie.autoComplete("j") == None)
        self.assertTrue(trie.autoComplete("k") == "kinds")
        self.assertTrue(trie.autoComplete("l") == "late")
        self.assertTrue(trie.autoComplete("m") == "make")
        self.assertTrue(trie.autoComplete("n") == "not")
        self.assertTrue(trie.autoComplete("o") == "of")
        self.assertTrue(trie.autoComplete("p") == "plagiarism")
        self.assertTrue(trie.autoComplete("q") == "question")
        self.assertTrue(trie.autoComplete("r") == "required")
        self.assertTrue(trie.autoComplete("s") == "slash")
        self.assertTrue(trie.autoComplete("t") == "the")
        self.assertTrue(trie.autoComplete("u") == "unit")
        self.assertTrue(trie.autoComplete("v") == "variables")
        self.assertTrue(trie.autoComplete("w") == "will")
        self.assertTrue(trie.autoComplete("x") == None)
        self.assertTrue(trie.autoComplete("y") == "you")
        self.assertTrue(trie.autoComplete("z") == "zero")
        self.assertTrue(trie.autoComplete("ab") == "about")
        self.assertTrue(trie.autoComplete("ac") == "accept")
        self.assertTrue(trie.autoComplete("ad") == "addition")
        self.assertTrue(trie.autoComplete("ae") == "aedt")
        self.assertTrue(trie.autoComplete("ai") == "ai")
        self.assertTrue(trie.autoComplete("al") == "algorithm")
        self.assertTrue(trie.autoComplete("an") == "and")
        self.assertTrue(trie.autoComplete("ap") == "appropriate")
        self.assertTrue(trie.autoComplete("ar") == "are")
        self.assertTrue(trie.autoComplete("as") == "as")
        self.assertTrue(trie.autoComplete("at") == "at")
        self.assertTrue(trie.autoComplete("au") == "automated")
        self.assertTrue(trie.autoComplete("av") == "available")
        self.assertTrue(trie.autoComplete("ba") == "baseline")
        self.assertTrue(trie.autoComplete("be") == "be")
        self.assertTrue(trie.autoComplete("bi") == "big")
        self.assertTrue(trie.autoComplete("bl") == "block")
        self.assertTrue(trie.autoComplete("bo") == "books")
        self.assertTrue(trie.autoComplete("br") == "bracket")
        self.assertTrue(trie.autoComplete("bu") == "but")
        self.assertTrue(trie.autoComplete("by") == "by")
        self.assertTrue(trie.autoComplete("ca") == "cases")
        self.assertTrue(trie.autoComplete("ch") == "check")
        self.assertTrue(trie.autoComplete("ci") == "cite")
        self.assertTrue(trie.autoComplete("cl") == "clayton")
        self.assertTrue(trie.autoComplete("co") == "code")
        self.assertTrue(trie.autoComplete("cr") == "criteria")
        self.assertTrue(trie.autoComplete("da") == "days")
        self.assertTrue(trie.autoComplete("de") == "description")
        self.assertTrue(trie.autoComplete("di") == "different")
        self.assertTrue(trie.autoComplete("do") == "documentation")
        self.assertTrue(trie.autoComplete("du") == "during")
        self.assertTrue(trie.autoComplete("ea") == "each")
        self.assertTrue(trie.autoComplete("ed") == "edge")
        self.assertTrue(trie.autoComplete("eg") == "eg")
        self.assertTrue(trie.autoComplete("em") == "employability")
        self.assertTrue(trie.autoComplete("en") == "end")
        self.assertTrue(trie.autoComplete("et") == "etc")
        self.assertTrue(trie.autoComplete("ev") == "everything")
        self.assertTrue(trie.autoComplete("ex") == "examples")
        self.assertTrue(trie.autoComplete("fa") == "failed")
        self.assertTrue(trie.autoComplete("fe") == "feel")
        self.assertTrue(trie.autoComplete("fi") == "file")
        self.assertTrue(trie.autoComplete("fo") == "for")
        self.assertTrue(trie.autoComplete("fr") == "from")
        self.assertTrue(trie.autoComplete("fu") == "function")
        self.assertTrue(trie.autoComplete("ge") == "getting")
        self.assertTrue(trie.autoComplete("go") == "good")
        self.assertTrue(trie.autoComplete("gu") == "guide")
        self.assertTrue(trie.autoComplete("ha") == "have")
        self.assertTrue(trie.autoComplete("he") == "helping")
        self.assertTrue(trie.autoComplete("hi") == "highlevel")
        self.assertTrue(trie.autoComplete("ho") == "how")
        self.assertTrue(trie.autoComplete("ht") == "https")
        self.assertTrue(trie.autoComplete("hy") == "hyphen")
        self.assertTrue(trie.autoComplete("id") == "idea")
        self.assertTrue(trie.autoComplete("if") == "if")
        self.assertTrue(trie.autoComplete("im") == "implement")
        self.assertTrue(trie.autoComplete("in") == "in")
        self.assertTrue(trie.autoComplete("is") == "is")
        self.assertTrue(trie.autoComplete("it") == "it")


if __name__ == "__main__":
    unittest.main()