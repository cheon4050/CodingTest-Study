import collections
import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
            if node.word:
                return True
        node.word = True
        return False

T = int(input())
for _ in range(T):
    n = int(input())
    trie = Trie()
    phoneNumberList = []
    for i in range(n):
        phoneNumberList.append(input().rstrip())
    phoneNumberList.sort()
    for phoneNumber in phoneNumberList:
        if trie.insert(phoneNumber):
            print("NO")
            break
    else:
        print("YES")
