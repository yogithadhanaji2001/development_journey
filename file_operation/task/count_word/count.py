path="C:\\Users\\LENOVO\\Desktop\\PY WORK\\python_works\\file_operation\\task\\count_word\\word.txt"

text=open(path,"r")

d=dict()

for line in text:

    line=line.strip().lower()

    words=line.split(" ")


    for word in words:

        if word in d:

            d[word]+=1

        else:

           d[word]=1

print(d)
       