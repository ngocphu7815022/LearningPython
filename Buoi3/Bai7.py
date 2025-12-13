numbers = [2, 5, 8, 11, 14, 17, 20]

# In ra ta cac so trong list
for number in numbers:
    print(number)

# In ra so chan trong list
print("Cac so chan la:")
for number in numbers:
    if number % 2 == 0:
        print(number)


# Tinh tong tat ca cac so trong list
sum = 0
for number in numbers:
    sum = sum + number
print(f"Tong cac so la {sum}")

# In ra bang cuu chuong cua tung so trong list
for number in numbers:
    print(f"Bang cuu chuong {number}")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
