clothes = [
    {"code": "C001", "title": "Casual T-Shirt", "brand": "Adidas", "sizes": ["S", "M", "L", "XL"]},
    {"code": "C002", "title": "Formal Shirt", "brand": "Van Heusen", "sizes": ["38", "40", "42", "44"]},
    {"code": "C003", "title": "Slim Fit Jeans", "brand": "Levi's", "sizes": ["30", "32", "34", "36"]},
    {"code": "C004", "title": "Denim Jacket", "brand": "Wrangler", "sizes": ["M", "L", "XL"]},
    {"code": "C005", "title": "Hoodie", "brand": "H&M", "sizes": ["S", "M", "L", "XL"]},
    {"code": "C006", "title": "Chinos", "brand": "Peter England", "sizes": ["30", "32", "34", "36"]},
    {"code": "C007", "title": "Kurta", "brand": "FabIndia", "sizes": ["38", "40", "42", "44"]},
    {"code": "C008", "title": "Track Pants", "brand": "Nike", "sizes": ["S", "M", "L", "XL"]},
    {"code": "C009", "title": "Polo T-Shirt", "brand": "US Polo Assn.", "sizes": ["S", "M", "L", "XL"]},
    {"code": "C010", "title": "Sweatshirt", "brand": "Zara", "sizes": ["M", "L", "XL"]},
    {"code": "C011", "title": "Maxi Dress", "brand": "Only", "sizes": ["S", "M", "L"]},
    {"code": "C012", "title": "Crop Top", "brand": "Forever 21", "sizes": ["XS", "S", "M", "L"]},
    {"code": "C013", "title": "Leggings", "brand": "Reebok", "sizes": ["S", "M", "L", "XL"]},
    {"code": "C014", "title": "Blazer", "brand": "Allen Solly", "sizes": ["38", "40", "42", "44"]},
    {"code": "C015", "title": "Party Dress", "brand": "H&M", "sizes": ["S", "M", "L"]},
    {"code": "C016", "title": "Cargo Pants", "brand": "Woodland", "sizes": ["30", "32", "34", "36", "38"]},
    {"code": "C017", "title": "Jumpsuit", "brand": "Zara", "sizes": ["S", "M", "L"]},
    {"code": "C018", "title": "Kurti", "brand": "Biba", "sizes": ["S", "M", "L", "XL"]},
    {"code": "C019", "title": "Sports Shorts", "brand": "Puma", "sizes": ["S", "M", "L", "XL"]},
    {"code": "C020", "title": "Winter Jacket", "brand": "North Face", "sizes": ["M", "L", "XL", "XXL"]},
]



produt=[p.get("title") for p in clothes if p.get("brand").lower()=="puma"]

print(produt)


# display all products titles available in size s 

size=[p.get("title") for p in clothes if "S" in p.get("sizes")]

print(size)

# in the given data set which brand contain most number of products

all_brands=[p.get("brand") for p in clothes ]


count= {b:all_brands.count(b) for b in all_brands}

sorted_bc=sorted(count,key=count.get,reverse=True)

print(sorted_bc)