
purchase_price = int(input("enter the price"))

GSt = 8

profit = int(input("enter profit"))

result = (profit/100)*purchase_price

selling_price=result+purchase_price

gst_amount=(GSt/100)*selling_price

total_cost = selling_price+gst_amount

print(total_cost)

