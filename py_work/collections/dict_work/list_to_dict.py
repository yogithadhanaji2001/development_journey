number=[1,2,3,4,5,6]

square_dict={}
square=0


for i in number:

    # square_dict[i]=i**2

    square_dict.update({i:i**2})

print(square_dict)    



text="goodmorning"

w={}

for ch in text:

    if ch in w:

        w[ch]+=1

    else:

        w[ch]= 1

print(w)



for ch in set(text):

    w[ch]=text.count(ch)
    
print(w)

max_freq= 0

max_freq_dict = {}


for k,v in w.items():

    if v >max_freq:
        max_freq = v

        max_freq_dict.clear()
        max_freq_dict[k]=v
print(max_freq_dict)




