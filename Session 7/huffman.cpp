class Solution {
  public:
    
    struct Node {
        int freq;
        Node* left;
        Node* right;
        
        Node(int f) {
            freq = f;
            left = right = NULL;
        }
    };
    
    struct Compare {
        bool operator()(Node* a, Node* b) {
            return a->freq > b->freq;
        }
    };
    
    void dfs(Node* root, string code, vector<string>& ans) {
        if (!root) return;
        
        if (!root->left && !root->right) {
            ans.push_back(code);
            return;
        }
        
        dfs(root->left, code + "0", ans);
        dfs(root->right, code + "1", ans);
    }
    
    vector<string> huffmanCodes(string S, vector<int> f, int N) {
        
        priority_queue<Node*, vector<Node*>, Compare> pq;
        
        for (int i = 0; i < N; i++) {
            pq.push(new Node(f[i]));
        }
        
        if (N == 1) {
            return {"0"};
        }
        
        while (pq.size() > 1) {
            Node* left = pq.top(); pq.pop();
            Node* right = pq.top(); pq.pop();
            
            Node* parent = new Node(left->freq + right->freq);
            parent->left = left;
            parent->right = right;
            
            pq.push(parent);
        }
        
        Node* root = pq.top();
        vector<string> ans;
        
        dfs(root, "", ans);
        
        return ans;
    }
};
