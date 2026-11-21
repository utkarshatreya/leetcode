
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:

        n = len(parent)

        # Step 1: Build original tree
        tree = [[] for _ in range(n)]

        for i in range(1, n):
            tree[parent[i]].append(i)

        new_parent = parent[:]

        # Store latest node for each character
        last_seen = [-1] * 26

        # Iterative DFS with backtracking
        stack = [(0, 0, -1)]

        while stack:
            node, state, old = stack.pop()

            idx = ord(s[node]) - ord('a')

            if state == 0:

                old = last_seen[idx]

                if node != 0 and old != -1:
                    new_parent[node] = old

                last_seen[idx] = node

                # Exit event restores previous value
                stack.append((node, 1, old))

                for child in reversed(tree[node]):
                    stack.append((child, 0, -1))

            else:
                last_seen[idx] = old

        # Step 2: Build modified tree
        new_tree = [[] for _ in range(n)]

        for i in range(1, n):
            new_tree[new_parent[i]].append(i)

        # Step 3: Calculate subtree sizes
        ans = [1] * n

        order = []
        stack = [0]

        while stack:
            node = stack.pop()
            order.append(node)

            for child in new_tree[node]:
                stack.append(child)

        # Process children before parents
        for node in reversed(order):

            if new_parent[node] != -1:
                ans[new_parent[node]] += ans[node]

        return ans
