arr=[6,7,8,9,10]

dic={num:num**2 for num in arr}

print(dic)

fruits=["apple","banana","carrot","drumstick","egg","fish"]


word_dict={w:len(w) for w in fruits}

print(word_dict)

orders=["tea","dosa","tea","ghee-roast","coffee","tea","idily","dosa"]


order_count={o:orders.count(o)for o in orders}

print(order_count)


# collection and methods.