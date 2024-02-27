#include <bits/stdc++.h>
#define fastio cin.tie(0), cout.tie(0), ios_base::sync_with_stdio(false)
typedef long long ll;
#define MAX 10001
using namespace std;

ll p[MAX];
vector<tuple<ll, ll, ll>> arr;
ll v, e, a, b, c, ans, lines, cost;

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
    cin >> v >> e;
    init();
    while (e--){
        cin >> a >> b >> c;
        arr.push_back(make_tuple(c, a, b));
    }
    sort(arr.begin(), arr.end());
    for (auto ar: arr){
        cost = get<0>(ar); a = get<1>(ar); b = get<2>(ar);
        if (find(a) != find(b)){
            uni(a, b);
            ans += cost;
            lines++;
        }
        if (lines == v-1) break;
    }
    
    cout << ans << '\n';
}
