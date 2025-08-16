nums = [1, 2, 3, 4, 5]

squared = map(lambda x: x**2, nums)
print("Squared)", list(squared))

words = ["apple", "banana", "cherry"]

uppercased = map(str.upper, words)
print("Uppercased)", list(uppercased))
