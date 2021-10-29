lead_amount_in_cm3 = 18
copper_amount_in_cm3 = 23
lead_density = 11.34
copper_density = 8.69
if lead_amount_in_cm3*lead_density > copper_amount_in_cm3*copper_density:
    print("Az ólom nehezbb.")
else:
    print("A réz nehezebb.")
