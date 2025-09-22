# BMI calculation

# read height
# read weight

# bmi= weight_in_kg / height_in_meter**2

weight_in_kg = int(input("enter weight in kg : "))

height_in_cm =  int(input("enter height in cm : "))

height_in_meter = height_in_cm/100

BMI = weight_in_kg / height_in_meter**2

print(f"person with height {height_in_cm} and weight {weight_in_kg} BMI = {BMI}")
