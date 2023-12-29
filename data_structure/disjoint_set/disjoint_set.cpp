#include <bits/stdc++.h>
#define fastio cin.tie(0), cout.tie(0), ios_base::sync_with_stdio(false)
typedef long long ll;
#define MAX 1000001
using namespace std;

ll p[MAX];
ll n, m, a, b, check;

void init(){
    for (ll i = 0; i < MAX; i++){
        p[i] = i;
    }
}

ll find(ll x){
    if (p[x] != x){
        p[x] = find(p[x]);
    }
    return p[x];
}

void uni(ll a, ll b){
    a = find(a); b = find(b);
    p[max(a, b)] = min(a, b);
}

int main() {
    fastio;
    cin >> n >> m;
    init();
    while (m--){
        cin >> check >> a >> b;
        if (check == 1){
            if (find(a) != find(b)) cout << "NO" << '\n'; 
            else cout << "YES" << '\n';
        }
        else{
            uni(a, b);
        }
    }
}
