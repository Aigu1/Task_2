#количество лет:
years = float(input("Введите количество лет:"))
#дней:
days = years * 365
#480 минут(8 часов):5=96 экспонатов в день, всего:
sum = 96 * days
print("За это время вы посмотрите:",sum, "экспанатов")

#количество экспонатов:
ex = int(input("Введите количество экспонатов:"))
#сколько минут нужно
min = 5 * ex
# целое число дней
days = min // 480
# оставшиеся минуты
ost_min = min % 480
# целое число лет
years = days // 365
# оставшиеся дни
ost_days = days % 365
print("Для просмотра этих экспонатов потребуется:",years, "лет,", ost_days,"дней и", ost_min,"минуты")