# TODO Напишите функцию для поиска индекса товара

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
fruit = ['банан', 'груша', 'персик']


def food(spisok, tovar):
    a = []
    for find_item in tovar:
        if find_item in spisok:
            index_item = spisok.index(find_item)
            b = print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
            a.append(b)
        else:
            c = print(f"Товар '{find_item}' не найден в списке.")
            a.append(c)
    return a


food(items_list, fruit)
