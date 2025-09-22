prodect={"code":"sku1234",
         "title":"linen shirt",
         "brand":"peterngland",
         "price":1700,
         "offer":200
         }


# check offer key exist or not




if "offer" in prodect:
    prodect["offer"]+=500
else:
    prodect["offer"]=1000

print(prodect["offer"])    