def bank(X, Y):
    r = 0.1  # Годовая ставка
    A = X * (1 + r) ** Y
    return A
X = 500000  # Размер вклада
Y = 5     # Срок вклада в годах
final_amount = bank(X, Y)
print("На счёте будет через", Y, "лет будет:", final_amount)


