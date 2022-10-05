class Solution(object):
    def addOneRow(self, root, v, d):
        return self.dfs(root, v, d, 1, 0)
    
    def dfs(self, node, v, d, height, direction):
        if node == None:
            if height == d:
                return TreeNode(v)
            else:
                return None
        if height == d:
            temp = TreeNode(v)
            if direction == 0:
                temp.left = node
            elif direction == 1:
                temp.right = node
            return temp
        node.left = self.dfs(node.left, v, d, height+1, 0)
        node.right = self.dfs(node.right, v, d, height+1, 1)
        return node