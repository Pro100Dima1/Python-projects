count_ticket = int(input())

age = int(input())

if count_ticket < 3:
    if age < 18:
        free = 0
        print("Бесплатно")
    elif 18 < age < 25:
        price = 990 * count_ticket
        print(price)
    elif age > 25:
         full_price = 1390 * count_ticket
         print(full_price)
else:
    if age < 18:
        free = 0
        print("Бесплатно")
    elif 18 < age < 25:
        price = (990 * count_ticket) - (990 * count_ticket * 0.1)
        print("Цена билетов: ", price)
    elif age > 25:
         full_price = (1390 * count_ticket) - (1390 * count_ticket * 0.1)
         print("Цена билетов: ", full_price)