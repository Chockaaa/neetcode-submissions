# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        stack =[]

        def bfs(root, level=0):
            
            if root:
                if len(stack)>level:
                    stack[level].append(root.val)
                else:
                    stack.append([root.val])
            
                bfs(root.left,level+1)
                bfs(root.right,level+1)

        bfs(root,0)
        return stack



