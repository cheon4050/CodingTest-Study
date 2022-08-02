import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# class Tree:
#     def __init__(self, val = None):
#         if val != None:
#             self.val = val
#         else:
#             self.val = None
#         self.left = None
#         self.right = None
#
#     def insert(self, val):
#         if self.val:
#             if val < self.val:
#                 if self.left is None:
#                     self.left = Tree(val)
#                 else:
#                     self.left.insert(val)
#             else:
#                 if self.right is None:
#                     self.right = Tree(val)
#                 else:
#                     self.right.insert(val)
#         else:
#             self.val = val
#
#
#     def postOrder(self):
#         if self.left:
#             self.left.postOrder()
#         if self.right:
#             self.right.postOrder()
#         print(self.val)
# tree = Tree()
# for i in arr:
#     tree.insert(i)
# tree.postOrder()

arr = []

def solution(arr, left, right):
    if left > right:
        return

    mid = left+1
    for i in range(left+1, right+1):
        if arr[i] > arr[left]:
            mid = i
            break
    solution(arr, left + 1, mid-1)
    solution(arr, mid, right)
    print(arr[left])

while True:
    try:
        num = int(input())
        arr.append(num)
    except:
        break
solution(arr, 0, len(arr)-1)