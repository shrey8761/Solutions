class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        treeMap_Dict = {}

        def preorder(node):
            # if the child is Null, mark it as "-"
            if not node:
                return "null"
            
            # preorder (val, left, right)
            subTree = ",".join([str(node.val), preorder(node.left), preorder(node.right)])

            # after recursive, a "subtree" is found
            # if "subtree" is not seen, add to the dictionary
            if subTree not in treeMap_Dict:
                treeMap_Dict[subTree] = 0
            else:
                treeMap_Dict[subTree] += 1
                # if "subtree" saw 1 addtional time, append to dictionary
                if treeMap_Dict[subTree] == 1:                
                    res.append(node)

            return subTree
            
        preorder(root)

        return res
