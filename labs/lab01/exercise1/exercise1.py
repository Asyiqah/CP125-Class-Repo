# Lab 01 Exercise 1: Road Trip Budgeter
def is_budget_sufficient (one_way_km, budget):
    distance = one_way_km*2
    fuel = distance/10
    price = fuel*2
    return price<=budget

print(is_budget_sufficient(100,40))
print(is_budget_sufficient(100,39))
