# TODO Напишите функцию find_common_participants


def find_common_participants(participants_first_users, participants_second_users, razdelitel=','):
    a = participants_first_users.split(razdelitel)
    b = participants_second_users.split(razdelitel)
    common_users = list(set(a).intersection(set(b)))
    return sorted(common_users)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


print("Общие участники:", find_common_participants(participants_first_group, participants_second_group))

# TODO Провеьте работу функции с разделителем отличным от запятой
