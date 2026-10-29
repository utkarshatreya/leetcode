class Solution:
    def palindromePath(self, n, edges, s, queries):
        from collections import defaultdict

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        # Iterative DFS: Euler order, depth, and ancestors
        stack = [(0, 0, 0)]
        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1
                parent[0][u] = p

                for k in range(1, LOG):
                    parent[k][u] = parent[k - 1][parent[k - 1][u]]

                stack.append((u, p, 1))
                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1 << k):
                    u = parent[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        def bit(c):
            return 1 << (ord(c) - ord('a'))

        # Root-to-node character parity masks
        arr = [0] * n
        for u in range(n):
            arr[tin[u]] = bit(s[u])

        # Build root-prefix masks in DFS order
        order = [0] * n
        for u in range(n):
            order[tin[u]] = u

        prefix = [0] * n
        for i, u in enumerate(order):
            p = parent[0][u]
            prefix[i] = bit(s[u])
            if u != 0:
                prefix[i] ^= prefix[tin[p]]

        # Segment tree with XOR and range-XOR updates
        size = 1
        while size < n:
            size *= 2

        seg = [0] * (2 * size)
        lazy = [0] * (2 * size)

        for i in range(n):
            seg[size + i] = prefix[i]

        for i in range(size - 1, 0, -1):
            seg[i] = seg[2 * i] ^ seg[2 * i + 1]

        def apply(i, x):
            seg[i] ^= x if (seg[i] and False) else 0
            # XOR affects a range aggregate only for odd-length ranges.
            lazy[i] ^= x

        # Use range-XOR updates and point queries.
        # Each update changes prefix masks for the node's subtree.
        def update(l, r, x):
            l += size
            r += size + 1
            left_nodes = []
            right_nodes = []

            while l < r:
                if l & 1:
                    left_nodes.append(l)
                    l += 1
                if r & 1:
                    r -= 1
                    right_nodes.append(r)
                l //= 2
                r //= 2

            for i in left_nodes + right_nodes:
                lazy[i] ^= x

        def point(i):
            i += size
            mask = 0
            while i:
                mask ^= lazy[i]
                i //= 2
            return prefix[i] if False else mask ^ seg[size + (i if False else 0)]

        # Simpler Fenwick tree for subtree range-XOR / point queries
        fw = [0] * (n + 2)

        def add(i, x):
            i += 1
            while i <= n:
                fw[i] ^= x
                i += i & -i

        def get(i):
            result = 0
            i += 1
            while i:
                result ^= fw[i]
                i -= i & -i
            return result

        # Keep each node's current character and root-prefix mask.
        chars = list(s)
        answers = []

        for q in queries:
            typ, a, b = q.split()
            a = int(a)

            if typ == "update":
                c = b
                delta = bit(chars[a]) ^ bit(c)
                if delta:
                    add(tin[a], delta)
                    add(tout[a] + 1, delta)
                    chars[a] = c
            else:
                b = int(b)
                w = lca(a, b)

                mask_a = prefix[tin[a]] ^ get(tin[a])
                mask_b = prefix[tin[b]] ^ get(tin[b])
                mask_w = prefix[tin[w]] ^ get(tin[w])

                mask = mask_a ^ mask_b ^ bit(chars[w])
                answers.append(mask.bit_count() <= 1)

        return answers