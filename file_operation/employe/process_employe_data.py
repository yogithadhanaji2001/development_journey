path="C:\\Users\\LENOVO\\Desktop\\PY WORK\\python_works\\file_operation\\employe\\employe.csv"

read_file=open(path,"r")

all_employe=[]


for line in read_file:

    line=line.rstrip("\n").lower() 

    data=line.split(",")

    dictionary= {"id": data[0],"name":data[1],
           "depat":data[2],"salary":data[3], 
           "email":data[4], "location":data[5]
           }
    

    all_employe.append(dictionary)

# print(all_employe)

all_employe_name=[e.get("name")for e in all_employe if e.get("location")=="ekm"]

print(all_employe_name)

max_sal=max(all_employe,key=lambda e:e.get("salary")).get("salary")

print(max_sal)

max_sal_emplo=[e.get("name") for e in all_employe if e.get("salary")==max_sal]
print(max_sal_emplo)

min_sal=min(all_employe,key=lambda e:e.get("salary")).get("salary")

min_sal_emplo=[e.get("name") for e in all_employe if e.get("salary")==min_sal]

print(min_sal_emplo)