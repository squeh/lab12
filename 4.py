marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]

count5 = 0
count2 = 0

for mark in marks:
    if mark == 5:
        count5 += 1
    elif mark == 2:
        count2 += 1

print(f"Кол-во пятерок: {count5}")
print(f"Кол-во двоек: {count2}")
