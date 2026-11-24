# Lab 01 Exercise 2: Camping Logistics
import math

def calculate_tent_cost(participants, tent_capacity, tent_price):
    num_of_tent = math.ceil(participants/tent_capacity)
    total = tent_price*num_of_tent
    return total

print(calculate_tent_cost(12, 4, 100))
print(calculate_tent_cost(13, 4, 100))