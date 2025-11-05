import sys
input = sys.stdin.readline

class Trie:
    __slots__ = ("children", "is_end")

    def __init__(self):
        self.children = {}
        self.is_end = 0
    
    def insert(self, word):
        node = self
        for c in word:
            if not c in node.children: node.children[c] = Trie()
            node = node.children[c]
        node.is_end = 1
    
    def delete(self, word):
        node = self
        stack = []

        for c in word:
            if not c in node.children: return
            stack.append((node, c))
            node = node.children[c]
        
        if not node.is_end: return
        node.is_end = 0

        while stack:
            if node.children or node.is_end: break
            parent, c = stack.pop()
            del parent.children[c]
            node = parent

    def directory(self, depth=0):
        for name in sorted(self.children):
            tmps = ["",">"][depth>0]
            print("-"*depth+tmps+name)
            self.children[name].directory(depth+1)

    def search(self, word):
        node = self
        for c in word:
            if not c in node.children: return 0
            node = node.children[c]
        return node.is_end
    
    def startwith(self, prefix):
        return self.node_of(prefix) != -1

    def node_of(self, s):
        node = self
        for c in s:
            if not c in node.children: return -1
            node = node.children[c]
        return node
    
    def max_xor(self, bit):
        node = self
        mxor = 0
        for i in range(30):
            if bit[i] == '0': opbit = '1'
            else: opbit = '0'
            cbit = 1<<(29-i)
            if opbit in node.children:
                mxor |= cbit
                node = node.children[opbit]
            else: node = node.children[bit[i]]
        return mxor
