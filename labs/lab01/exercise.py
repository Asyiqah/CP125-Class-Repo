#One Value Change

def calculate_bill(meal_price):
    tax = meal_price * 0.06  # 6% SST
    service_charge = 2.00
    total = meal_price + tax + service_charge
    return total

total1 = calculate_bill(8.50)  # Nasi Lemak
print(f"Customer 1 total: RM{total1:.2f}")

total2 = calculate_bill(3.50)  # Roti Canai
print(f"Customer 2 total: RM{total2:.2f}")

total3 = calculate_bill(7.00)  # Mee Goreng
print(f"Customer 3 total: RM{total3:.2f}")


#Two Value Change

def calculate_rectangle_area(length, width):
    area = length * width
    return area

print(f"Rectangle 1: {calculate_rectangle_area(5, 3)}")
print(f"Rectangle 2: {calculate_rectangle_area(10, 4)}")
print(f"Rectangle 3: {calculate_rectangle_area(7, 2)}")



def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi

result = calculate_bmi(70, 1.75)
print(f"BMI: {result:.2f}")



def calculate_total(price, quantity, discount):
    subtotal = price * quantity
    total = subtotal - discount
    return total




def add_with_print(a, b):
    result = a + b
    print(result)  # shows the number

def add_with_return(a, b):
    result = a + b
    return result  # gives the number back

x = add_with_print(5, 3)
print(f"x contains: {x}")

y = add_with_return(5, 3)
print(f"y contains: {y}")