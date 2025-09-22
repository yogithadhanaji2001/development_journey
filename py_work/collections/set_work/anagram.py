# anagram

word1="silent"
word2="listen"

if sorted(word1)==sorted(word2):
    print(True)

else:
    print(False)


def isanagram(w1,w2):

    return sorted(w1)==sorted(w2)

print(isanagram("late","hate"))



print(set(word1)==set(word2) and len(word1)==len(word2))


