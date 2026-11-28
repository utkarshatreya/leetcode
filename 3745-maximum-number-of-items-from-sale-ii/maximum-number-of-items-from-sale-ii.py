
class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)

        # Step 1: Count frequency of each factor
        mx = max(factor for factor, price in items)
        freq = [0] * (mx + 1)

        for factor, price in items:
            freq[factor] += 1

        # Step 2: Count items having multiple factors
        cnt = [0] * (mx + 1)

        for i in range(1, mx + 1):
            for j in range(i, mx + 1, i):
                cnt[i] += freq[j]

            cnt[i] -= 1

        # Step 3: Sort items by price
        items.sort(key=lambda x: x[1])

        min_price = items[0][1]
        ans = 0

        # Step 4: Buy items that provide one free item
        for factor, price in items:

            if price > 2 * min_price:
                break

            free_count = cnt[factor]

            take = min(free_count, budget // price)

            ans += take * 2
            budget -= take * price

        # Step 5: Spend remaining budget on cheapest items
        ans += budget // min_price

        return ans
