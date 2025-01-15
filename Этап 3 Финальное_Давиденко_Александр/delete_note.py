from datetime import datetime

# - список заметок
all_info = [{'Заметка № ': 1,
             'имя': 'паша',
             'Описание': 'Нужно создать словать для теста удаления',
             'Статус': ['Новая'],
             'создание заметки': datetime(2024, 12, 27, 0, 0),
             'истечения заметки': datetime(2024, 12, 27, 0, 0),
             'заголовок': ['обучение коду', 'вводный урок', 'простой код']}
         , {'Заметка № ': 2,
            'имя': 'вова',
            'Описание': 'ор',
            'Статус': ['Новая'],
            'создание заметки': datetime(2024, 12, 26, 0, 0),
            'истечения заметки': datetime(2024, 12, 27, 0, 0),
            'заголовок': ['вторая заметка', 'тот же', 'тот же']}
         , {'Заметка № ': 3,
            'имя': 'коля',
            'Описание': 'кака бубу',
            'Статус': ['Новая'],
            'создание заметки': datetime(2027, 12, 15, 0, 0),
            'истечения заметки': datetime(2024, 12, 27, 0, 0),
            'заголовок': ['такая же', 'капуста', 'лук']}]

def delete_note(all_info): # - фунция удаления заметки
    print("Добро пожаловать в 'Менеджер заметок'! Вы можете удалить заметку.")

    delete_ok = False # - переменная флаг с помощью которой будем выходить из главного цикла

    name_zag = input("Вы хотите удалить заметку с по 'Имя' или 'Заголовка': ").lower()

    while not delete_ok:
        if name_zag not in ["имя", "заголовка"]:
            print("Это неверное значение введите знаечение корректно")
            name_zag = input("Вы хотите удалить заметку с по 'Имя' или 'Заголовка': ").lower()
            continue

        # - цикл для удаления заметки по имени
        if name_zag == "имя":
            print("Введенное имя должно в точности совпадать с именем заметки")
            name_key = input("Введите имя заметки которую хотите удалить: ")
            for name_zag in all_info:
                if name_zag ["имя"] == name_key:
                    all_info.remove(name_zag)
                    print(f"Заметка с именем '{name_key}' успешна удалена!")
                    delete_ok = True # - перезаписываем переменную для завершения цикла

                # - перезаписываем номера заметок
                    for index, nomer in enumerate(all_info, start=1):
                        nomer["Заметка № "] = index
                    break
            else:
                print(f"Заметка с именем '{name_key}' не найдена!")
                print("Или")
                continue

        # - цикл для удаления заметки по заголовку
        if name_zag == "заголовка":
            print("Введенный заголовок должно в точности совпадать с заголовком заметки")
            name_key = input("Введите заголовок заметки которую хотите удалить: ")
        for name_zag in all_info:
            if name_key in name_zag["заголовок"]:
                all_info.remove(name_zag)
                print(f"Заметка с заголовком '{name_key}' успешна удалена!")
                delete_ok = True # - перезаписываем переменную для завершения цикла

                # - перезаписываем номера заметок
                for index, nomer in enumerate(all_info, start=1):
                    nomer["Заметка № "] = index
                break
        else:
            print(f"Заметка с заголовком '{name_key}' не найдена!")
            print("Или")
            continue
    return all_info



