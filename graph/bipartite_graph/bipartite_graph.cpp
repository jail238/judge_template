#include <bits/stdc++.h>
#define fastio cin.tie(0), cout.tie(0), ios_base::sync_with_stdio(false)
#define MAX 20010
typedef long long ll;
using namespace std;

ll v, e, a, b;
vector<vector<ll>> graph(MAX);
char color[MAX];
bool isBigraph;

void init(){
    isBigraph = true;
    for (ll i=0; i<MAX; i++){
        color[i] = 'W';
        graph[i].clear();
    }
}

void dfs(ll now, char cor){
    color[now] = cor;
    for (auto nxt: graph[now]){
        if (color[nxt] == 'W'){
            if (cor == 'X') dfs(nxt, 'Y');
            else dfs(nxt, 'X');
        }
        else{
            if (color[now] == color[nxt]){
                isBigraph = false;
                return;
            }
        }
    }
    return;
}

int main() {
    init();
    cin >> v >> e;
    for (ll i=0; i<e; i++){
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    
    for (ll i=1; i<=v; i++){
        if (color[i] == 'W') dfs(i, 'X');
        else{
            for (auto nxt: graph[i]){
                if (color[i] == color[nxt]){
                    isBigraph = false;
                    break;
                }
            }
        }
        if (!isBigraph) break;
    }
    if (isBigraph) cout << "YES";
    else cout << "NO"; 
}
