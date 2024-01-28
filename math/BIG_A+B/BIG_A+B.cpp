#include <bits/stdc++.h>
#define fastio cin.tie(0), cout.tie(0), ios_base::sync_with_stdio(false)
#define MAX 10010
typedef long long ll;
using namespace std;

string a, b;
ll len_a, len_b, c[MAX];

int main(){
    fastio;
    cin >> a >> b;
    if (a == "0" && b == "0") {cout << 0; return 0;}
    len_a = a.size(); len_b = b.size();
    if (len_b > len_a){ swap(a, b); swap(len_a, len_b); }

    for (ll i=1; i <= len_a; i++){
        if (len_b-i < 0) { c[MAX-i] += stoi(string(1, a[len_a-i]));}
        else {c[MAX-i] += stoi(string(1, a[len_a-i]))+stoi(string(1, b[len_b-i])); }
        if (c[MAX-i] >= 10){ c[MAX-i-1] += 1;c[MAX-i] -= 10; }
    }
    if (c[MAX-len_a-1] != 0) cout << c[MAX-len_a-1];
    for (ll i=MAX-len_a; i < MAX; i++) cout << c[i];
}
