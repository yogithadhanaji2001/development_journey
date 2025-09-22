text="hello hai hello hai hai bye"
count=0

word=text.split(" ")

wc={}

for w in word:

    if w in wc:

        wc[w]+=1

    else:
        wc[w]=1    

print(wc)        



