# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return root
        currentLevel = []
        output = []
        currentLevel.append(root)
        while currentLevel:
            output.append(currentLevel[-1].val)
            nextLevel = []
            for element in currentLevel: 
                if element.left:
                    nextLevel.append(element.left)
                if element.right:
                    nextLevel.append(element.right)
            currentLevel = nextLevel
        return output