def month_to_season(num_month):

    if num_month in [12, 1, 2]:
        return "Зима"
    elif num_month in [3, 4, 5]:
        return "Весна"
    elif num_month in [6, 7, 8]:
        return "Лето"
    elif num_month in [9, 10, 11]:
        return "Осень"
    else:
        return "Неверный номер месяца"
num_month=13
print(month_to_season(num_month))

