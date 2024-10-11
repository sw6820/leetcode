/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int minDepth(TreeNode* root) {
        if (root==NULL) return 0;
        if (root->left==NULL && root->right==NULL)return 1;
        int lDepth = minDepth(root->left);
        int rDepth = minDepth(root->right);
        if (root->left==NULL) return rDepth+1;
        if (root->right==NULL) return lDepth+1;
        return min(lDepth,rDepth)+1;
    }
};