money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
dohod = money_capital + salary  # Доход в первом месяце
rashod = spend  # Расход в первом месяце
month = 1  # Первый месяц
while dohod > rashod:
    ostatok = dohod - rashod  # Остаток денег после расходов
    dohod = ostatok + salary  # Доход в последующие месяцы
    rashod = rashod * (1 + increase)  # Расход в последующие месяцы
    if dohod < rashod:
        break
    else:
        month = month + 1  # Счетчик месяцев
print("Количество месяцев, которое можно протянуть без долгов:", month)
