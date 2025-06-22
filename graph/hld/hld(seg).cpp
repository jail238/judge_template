#include <bits/stdc++.h>
#define fastio cin.tie(0), cout.tie(0), ios_base::sync_with_stdio(false)
typedef long long ll;
#define MAX 101010
using namespace std;

class SegTree{
public:
    int n;
    vector<int> tree;

    SegTree(int size=0){
        n = size;
        tree.resize(2*n+100, 0);
    }

    void seg_init(const vector<int>& arr){
        for (int i=0; i<n; i++) tree[i+n] = arr[i];
        for (int i=n-1; i>0; i--) tree[i] = max(tree[i<<1], tree[i<<1|1]);
    }

    void seg_update(int idx, int val){
        idx += n; tree[idx] = val;
        while (idx > 1){
            idx >>= 1;
            tree[idx] = max(tree[idx<<1], tree[idx<<1|1]);
        }
    }

    int seg_query(int l, int r){
        l += n; r += n;
        int res = 0;
        while (l <= r){
            if (l&1) res = max(res, tree[l++]);
            if (!(r&1)) res = max(res, tree[r--]);
            l >>= 1; r >>= 1;
        }
        return res;
    }
};

class HLD{
public:
    int n;
    vector<vector<pair<int, int>>> adj;
    array<int, MAX> parent, depth, sz, heavy, head, pos, to_child;
    SegTree seg;
    int now;

    HLD(int size) : n(size), now(0) {
        adj.resize(n + 1);
        seg = SegTree(n);
        sz.fill(1), parent.fill(0), depth.fill(0), heavy.fill(0), head.fill(0), pos.fill(0), to_child.fill(0);
    }

    void add_edge(int u, int v, int idx){
        adj[u].push_back({v, idx});
        adj[v].push_back({u, idx});
    }

    void dfs_ordering(int u, int p){
        sz[u] = 1;
        int max_size = 0;
        for (auto& edge: adj[u]){
            auto [v, idx] = edge;
            if (v == p) continue;
            parent[v] = u, depth[v] = depth[u]+1;
            dfs_ordering(v, u);
            sz[u] += sz[v];
            if (sz[v] > max_size){
                max_size = sz[v];
                heavy[u] = v;
            }
            to_child[idx] = v;
        }
    }
    
    void decomposition(int u, int h){
        head[u] = h, pos[u] = now++;
        if (heavy[u] > 0) decomposition(heavy[u], h);
        for (auto& edge: adj[u]){
            int v = edge.first;
            if (v != parent[u] && v != heavy[u]) decomposition(v, v);
        }
    }

    void hld_init(const vector<int>& edge_cost){
        dfs_ordering(1, 0); decomposition(1, 1);
        vector<int> arr(n);
        for (int i=1; i<n; i++){
            int child_node = to_child[i];
            arr[pos[child_node]] = edge_cost[i];
        }
        seg.seg_init(arr);
    }

    void update_edge(int edge_idx, int val){
        int child_node = to_child[edge_idx];
        seg.seg_update(pos[child_node], val);
    }

    int hld_query(int u, int v){
        int res = 0;
        while (head[u] != head[v]){
            if (depth[head[u]] < depth[head[v]]) swap(u, v);
            res = max(res, seg.seg_query(pos[head[u]], pos[u]));
            u = parent[head[u]];
        }
        if (depth[u] > depth[v]) swap(u, v);
        if (u != v) res = max(res, seg.seg_query(pos[u]+1, pos[v]));
        return res;
    }
};
