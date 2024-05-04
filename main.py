# Требуется создать программу для работы с файлом данных пассажиров "Титаника" (файл data.csv)
# Вариант № 6. Вычислить среднюю стоимость билета (поле Fare) у спасенных и погибших.
import csv
# вводим переменную (первую строку с названием столбцов) first, чтобы она не учитывалась при обработке файла
first = False
# открываем наш файл data.csv
f = open('data.csv')
# считываем все строки из файла
data = csv.reader(f)
# вводим две переменные (2 списка - сколько заплатили спасенные и погибшие соответственно)
fare_not_survived = []
fare_survived = []
# проходимcя по всей информации (строки), полученной из файла, кроме первой строки и
# пополняем списки с оплаченными билетами для спасенных и погибших соответственно
for raw in data:
    if first:
        if int(raw[1]) == 0:
            fare_not_survived.append(float(raw[9]))
        if int(raw[1]) == 1:
            fare_survived.append(float(raw[9]))
    first = True
# вычисляем сумму оплаченных билетов для спасенных, затем вычисляем среднее значение
sum_survived = 0.0
for fare in fare_survived:
    sum_survived += fare
print(f"Средняя стоимость билета у спасённых {sum_survived/len(fare_survived)}")
# вычисляем сумму оплаченных билетов для погибших, затем вычисляем среднее значение
sum_not_survived = 0.0
for fare in fare_not_survived:
    sum_not_survived += fare
print(f"Средняя стоимость билета у погибших {sum_not_survived / len(fare_not_survived)}")
f.close()
