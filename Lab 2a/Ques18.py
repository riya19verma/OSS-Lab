from collections import defaultdict

def find_anagrams(words):
    anagram_groups = defaultdict(list)

    for word in words:
        # Sort the word to use as a key
        key = ''.join(sorted(word))
        anagram_groups[key].append(word)

    # Only return groups with more than 1 word (true anagrams)
    return [group for group in anagram_groups.values() if len(group) > 1]


# Example usage
words = ["eat", "ate", "tea", "tan", "nat", "bat", "tab", "hello"]
anagrams = find_anagrams(words)

print("Anagram groups found:")
for group in anagrams:
    print(group)
