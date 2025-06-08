#include<iostream>
#include<deque>
#include<unordered_map>
#include<unordered_set>
#include<bits/c++io.h>
using namespace std;


void dfs(int node, int (&graph)[], unordered_set<int> &visited) {
    cout << node << endl;
    visited.insert(node);
    int nextNode = graph[node];
    if (visited.find(nextNode) == visited.end()) {
        dfs(nextNode, graph, visited);
    }
}

void solve() {
    
}


int main() {
    solve();
}