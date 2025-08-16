from collections import Counter

def char_frequency(filename):
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
    return Counter(text), text


def guess_file_type(text, freq):
    
    # Heuristic for C file
    if freq.get('{', 0) > 0 or freq.get('}', 0) > 0 or freq.get(';', 0) > 5 or "#include" in text:
        return "C Program File"

    # Heuristic for Python file
    if "def " in text or "class " in text or ":" in text:
        return "Python Program File"

    # Otherwise, assume plain text
    return "Text File"

filename = input("Enter filename: ")
freq, text = char_frequency(filename)

print("\n--- Character Frequencies ---")
for char, count in freq.items():
    print(repr(char), ":", count)

filetype = guess_file_type(text, freq)
print("\n--- File Type Guess ---")
print(filetype)
