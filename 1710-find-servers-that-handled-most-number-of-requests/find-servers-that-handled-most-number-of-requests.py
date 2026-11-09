class Solution:
    def busiestServers(self, k, arrival, load):

        
        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)

        
        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

    
        def update(pos, value):
            pos += size
            tree[pos] = value

            while pos > 1:
                pos //= 2
                tree[pos] = tree[2 * pos] + tree[2 * pos + 1]

        
        def find(node, left, right, start):

            if right < start or tree[node] == 0:
                return -1

            if left == right:
                return left

            mid = (left + right) // 2

            ans = find(2 * node, left, mid, start)

            if ans != -1:
                return ans

            return find(2 * node + 1, mid + 1, right, start)

        busy = []
        count = [0] * k

        for i in range(len(arrival)):

            start = arrival[i]

            
            while busy and busy[0][0] <= start:
                end, server = heapq.heappop(busy)
                update(server, 1)

            
            preferred = i % k

            # Find available server
            server = find(1, 0, size - 1, preferred)

            
            if server == -1:
                server = find(1, 0, size - 1, 0)

            
            if server == -1:
                continue

            
            update(server, 0)

            count[server] += 1

            end_time = arrival[i] + load[i]

            heapq.heappush(busy, (end_time, server))

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]