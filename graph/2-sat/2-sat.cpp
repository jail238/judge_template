#include <bits/stdc++.h>
#define fastio cin.tie(0), cout.tie(0), ios_base::sync_with_stdio(false)
#define MAX 200010
typedef long long ll;
using namespace std;

vector<ll> stacks;
vector<vector<ll>> graph(MAX);
bool visited[MAX];
ll ids_arr[MAX], parents[MAX], scc_idx[MAX], ans[MAX];
ll ids = 1, scc_cnt = 0;
ll n, m, a, b;

ll change(ll x){
    if (x > 0) return 2*x-1;
    else return 2*abs(x);
}

void init(){
    for (ll i = 0; i < MAX; i++){
        graph[i].clear();
        visited[i] = false;
        ids_arr[i] = 0;
        parents[i] = 0;
        scc_idx[i] = -1;
    }
    ids = 1;
    scc_cnt = 0;
}

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
    init();
    cin >> n >> m;
    for(ll i=0; i<m; i++){
        cin >> a >> b;
        if (a != b) graph[change(-a)].emplace_back(change(b));
        graph[change(-b)].emplace_back(change(a));
    }
    for(ll i=1; i<=2*n; i++)
        if (ids_arr[i] == 0) scc(i);

    for (ll i=1; i <=2*n; i+=2){
        if (scc_idx[i] == scc_idx[i+1]){
            cout << 0;
            return 0;
        }
        if (scc_idx[i] < scc_idx[i+1]) { // retracing
            ans[i/2] = 1;
        }
    }
    
    cout << 1 << '\n';
    for (ll i=0; i<n; i++){
        cout << ans[i] << ' ';
    }
}
