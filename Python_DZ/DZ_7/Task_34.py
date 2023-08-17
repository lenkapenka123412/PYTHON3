def check_rhythm(poem):
    phrases = poem.split()  # Разделение стихотворения на фразы
    syllables = []  # Список для хранения числа слогов в каждой фразе

    for phrase in phrases:
        words = phrase.split('-')  # Разделение фразы на слова
        syllables_count = sum([len([c for c in word if c.lower() in 'aeiou']) for word in words])
        syllables.append(syllables_count)  # Добавление числа слогов в список

    if len(set(syllables)) == 1:  # Проверка, все ли числа слогов одинаковые
        return "Парам пам-пам"
    else:
        return "Пам парам"

poem_input = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem_input)
print(result)

