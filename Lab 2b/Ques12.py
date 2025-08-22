# sorted(<input>) returns a list of sorted elements from the input iterable
# ''.join(<input>) concatenates the elements of the input iterable into a single string
# <input> is the input iterable to be processed
# '' is the separator between elements (default is empty string)

def find_anagrams(words):
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)
    return list(anagrams.values())

words = ["eat", "tea", "ate", "bat", "tab", "tan", "nat"]
anagrams = find_anagrams(words)
for i in anagrams:
    print(i)