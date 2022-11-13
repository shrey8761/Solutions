class Solution {
public:
string reverseWords(string s) {
        string ans="";
        int i,j,n=s.length();
        i=0;
        while(i<n){
            // Do not include leading spaces
            while(i<n && s[i]==' ')
                i++;
            j=i;
            //Till when we do not reach a space, means we are currently on a word
            while(j<n && s[j]!=' ')
                j++;
		   // Here j is pointing to the next index of the ending of the current word, Due to this when passing length as 2nd parameter in substr fn, We pass j-i not j-i+1
            ans=" "+s.substr(i,j-i)+ans;
            i=j+1;
        }

// Remove leading spaces
        i=0;
        while(i<n && ans[i]==' ')
            i++;
        ans=ans.substr(i);
        return ans;
    }

};