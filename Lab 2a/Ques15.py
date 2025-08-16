import string
from nltk.corpus import words

# Build a set of valid words for fast lookup
english_words = set(words.words())

def mutate(word):
    mutations = set()
    letters = string.ascii_lowercase

    # 1. Insertion
    for i in range(len(word) + 1):
        for c in letters:
            mutations.add(word[:i] + c + word[i:])

    # 2. Deletion
    for i in range(len(word)):
        mutations.add(word[:i] + word[i+1:])

    # 3. Replacement
    for i in range(len(word)):
        for c in letters:
            if word[i] != c:
                mutations.add(word[:i] + c + word[i+1:])

    # 4. Swapping consecutive characters
    for i in range(len(word) - 1):
        mutations.add(word[:i] + word[i+1] + word[i] + word[i+2:])

    # ✅ Keep only valid English words
    return sorted(mutations & english_words)

list1 = mutate("cat")
print("Mutated words:", list1)