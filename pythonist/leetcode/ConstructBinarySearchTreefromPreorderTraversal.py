
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def btsfromPreorder(preorder):
    root = TreeNode(preorder[0])
    stack = [root]

    for idx in range(1, len(preorder)):
        ch = TreeNode(preorder[idx])
        parent = stack[-1]
        while stack and stack[-1].val < ch.val:
            parent = stack.pop()
        if parent.val < ch.val:
            parent.right = ch
        else:
            parent.left = ch
        stack.append(ch)
    return root

def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', btsfromPreorder([8,5,1,7,10,12]))



if __name__ == "__main__":
    main()
