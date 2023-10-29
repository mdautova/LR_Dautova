# TODO  Напишите функцию count_letters
def count_letters(text):
    words = []  # список текста без пробелов
    j_ = []  # список, состоящий из уникальных букв
    dict_word = {}  # создаем словарь
    text_lower = text.lower()  # приводим все буквы к нижнему регистру
    for i in text_lower:
        if i.isalpha() == True:  # если i - буква, а не пробел, то возвращает true
            words.append(i)  # записываем букву в список


    for j in words:
        if j not in j_:
            count_word = text_lower.count(j)
            j_.append(j)
            a = {j: count_word}
            dict_word.update(a)

    return dict_word


def calculate_frequency(dict):
    list_frequency = []
    dict_values = dict.items()

    summa = (sum(dict.values()))
    for key, value in dict_values:
        frequency = round(value / summa, 2)
        dict[key] = frequency

        list_frequency.append(frequency)

    return dict

# TODO Напишите функцию calculate_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте


dict_letters = count_letters(main_str)
new_dict = calculate_frequency(dict_letters)
for letter, frequency in new_dict.items():
    print(f"{letter}: {frequency:.2f}")

