# emi calculator program

# EMI=p*r*(1+r)**n/((1+r)**n-1)

# p= loan amount

# r= intrest rate => monthly intrest rate =intrest rate /100/12

# n=tenure*12

p=loan_amount=52000

intrest_rate=12

r=montly_intrest=intrest_rate/12/100

terure=1

n=monthly=terure*12

r_pluseone=(r+1)

EMI=p*r*(r_pluseone)**n/((r_pluseone)**n-1)

print(EMI)

total_emi=EMI*n

total_intrest_paid=total_emi-loan_amount

print(total_intrest_paid //10)

