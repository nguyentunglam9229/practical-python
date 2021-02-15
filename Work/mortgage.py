# mortgage.py
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 12*5
extra_payment_end_month = extra_payment_start_month + 12*4
extra_payment = 1000
while principal > 0:
    month += 1
    principal = principal * (1+rate/12) - payment
    if extra_payment_end_month >= month > extra_payment_start_month:
        principal -= extra_payment
        total_paid += extra_payment
    total_paid = total_paid + payment
    print(f'{month} {round(total_paid, 2)} {round(principal, 2)}')

print('Total paid', round(total_paid, 2))
print('month', round(month,2))
# Exercise 1.7
