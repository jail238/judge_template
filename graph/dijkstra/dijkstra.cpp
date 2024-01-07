#include <bits/stdc++.h>
#define fastio cin.tie(0), cout.tie(0), ios_base::sync_with_stdio(false)
#define MAX 20001
#define INF 1234567890
typedef long long ll;
using namespace std;

ll v, e, a, b, c, k, d, now, cost;
vector<vector<pair<ll, ll>>> graph(MAX);
ll dist[MAX];
priority_queue<pair<ll, ll>> pq;

void dijkstra(ll start){
    pq.push({0, start});
    dist[start] = 0;
    while (!pq.empty()){
        d = -pq.top().first; now = pq.top().second;
        pq.pop();
        if (dist[now] < d) continue;
        for (auto nxt: graph[now]){
            cost = d+nxt.second;
            if (cost < dist[nxt.first]){
                dist[nxt.first] = cost;
                pq.push({-cost, nxt.first});
            }
        }
    }
}

int main(){
    fastio;
    cin >> v >> e >> k;
    fill(dist, dist+MAX, INF);
    for (ll i=0; i<e; i++){
        cin >> a >> b >> c;
        graph[a].push_back(make_pair(b, c));
    }
    dijkstra(k);
    for (ll i = 1; i <= v; i++){
        if (dist[i] != INF) cout << dist[i];
        else cout << "INF";
        cout << '\n';
    }
}
