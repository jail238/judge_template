// BOJ 2820
// ett with fenwick_tree

#include <bits/stdc++.h>
#define fastio cin.tie(0), cout.tie(0), ios_base::sync_with_stdio(false)
typedef long long ll;
#define MAX 500001
using namespace std;

ll n, m, a, b, x, y, cnt;
char p;
ll in_ett[MAX], out_ett[MAX], arr[MAX], tree[MAX];
vector<vector<ll>> graph(MAX); 

void ett(ll now){
    in_ett[now] = ++cnt;
    for (auto nxt: graph[now]) ett(nxt);
    out_ett[now] = cnt;
}

ll bit_sum(ll idx){
    ll val = 0;
    while (idx > 0){
        val += tree[idx];
        idx -= (idx & -idx);
    }
    return val;
}

void bit_update(ll idx, ll val){
    while (idx < cnt){
        tree[idx] += val;
        idx += (idx & -idx);
    }
}

int main() {
    fastio;
    cin >> n >> m >> arr[1];
    for (ll i = 2; i <= n; i++){
        cin >> a >> b;
        arr[i] = a;
        graph[b].push_back(i);
    }
    ett(1); cnt++;
    
    for (ll i = 1; i <= n; i++){
        bit_update(in_ett[i], arr[i]);
        bit_update(in_ett[i]+1, -arr[i]);
    }
    
    while (m--){
        cin >> p;
        if (p == 'p'){
            cin >> x >> y;
            bit_update(in_ett[x]+1, y);
            bit_update(out_ett[x]+1, -y);
        }
        else {
            cin >> x;
            cout << bit_sum(in_ett[x]) << '\n';
        }
    }
}
