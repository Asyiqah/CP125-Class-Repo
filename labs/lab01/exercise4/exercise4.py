# Lab 01 Exercise 4: Dynamic Parking Rate
def get_hourly_rate(vehicle_type, hour):
    if vehicle_type == "Electric":
        price = 2.00
    elif vehicle_type == "Hybrid" and (hour >= 22 or hour <=6):
        price = 2.00
    elif vehicle_type == "Hybrid":
        price = 5.00
    else:
        return 5.00

print(get_hourly_rate("Hybrid", 23))
print(get_hourly_rate("Hybrid", 13))
print(get_hourly_rate("Sedan", 2))
