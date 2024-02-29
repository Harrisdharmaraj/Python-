class MagicDictionary:

    def _init_(self):
        self.words = []

    def buildDict(self, dictionary):
        self.words = dictionary

    def search(self, searchWord):
        for word in self.words:
            if len(word) != len(searchWord):
                continue
            diff = 0
            for w, sw in zip(word, searchWord):
                if w != sw:
                    diff += 1
                if diff > 1:
                    break
            if diff == 1:
                return True
        return False

# Example usage
magicDict = MagicDictionary()
magicDict.buildDict(["hello", "leetcode"])
print(magicDict.search("hello"))  # Output: False
print(magicDict.search("hhllo"))  # Output: True
print(magicDict.search("hell"))   # Output: False
print(magicDict.search("leetcoded"))  # Output: False
