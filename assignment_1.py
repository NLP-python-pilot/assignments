#Variables and type
first_number = 45
print(type(first_number))

second_number = 45.1
print(type(second_number))

float(first_number) 
print(type(first_number))

int(second_number)
print(type(second_number))

if first_number > second_number:
    print(f"True {first_number} es mayor que {second_number}")
else:
    print(f"False {first_number} es menor que {second_number}")

# Operators
i1 = 10
i2 = 6
i3 = 4
i4 = 5
ix = (i2 + i3) * i4 / i1
print(f"{ix} is the sum of i2 = {i2} with i3 = {i3}, product with i4 = {i4}\
 and division for i1 = {i1}, it's type is ", type(ix))

import random
import itertools 
x = random.randint(1, 50)
if x % 2 == 0: #Muestra si x es par, al checar que si divido pa 2, el resto de division es 0
    print(f"El número {x} es par.")
else:
    print(f"El número {x} es impar.")

numbers = random.sample(range(1,100), 10)
xi = 9
xn = (xi + 2) % len(numbers) 
# Rota desde la posicion inicial x1, los espacios correspondientes 
# a la derecha pero dentro de la lista inicial
print(numbers)
print(numbers[xn])


x = random.randint(1,10)
y = random.randint(1,5)

print(f"{x} to the power {y} is {x**y}")

start = 1
for _ in range(y):
    start *= x   # *= compound assignment operator used to multiply and
                # assign the result to the left variable. It is variable = variable * expression.
print(f"{x} to the power {y} is {start}")


# Advanced
min_doctors = 31.2 
min_patients = 24.5
hora_doctors = min_doctors / 60
hora_patients = min_patients/60
sec_doctors = hora_doctors * 60
sec_patients = hora_patients * 60
print(f"{hora_doctors} hours for doctors")
print(f"{hora_patients} hours for patients")
print(f"{sec_doctors} seconds for doctors")
print(f"{sec_patients} seconds for patients")

sec = int(input("How many seconds do you want to convert?\
 -write only numbers-"))
min = sec / 60
print(f"It'll be {min} minutes")
print(f"It'll be {min / 60} hours")