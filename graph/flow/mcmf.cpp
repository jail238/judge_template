#include <bits/stdc++.h>
#define fastio cin.tie(0), cout.tie(0), ios_base::sync_with_stdio(false)
typedef long long ll;
// #define int ll
const int INF = 2e9;
const int MAX_SIZE = 111;
using namespace std;

class MCMF{
public:
    int n;
    vector<vector<tuple<int, int, int, int>>> adj;
    array<int, MAX_SIZE> dist;
    array<bool, MAX_SIZE> inq;
    array<bool, MAX_SIZE> visited;
    array<int, MAX_SIZE> used;

    MCMF(int size): n(size){
        adj.resize(n+1);
    }

    void add_edge(int u, int v, int capacity, int cost){
        adj[u].push_back({v, capacity, cost, (int)adj[v].size()});
        adj[v].push_back({u, 0, -cost, (int)adj[u].size()-1});
    }

    bool spfa(int src, int sink){
        dist.fill(INF); inq.fill(false);
        dist[src] = 0; inq[src] = true;
        queue<int> q; q.push(src);

        while (!q.empty()){
            int now = q.front(); q.pop();
            inq[now] = false;
            for (auto [nxt, cap, cost, dual]: adj[now]){
                if (cap && dist[nxt] > dist[now]+cost){
                    dist[nxt] = dist[now]+cost;
                    if (!inq[nxt]){
                        q.push(nxt);
                        inq[nxt] = true;
                    }
                }
            }
        }
        return dist[sink] < INF;
    }

    int dfs(int src, int sink, int now, int nowflow){
        visited[now] = true;
        if (now == sink) return nowflow;
        for(; used[now]<adj[now].size(); used[now]++){
            auto &[nxt, cap, cost, dual] = adj[now][used[now]];
            if (!visited[nxt] && dist[nxt]==dist[now]+cost && cap){
                int tmp = dfs(src, sink, nxt, min(nowflow, cap));
                if (tmp){
                    cap -= tmp;
                    get<1>(adj[nxt][dual]) += tmp;
                    return tmp;
                }
            }
        }
        return 0;
    }

    pair<int, int> solve(int src, int sink, int maxf=INF){
        int maxflow = 0, mincost = 0;
        while((maxflow < maxf) && spfa(src, sink)){
            used.fill(0);
            int nowflow = 0;
            visited.fill(false);
            while ((nowflow = dfs(src, sink, src, INF))){
                maxflow += nowflow;
                mincost += dist[sink]*nowflow;
                visited.fill(false);
            }
        }
        return {maxflow, mincost};
    }
};

signed main(){
    fastio;
    MCMF mcmf(MAX_SIZE);
}
