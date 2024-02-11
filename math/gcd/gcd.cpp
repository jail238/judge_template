#include <bits/stdc++.h>
#define fastio cin.tie(0), cout.tie(0), ios_base::sync_with_stdio(false)
#define MAX 20010
typedef long long ll;

using namespace std;
ll a, b;

ll gcd(ll a, ll b){
    ll temp;
    while (b != 0){
        temp = b;
        b = a%b;
        a = temp;
    }
    return a;
}

int main() {
    fastio;
    cin >> a >> b;
    cout << gcd(a, b);
}
