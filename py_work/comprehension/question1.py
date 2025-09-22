arr=[2,3,4,8,9,10]


list=[num+1 if num>5 else num-1 for num in arr ]
print(list)

# mapping
# filtering
# reduce


fruits=["apple","banana","carrot","drumstick","egg","fish"]

vowels=[w for w in fruits if w[0].lower() in "aeiou"]

print(vowels)

# print longest word

longest_word=max(fruits,key=len)
short_word=min(fruits,key=len)

print(longest_word)
print(short_word)



