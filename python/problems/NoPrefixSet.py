
class PrefixNode:
    def __init__(self):
        self.chars = {}
        self.leaf = 0
    
class Trie:
    def __init__(self):
        self.root = PrefixNode()
    
    def add(self, s: str):
        node = self.root
        leafCount = 0
        for c in s:
            if c not in node.chars:
                node.chars[c] = PrefixNode()
            node = node.chars[c]
            leafCount += node.leaf

        node.leaf += 1
        return leafCount ==0 and node.leaf <= 1 and len(node.chars) == 0


def noPrefix(words):
    t = Trie()
    for w in words:
        if not t.add(w):
            print("BAD SET")
            print(w)
            return
    print("GOOD SET")

noPrefix(['abcd', 'bcd', 'abcde', 'bcde'])
noPrefix(['ab', 'bc', 'cd'])
noPrefix(['aab', 'defgab', 'abcde', 'aabcde', 'bbbbbbbbbb', 'jabjjjad'])
noPrefix(['aab', 'aac', 'aacghgh', 'aabghgh'])

noPrefix(['aab', 'aab'])
noPrefix(['dcjaichjejgheiaie', 'd'])



# t = Trie()
# t.add('abc')
# t.add('abcd')
# t.add('abcde')
# t.add('abcdef')
# t.add('def')
# print(t.check('abc'))
# print(t.check('abcd'))
# print(t.check('abcdef'))
# print(t.check('def'))