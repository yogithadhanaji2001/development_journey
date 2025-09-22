path="C:\\Users\\LENOVO\\Desktop\\PY WORK\\python_works\\file_operation\\food_logs.csv\\food_logs.csv"


fr=open(path,"r")

food_logs=[]

for line in fr:

    data=line.rstrip("\n").lower().split(",")

    if len(data)>1:

        dictionary ={
            "date":data[0],
            "meal_type":data[1],
            "meal":data[2],
            "serving_size":data[3],
            "calories":data[4]
        }

        food_logs.append(dictionary)


# print(food_logs)


# daily summary


daily_summary=dict()

for e in food_logs:

    date=e.get("date")

    calories=int(e.get("calories"))

    if date in daily_summary:

        daily_summary[date]+=calories

    else:
        daily_summary[date]=calories


print(daily_summary)



max_calo=max(daily_summary,key=lambda e:e.get("calories")).get("calories")



max_calo_date=[e.get("date") for e in daily_summary if e.get("calories")==max_calo]
print(max_calo_date)