#include <bits/stdc++.h>
#define fastio cin.tie(0), cout.tie(0), ios_base::sync_with_stdio(false)

using namespace std;

int div2(int x){
    int ret = x;
    while (~x & 1) x >>= 1;
    if (ret != x) ret >>= 1;
    return ret, x;
}


int phi(int x){
    int ans, x2 = div2(x);
    int p = 3;
    while (p*p <= x2){
        if (x%p == 0){
            ans -= ans/p;
            while (x2%p == 0){
                x /= p;
            }
        p += 2;
        }
    }

    if (x2 > 1) return ans-(ans/x2);
    return ans;
}
