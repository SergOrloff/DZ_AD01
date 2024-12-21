# 1) Напиши пошаговый алгоритм действий в комментариях для определения,
# является ли строка палиндромом.
# 2) Напишите по созданному вами алгоритму функцию для проверки,
# является ли строка палиндромом.

import unicodedata


def is_palindrome(s):
    # 1. Преобразуем строку в нижний регистр, чтобы не учитывать регистр символов.
    s = s.lower()

    # 2. Нормализуем строку для поддержки символов Unicode.
    s = unicodedata.normalize('NFKD', s)

    # 3. Удаляем из строки все пробелы и специальные символы, оставляя только буквы и цифры.
    s = ''.join(char for char in s if char.isalnum())

    # 4. Проверяем, является ли строка пустой после удаления символов.
    if not s:
        return False

    # 5. Сравниваем строку с её перевёрнутым вариантом, используя цикл для поэтапной проверки.
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False

    # 6. Если все символы совпадают, возвращаем True (это палиндром).
    return True


# Пример использования
test_strings = [
    "A man, a plan, a canal, Panama",
    "Аргентина манит негра",
    "Hello",
    "Лёша на полке клопа нашёл",
    "Racecar",
    "Топот",
    "",
    "Казак",
    "Level",
    "А роза упала на лапу Азора",
    "Rotor",
    "Я иду с мечем судия",
    "Civic",
    "Шалаш",
    "Kayak",
    "Дед",
    "Madam",
    "Panapanap"
    "none"
]

# Выводим результаты для тестовых строк
for string in test_strings:
    result = is_palindrome(string)
    if result == True:
        print(f"Строка '{string}' \033[1mявляется палиндромом: {result}\033[0m")
    else:
        print(f"Строка '{string}' \033[4mне является палиндромом: {result}\033[0m")
