#include <bits/stdc++.h>
#define fastio cin.tie(0), cout.tie(0), ios_base::sync_with_stdio(false)
typedef long long ll;
#define MAX 500001
using namespace std;

ll n, m, a, b, x, y, cnt;
ll arr[MAX], tree[MAX];

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

int main(){
    fastio;
    cin >> n >> m;
}
