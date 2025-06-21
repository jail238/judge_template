#include <bits/stdc++.h>
#define fastio cin.tie(0), cout.tie(0), ios_base::sync_with_stdio(false)
typedef long long ll;
using namespace std;

template<typename Node, typename Lazy>
class LazySegTree{
private:
    int n;
    vector<Node> tree;
    vector<Lazy> lazy;
    Node node_idt;
    Lazy lazy_idt;
    ll MOD;

    function<Node(const Node&, const Node&)> merge;
    function<void(Node&, const Lazy&, int)> apply_lazy;
    function<void(Lazy&, const Lazy&)> merge_lazy;

    void up(int k) { tree[k] = merge(tree[k<<1], tree[(k<<1)|1]); }
    void down(int k, int l, int r){
        if (lazy[k] == lazy_idt) return; // lazy[k]가 항등원임
        int mid = l+((r-l)>>1);
        int left = mid-l+1, right = r-mid;
        
        apply_lazy(tree[k<<1], lazy[k], left);
        merge_lazy(lazy[k<<1], lazy[k]);
        apply_lazy(tree[(k<<1)|1], lazy[k], right);
        merge_lazy(lazy[(k<<1)|1], lazy[k]);

        lazy[k] = lazy_idt; // 자기 자신 초기화
    }

    void seg_build(const vector<Node>& v, int k, int l, int r){
        if (l==r) { tree[k] = v[l]; return; }
        int mid = l+((r-l)>>1);
        seg_build(v, k<<1, l, mid);
        seg_build(v, (k<<1)|1, mid+1, r);
        up(k);
    }

    void seg_update(int a, int b, const Lazy& lazy_val, int k, int l, int r){
        if (a>r || b<l) return;
        if (a<=l && r<=b){
            apply_lazy(tree[k], lazy_val, r-l+1);
            merge_lazy(lazy[k], lazy_val);
            return;
        }
        int mid = l+((r-l)>>1);
        down(k, l, r);
        seg_update(a, b, lazy_val, k<<1, l, mid);
        seg_update(a, b, lazy_val, (k<<1)|1, mid+1, r);
        up(k);
    }

    Node seg_query(int a, int b, int k, int l, int r){
        if (a>r || b<l) return node_idt;
        if (a<=l && r<=b) return tree[k];

        int mid = l+((r-l)>>1);
        down(k, l, r);
        Node left_res = seg_query(a, b, k<<1, l, mid);
        Node right_res = seg_query(a, b, (k<<1)|1, mid+1, r);

        return merge(left_res, right_res);
    }

    void set_operation(int merge_type, int update_type){
        bool is_using_mod = (this->MOD > 0);
        /* 1: 합(default), 2: 곱, 3: min, 4: max, 5: xor */
        switch (merge_type){
            case 1:
                node_idt = 0;
                merge = [this, is_using_mod](const Node& a, const Node& b) {
                    Node res = a+b;
                    if (is_using_mod) res = (res%this->MOD+this->MOD)%this->MOD;
                    return res;
                };
                break;
            
            case 2:
                node_idt = 1;
                merge = [this, is_using_mod](const Node& a, const Node& b) {
                    Node res = a*b;
                    if (is_using_mod) res = (res%this->MOD+this->MOD)%this->MOD;
                    return res;
                };
                break;

            case 3:
                node_idt = numeric_limits<Node>::max();
                merge = [](const Node& a, const Node& b) { return min(a, b); };
                break;
            
            case 4:
                node_idt = numeric_limits<Node>::min();
                merge = [](const Node& a, const Node& b) { return max(a, b); };
                break;
            
            case 5:
                node_idt = 0;
                merge = [](const Node& a, const Node& b) { return a^b; };
                break;
        }

        switch (update_type){
            /* 1: 구간 변화(default), 2: 구간 변경(xor 포함), 3: xor 구간 변화 */
            case 1:
                lazy_idt = 0;
                apply_lazy = [=](Node& node, const Lazy& lazy_val, int len){
                    if (merge_type == 3 || merge_type == 4) node += lazy_val;
                    else {
                        if (is_using_mod){
                            Node tmp = (lazy_val%this->MOD+this->MOD)%this->MOD;
                            tmp = (tmp*len)%this->MOD;
                            node = (node+tmp)%this->MOD;
                        }
                        else node += lazy_val*len;
                    }
                };
                merge_lazy = [=](Lazy& old_lazy, const Lazy& new_lazy) {
                    old_lazy += new_lazy;
                    if (is_using_mod) old_lazy = (old_lazy%this->MOD+this->MOD)%this->MOD;
                };
                break;

            case 2:
                lazy_idt = 0;
                apply_lazy = [=](Node& node, const Lazy& lazy_val, int len){
                    if (lazy_val != lazy_idt){
                        if (merge_type == 3 || merge_type == 4) node = lazy_val;
                        else if (merge_type == 5) node = (len&1) ? lazy_val : 0;
                        else {
                            if (is_using_mod){
                                Node tmp = (lazy_val%this->MOD + this->MOD)%this->MOD;
                                node = (tmp*len)%this->MOD;
                            }
                            else node = lazy_val*len;
                        }
                    }
                };
                merge_lazy = [=](Lazy& old_lazy, const Lazy& new_lazy){
                    if (new_lazy != lazy_idt) old_lazy = new_lazy;
                };
                break;
            
            case 3:
                lazy_idt = 0;
                apply_lazy = [](Node& node, const Lazy& lazy_val, int len){
                    if (len&1) node ^= lazy_val;
                };
                merge_lazy = [](Lazy& old_lazy, const Lazy& new_lazy) {
                    old_lazy ^= new_lazy;
                };
                break;
            case 4:
                lazy_idt = 0;
                apply_lazy = [](Node& node, const Lazy& lazy_val, int len){
                    if (lazy_val == 1) node = len-node;
                };
                merge_lazy = [](Lazy& old_lazy, const Lazy& new_lazy){
                    old_lazy ^= new_lazy;
                };
                break;
        }
    }

public:
    LazySegTree(int size, int merge_type, int update_type, ll mod = 0): n(size), MOD(mod) {
        tree.resize(4*n);
        lazy.resize(4*n);
        set_operation(merge_type, update_type);
    }

    LazySegTree(const vector<Node>& v, int merge_type, int update_type, ll mod = 0): LazySegTree(v.size(), merge_type, update_type, mod) {
        if (MOD > 0){
            vector<Node> tmp_v = v;
            for (int i=0; i<n; i++) tmp_v[i] = (tmp_v[i]%MOD+MOD)%MOD;
            seg_build(tmp_v, 1, 0, n-1);
        }
        else seg_build(v, 1, 0, n-1);
    }
    void update(int l, int r, const Lazy& lazy_val) { seg_update(l, r, lazy_val, 1, 0, n-1); }
    Node query(int l, int r) { return seg_query(l, r, 1, 0, n-1); }
};
