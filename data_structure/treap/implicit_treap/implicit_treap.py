from random import randint
import sys
input = sys.stdin.readline

class ImplicitTreap:
    class Node:
        __slots__ = ("val", "priority", "left", "right", "size", "sum", "rev")
        def __init__(self, val):
            self.val = val
            self.priority = randint(0, (1<<31)-1)
            self.left = None; self.right = None
            self.size = 1
            self.sum = val
            self.rev = 0
    
    def __init__(self):
        self.root = None

    def size(self, node):
        if node: return node.size
        else: return 0
    
    def subsum(self, node):
        if node: return node.sum
        else: return 0
    
    def upt(self, node):
        if not node: return
        node.size = 1+self.size(node.left)+self.size(node.right)
        node.sum = node.val+self.subsum(node.left)+self.subsum(node.right)
    
    def push(self, node):
        if node and node.rev:
            node.left, node.right = node.right, node.left
            if node.left: node.left.rev ^= 1
            if node.right: node.right.rev ^= 1
            node.rev = 0

    def merge(self, left, right):
        if not left or not right: return left or right
        self.push(left); self.push(right)
        if left.priority > right.priority:
            left.right = self.merge(left.right, right)
            self.upt(left)
            return left
        else:
            right.left = self.merge(left, right.left)
            self.upt(right)
            return right
    
    def split(self, node, k):
        if not node: return (None, None)
        self.push(node)
        if self.size(node.left) >= k:
            l, r = self.split(node.left, k)
            node.left = r
            self.upt(node)
            return (l, node)
        else:
            l, r = self.split(node.right, k-self.size(node.left)-1)
            node.right = l
            self.upt(node)
            return (node, r)
    
    def kth(self, node, k): #0-based index
        self.push(node)
        left_size = self.size(node.left)
        if k < left_size: return self.kth(node.left, k)
        elif k == left_size: return node
        else: return self.kth(node.right, k-left_size-1)
    
    def insert(self, idx, val): #1-based index
        idx -= 1
        new = self.Node(val)
        left, right = self.split(self.root, idx)
        self.root = self.merge(self.merge(left, new), right)
    
    def append(self, val):
        self.insert(self.size(self.root)+1, val)
    
    def erase(self, idx):
        idx -= 1
        left, mid = self.split(self.root, idx)
        mid, right = self.split(mid, 1)
        self.root = self.merge(left, right)
    
    def get(self, idx):
        return self.kth(self.root, idx-1).val
    
    def change(self, idx, val):
        idx -= 1
        left, mid = self.split(self.root, idx)
        mid, right = self.split(mid, 1)
        mid.val = val
        self.upt(mid)
        self.root = self.merge(left, self.merge(mid, right))
    
    def range_sum(self, l, r):
        left, mid = self.split(self.root, l-1)
        mid, right = self.split(mid, r-l+1)
        ans = self.subsum(mid)
        self.root = self.merge(left, self.merge(mid, right))
        return ans
    
    def reverse(self, l, r):
        left, mid = self.split(self.root, l-1)
        mid, right = self.split(mid, r-l+1)
        if mid: mid.rev ^= 1
        self.root = self.merge(left, self.merge(mid, right))
    
    def substring(self, l, r):
        left, mid = self.split(self.root, l-1)
        mid, right = self.split(mid, r-l+1)
        substr = []
        def dfs(node):
            if not node: return
            self.push(node)
            dfs(node.left)
            substr.append(node.val)
            dfs(node.right)
        dfs(mid)

        self.root = self.merge(left, self.merge(mid, right))
        return ''.join(substr)

for _ in range(int(input())):
    s = input().rstrip()
    treap = ImplicitTreap()
    for i in s: treap.append(i)
    while True:
        order = input().rstrip()
        if order == "END": break
        o1, o2, o3 = order.split()
        if o1 == 'I':
            r, x = o2, int(o3)+1
            for i in r:
                treap.insert(x, i)
                x += 1
        elif o1 == 'P': print(treap.substring(int(o2)+1, int(o3)+1))
