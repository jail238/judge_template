#include <bits/stdc++.h>
#define fastio cin.tie(0), cout.tie(0), ios_base::sync_with_stdio(false)
typedef long long ll;
#define MAX 100001
using namespace std;

ll n, m, a, x, y, cnt;
ll in_ett[MAX], out_ett[MAX], arr[MAX], tree[MAX];
vector<vector<ll>> graph(MAX); 

void ett(ll now){
    in_ett[now] = ++cnt;
    for (auto nxt: graph[now]) ett(nxt);
    out_ett[now] = cnt;
}
