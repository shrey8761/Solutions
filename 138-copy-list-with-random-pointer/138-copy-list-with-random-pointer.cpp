class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, Node*> m;
        Node *curr=head, *newHead=NULL;

        // creating curresponding copies for all nodes in given list
        while(curr!=NULL) {      
            Node* newNode=new Node(curr->val);
            m[curr]=newNode;
            curr=curr->next;
        }

        // assigning next and random pointer of copy nodes according to given list
        for(auto e:m) {
            if(e.first == head) 
                newHead=e.second;
            if(e.first != NULL) {
                e.second->next = m[e.first->next],
                e.second->random = m[e.first->random];
            }
        }
        return newHead;
    }
};