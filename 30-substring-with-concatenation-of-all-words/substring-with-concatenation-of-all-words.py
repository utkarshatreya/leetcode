
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        word_freq = Counter(words)
        result = []

        for i in range(word_len):
            left = i
            seen = Counter()
            count = 0

            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word not in word_freq:
                    seen.clear()
                    count = 0
                    left = right + word_len
                    continue

                seen[word] += 1
                count += 1

                while seen[word] > word_freq[word]:
                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    count -= 1
                    left += word_len

                if count == word_count:
                    result.append(left)

        return result