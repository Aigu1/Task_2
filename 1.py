print("Введите имя:")
name = input()
print("Введите фимилию:")
surname = input()
print("Введите год рождения:")
year = int(input())
print('Результат:')
print(name, "_", surname, "_", year)
name, surname = surname, name
year+=60
print(name, "_", surname, "_", year)