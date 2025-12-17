word = input("Введите слово: ")
listt = list(word)
reversed_list = listt[::-1]

if listt == reversed_list:
    print("Это палиндром")
else:
    print("Не палиндром")

print(f"{listt} == {reversed_list}")
