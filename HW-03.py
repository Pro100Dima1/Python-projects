per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму: "))

valu = list(per_cent.values())
deposit = []
for i in range(len(valu)):
    deposit.append(valu[i] * money)

print(deposit)

print("Максимальная сумма, которую вы можете заработать -", max(deposit))