arr=["word","madam","racecar","car"]

words=[w for w in arr if w==w[::-1]]

print(words)