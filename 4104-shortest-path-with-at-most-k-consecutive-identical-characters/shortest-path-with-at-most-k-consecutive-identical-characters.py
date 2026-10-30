
import heapq

class Solution:
    def shortestPath(self, n, edges, labels, k):

        # Step 1: Create adjacency list
        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))

        # Store input as required by the problem
        mavorqeli = (n, edges, labels, k)

        # Step 2: Distance for each (node, count) state
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        # Start from node 0
        dist[0][1] = 0

        # Min heap: (weight, node, consecutive_count)
        pq = [(0, 0, 1)]

        # Step 3: Dijkstra
        while pq:

            wt, u, count = heapq.heappop(pq)

            # Ignore outdated states
            if wt > dist[u][count]:
                continue

            # Destination reached
            if u == n - 1:
                return wt

            # Explore neighbours
            for v, edge_wt in adj[u]:

                if labels[u] == labels[v]:
                    next_count = count + 1
                else:
                    next_count = 1

                # Invalid path
                if next_count > k:
                    continue

                new_wt = wt + edge_wt

                if new_wt < dist[v][next_count]:

                    dist[v][next_count] = new_wt

                    heapq.heappush(
                        pq,
                        (new_wt, v, next_count)
                    )

        return -1
