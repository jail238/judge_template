/* #pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops") */

#include <bits/stdc++.h>
#define fastio cin.tie(0), cout.tie(0), ios_base::sync_with_stdio(false)
typedef long long ll;
using namespace std;
ll N, M, K;

ll pw(ll base, ll exp, ll mod){
    ll res = 1;
    base %= mod;
    while (exp > 0){
        if (exp&1) res = (res*base)%mod;
        base = (base*base)%mod;
        exp >>= 1;
    }
    return res;
}

ll egcd(ll a, ll b, ll &x, ll &y){
    if (a == 0){
        x = 0, y = 1;
        return b;
    }
    ll x1, y1;
    ll g = egcd(b%a, a, x1, y1);
    x = y1 - (b/a)*x1;
    y = x1;
    return g;
}

ll modinv(ll a, ll m){
    ll x, y;
    ll g = egcd(a, m, x, y);
    if (g != 1) return -1;
    return (x%m+m)%m;
}

ll nCk_mod_m(ll N, ll K, ll M){
    if (M == 1) return 0;
    if (K < 0 || K > N) return 1%M;
    if (K == 0 || K == N) return 1%M;
    if (K > N/2) K = N-K;

    auto prime_fac = [](ll n) -> map<ll, int>{
        map<ll, int> div;
        ll i = 3, k = n;
        while (k%2 == 0){
            if (div.find(2) == div.end()) div[2] = 1;
            else div[2] += 1;
            k /= 2;
        }
        while (i*i <= k){
            while (k%i == 0){
                if (div.find(i) == div.end()) div[i] = 1;
                else div[i] += 1;
                k /= i;
            }
            i += 2;
        }
        if (k != 1) div[k] = 1;
        return div;
    };

    auto gcd = [&](ll a, ll b) -> ll {
        ll x, y;
        return egcd(a, b, x, y);
    };

    auto lcm = [&](ll a, ll b) -> ll {
        if (a == 0 || b == 0) return 0;
        return (a/gcd(a, b))*b;
    };

    auto crt = [&](const vector<ll>& a, const vector<ll>& p) -> ll {
        if (a.empty()) return 0;
        ll a0 = a[0], m0 = p[0];
        for (int i = 1; i < p.size(); i++){
            ll ai = a[i], mi = p[i];
            ll g = gcd(m0, mi);
            if ((a0-ai)%g != 0) return -1;
            ll k = (((ai-a0)/g)*modinv(m0/g, mi/g))%(mi/g);
            ll m_tmp = lcm(m0, mi);
            a0 = ((a0+k*m0)%m_tmp+m_tmp)%m_tmp;
            m0 = m_tmp;
        }
        return a0;
    };

    auto cntm = [](ll n, ll m) -> ll {
        ll tmp = 0;
        while (n > 0){
            tmp += n/m;
            n /= m;
        }
        return tmp;
    };

    ll pi, mod;
    vector<ll> fstarp;

    auto f_star_p = [&](ll n, ll mm) -> vector<ll> {
        vector<ll> fstarlist(n+1);
        fstarlist[0] = 1;
        ll res = 1;
        for (ll i = 1; i <= n; i++){
            if (i%mm != 0) res = (res*i)%mod;
            fstarlist[i] = res;
        }
        return fstarlist;
    };

    function<ll(ll)> f_p = [&](ll p_val) -> ll {
        if (p_val == 0) return 1;
        ll term1 = pw(fstarp[mod], p_val/mod, mod), term2 = f_p(p_val/pi)%mod, term3 = fstarp[p_val%mod];
        ll res = (term1*term2)%mod;
        res = (res*term3)%mod;
        return res;
    };

    map<ll, int> mdiv = prime_fac(M);
    vector<ll> a_i, p_i;
    for (auto const& [pii, eii]: mdiv) {
        ll cnt = cntm(N, pii)-cntm(K, pii)-cntm(N-K, pii);
        pi = pii, mod = 1;
        for (int i=0; i<eii; i++) mod *= pi;
        if (cnt >= eii){
            a_i.push_back(0);
            p_i.push_back(mod);
        }
        else{
            fstarp = f_star_p(mod, pi);
            ll x1n = f_p(N), x1k = f_p(K), x1nk = f_p(N-K);
            ll x = (x1n*modinv(x1k, mod)*modinv(x1nk, mod)*pw(pi, cnt, mod))%mod;
            a_i.push_back(x);
            p_i.push_back(mod);
        }
    }
    return crt(a_i, p_i);
}

int main(){
    fastio;
    cin >> N >> M >> K;
    cout << nCk_mod_m(N, M, K) << '\n';
}
