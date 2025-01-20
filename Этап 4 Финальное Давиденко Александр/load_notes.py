import re
import ast
from datetime import datetime

def load_notes_from_file():
    d_format = "%Y-%m-%d %H:%M:%S" # - формат даты для проверки

    # Открытие файла для чтения
    filename = open('filename.txt', encoding='utf-8')
    file_content = filename.read()

    zametki = file_content.split("\n\n")  # Заметки разделяются пустой строкой

    all_info = []  # Список для хранения заметок в формате словарей

    # Обработка заметки
    for zametka in zametki:
        zametka_dict = {}  # Словарь для хранения данных одной заметки
        i = zametka.split("\n")  # Разделяем заметку на строки
        for j in i:
            if j.strip():  # Пропускаем пустые строки
                k = re.match(r"([^:]+):\s*(.*)", j) # Разделяем строку на ключ (Условие захвата ([^:]+)) и значение (Условие захвата (.*))
                if k:
                    key = k.group(1).strip() # записываем ключи
                    value = k.group(2).strip() # записываем значения

                    # Преобразуем списки и даты
                    if "[" in value and "]" in value:  # Для списков
                        zametka_dict[key] = ast.literal_eval(value)
                    elif ":" in value and "-" in value:  # Для дат
                        zametka_dict[key] = datetime.strptime(value, d_format)
                    else:
                        zametka_dict[key] = value  # Обычная строка

        # Добавляем словарь заметки в список
        all_info.append(zametka_dict)

    print(all_info)  # Для проверки

load_notes_from_file()