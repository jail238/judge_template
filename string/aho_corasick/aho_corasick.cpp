#include <bits/stdc++.h>
#define fastio cin.tie(0), cout.tie(0), ios_base::sync_with_stdio(false)
typedef long long ll;
using namespace std;

int n, m, idx;

struct Trie{
    Trie* w[26];
    Trie* fail;
    bool end;
    
    Trie(){
        for (int i = 0; i < 26; i++) w[i] = nullptr; // a-z all pointer
        fail = nullptr; end = false;
    }
    
    ~Trie(){
        for (int i = 0; i < 26; i++){ 
            if (w[i]) delete w[i];
        }
    }
    
    void add(const char* s){ // make word tree
        if (s[0] == '\0'){ //word's end
            end = true;
            return;
        }
        idx = s[0] - 'a';
        if (!w[idx]) w[idx] = new Trie();
        w[idx]->add(s+1);
    }
};

int main() {
    fastio;
    cin >> n;
    Trie* root = new Trie();
    while (n--){
        char s[110];
        cin >> s; root->add(s);
    }
    
    queue<Trie*> q;
    q.push(root);
    while (!q.empty()){
        Trie* now = q.front(); q.pop();
        for (int i = 0; i < 26; i++){
            Trie* nxt = now -> w[i];
            if (nxt){
                if (now == root) nxt -> fail = root;
                else {
                    Trie* dst = now -> fail;
                    while (dst != root && !dst->w[i]) dst = dst -> fail;
                    if (dst -> w[i]) dst = dst -> w[i];
                    nxt -> fail = dst;
                }
                nxt -> end |= nxt -> fail -> end; // substring check
                q.push(nxt);
            }
        }
    }
    cin >> m;
    while (m--){
        char s[10010];
        cin >> s;
        Trie* cur = root;
        bool pos = false;
        for (int i = 0; s[i] != '\0'; i++){
            idx = s[i] - 'a';
            while (cur != root && !cur->w[idx]) cur = cur -> fail;
            if (cur->w[idx]) cur = cur->w[idx];
            if (cur -> end){
                pos = true;
                break;
            }
        }
        if (pos) cout << "YES" << '\n';
        else cout << "NO" << '\n'; 
    }
}