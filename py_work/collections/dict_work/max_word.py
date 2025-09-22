text="this this is a python program to find most recursive word this python program is simple"

count=0

word=text.split(" ")

wc={}


for w in word :
    if w in wc:

        wc[w]+=1

    else:
        wc[w]=1    

print(wc)

# max_freq= 0

# max_freq_dict = {}

# for k,v in wc.items():

#     if v >max_freq:
#         max_freq = v

#         max_freq_dict.clear()
#         max_freq_dict[k]=v
# print(max_freq_dict)


print(sorted(wc,key=wc.get,reverse=True))
