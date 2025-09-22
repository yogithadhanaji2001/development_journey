text= "the quick brown fox jumps over the lazy dog".casefold()

alpha="abcdefghijklmnopqrstuvwxyz"

is_pangram=True


for ch in alpha:

    if ch not in text:

        is_pangram=False

        break


print(is_pangram)    



word1="abc"

word2="pqr"

# merge word1+word2

# Apbqcr




for ch in (word1,word2):

    print(ch)


    

    
    

