# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)

# exer 1.8
principal = 500000.0
total_paid = 0.0
months = 0
extra = 1000
while principal > 0:
    if months < 12:
        monthly = payment + extra
    else:
        monthly = payment
    principal = principal * (1+rate/12) - monthly
    months += 1
    total_paid = total_paid + monthly

print('total paid', total_paid, 'in months:', months)

# exer 1.9
principal = 500000.0
total_paid = 0.0
months = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
while principal > 0:
    if (months >= extra_payment_start_month and 
        months <= extra_payment_end_month):
        monthly = payment + extra_payment
    else:
        monthly = payment
    # exer 1.11
    if principal < monthly:
        monthly = principal
        principal = 0
    else:
        principal = principal * (1+rate/12) - monthly
    months += 1
    total_paid = total_paid + monthly
    # exer 1.10
    #print(months, round(total_paid, 2), round(principal, 2))
    print(f'{months:4d} {total_paid:10.2f} {principal:10.2f}')

print('total paid', total_paid, 'in months:', months)
