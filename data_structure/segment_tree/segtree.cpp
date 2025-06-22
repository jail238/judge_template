#include <bits/stdc++.h>
#define fastio cin.tie(0), cout.tie(0), ios_base::sync_with_stdio(false)
typedef long long ll;
#define MAX 202020
using namespace std;

ll n, m, qi, ai, bi, a[MAX];
bool tree[4*MAX];

void init(int node, int s, int e){
    if (s == e){
        tree[node] = a[s];
        return;
    }
    int m = (s+e)>>1;
    init(node<<1, s, m); init((node<<1)|1, m+1, e);
    tree[node] = tree[node<<1]+tree[(node<<1)|1];
}

void update(int node, int s, int e, int idx, int val){
    if (idx < s || idx > e) return;
    if (s==e){
        tree[node] = val;
        return;
    }
    int m = (s+e)>>1;
    update(node<<1, s, m, idx, val); update((node<<1)|1, m+1, e, idx, val);
    tree[node] = tree[node<<1]+tree[(node<<1)|1];
}

bool query(int node, int s, int e, int l, int r){
    if (l > r) return true;
    if (l > e || r < s) return true;
    if (l <= s && e <= r) return tree[node];
    int m = (s+e)>>1;
    return query(node<<1, s, m, l, r)+query((node<<1)|1, m+1, e, l, r);
}
