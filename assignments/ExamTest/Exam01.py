unit_used = 350
rate_per_unit = 4.5
service_charge = 50

electricity_cost = unit_used * rate_per_unit
print(f"electricity_cost = {unit_used} * {rate_per_unit} = {electricity_cost}")

total = electricity_cost + service_charge
print(f"total = {electricity_cost} + {service_charge} = {total}")
print(f"used {unit_used} unit equals {int(total)} THB")