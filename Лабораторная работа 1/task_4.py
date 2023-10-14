users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
dict_ = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
unique_users = {'user1', 'user2', 'user3', 'user1', 'user4', 'user2'}   # Уникальные посещения
dict_["Общее количество"] = len(users)
dict_["Уникальные посещения"] = len(unique_users)

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
print(dict_)
