def calculate_net_salary(salary,tax_rate):
    return salary*tax_rate

salary=75000.5
tax_rate=0.18
print(f"{calculate_net_salary(salary,tax_rate):.2f}")
