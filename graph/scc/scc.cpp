#include <bits/stdc++.h>
#define fastio cin.tie(0), cout.tie(0), ios_base::sync_with_stdio(false)
#define MAX 1000001
typedef long long ll;
using namespace std;

vector<ll> stacks;
vector<vector<ll>> graph(MAX);
vector<vector<ll>> ans(MAX);
bool visited[MAX];
ll ids_arr[MAX], parents[MAX], scc_idx[MAX], indegree[MAX];
ll ids = 1, scc_cnt = 0;
ll n, m, a, b;


void scc(ll node){
    ids_arr[node] = ids; parents[node] = ids;
    ids++; visited[node] = true;
    stacks.emplace_back(node);
    
    for (auto now: graph[node]){
        if (ids_arr[now] == 0){
            scc(now);
            parents[node] = min(parents[now], parents[node]);
        }
        else if (visited[now])
            parents[node] = min(parents[now], parents[node]);
    }
    
    ll w = -1;
    if (parents[node] == ids_arr[node]){
        while (w != node){
            w = stacks.back();
            stacks.pop_back();
            scc_idx[w] = scc_cnt;
            visited[w] = false;
        }
        scc_cnt++;
    }
}

int main() {
    fastio;
    cin >> n >> m;
    for(ll i=0; i<m; i++){
        cin >> a >> b;
        graph[a].emplace_back(b);
    }
    for(ll i=1; i<=n; i++)
        if (ids_arr[i] == 0) scc(i);
    
    for(ll i=1; i<=n; i++){
        ans[scc_idx[i]].push_back(i);
        for (auto j: graph[i]){
            if (scc_idx[i] != scc_idx[j]) indegree[scc_idx[j]]++;
        }
    }
}
