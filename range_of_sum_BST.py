"""
Given the root node of a binary search tree, return the sum of values 
of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 
Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23

 

Note:

    The number of nodes in the tree is at most 10000.
    The final answer is guaranteed to be less than 2^31

"""


#  Apply a DFS



##### Iterative approach
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        st = [root]    # stack
        sum = 0

        while st:
            cur = st.pop()
            if cur:
                if cur.val >= L and cur.val <= R:
                    sum += cur.val    
                if cur.val > L:
                    st.append(cur.left)
                if cur.val < R:
                    st.append(cur.right)
        return sum                


##### Recursive approach
    def rangeSumBST(self, root, L, R):
        
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans