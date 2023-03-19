class TrieNode{
    public:
    TrieNode* children[26];
    bool isEnd;

    TrieNode(){
        for(int i=0;i<26;i++) children[i]=NULL;
        isEnd=false;
    }
};

class WordDictionary {
public:
    TrieNode* root;

    WordDictionary() {
        root = new TrieNode();
    }
    
    void addWord(string word) {
        TrieNode* temp=root;
        for(int i=0;i<word.size();i++){
            int ind=word[i]-'a';
            if(temp->children[ind]==NULL){
                temp->children[ind]=new TrieNode();
            }
            temp=temp->children[ind];
        }
        temp->isEnd=true;
    }

    bool searchHelper(string word, int i, TrieNode* curr){
        if(i==word.size()){
            return curr->isEnd;
        }

        if(word[i]!='.'){
            int ind=word[i]-'a';
            if(curr->children[ind]==NULL) return false;
            return searchHelper(word,i+1,curr->children[ind]);
        }
        else{
            bool ans=false;
            for(int ind=0;ind<26;ind++){
                if(curr->children[ind])
                ans = ans or searchHelper(word,i+1,curr->children[ind]);
            }
            return ans;
        }

    }
    
    bool search(string word) {
        TrieNode* temp=root;
        return searchHelper(word,0,temp);
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */