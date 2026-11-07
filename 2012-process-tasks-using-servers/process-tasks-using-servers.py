import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        available = []
        busy = []

        # Store (weight, server_index)
        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))

        ans = []
        time = 0

        for i, task in enumerate(tasks):

            time = max(time, i)

            # Move all free servers into available heap
            while busy and busy[0][0] <= time:
                free_time, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            # If no server is available, wait
            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    free_time, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            # Select the best available server
            weight, index = heapq.heappop(available)

            ans.append(index)

            # Server becomes free after task processing
            heapq.heappush(
                busy,
                (time + task, weight, index)
            )

        return ans